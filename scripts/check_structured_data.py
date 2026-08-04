#!/usr/bin/env python3
"""Validate every inline JSON-LD block in the static site.

Fails on malformed JSON or duplicate object properties. Duplicate properties are
invalid for Google's structured-data parser even though Python's default JSON
loader would silently keep the final value.
"""
from __future__ import annotations

import json
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".worktrees", "node_modules"}


class JsonLdExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.blocks: list[str] = []
        self._capturing = False
        self._parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "script":
            return
        values = {key.lower(): value for key, value in attrs}
        script_type = (values.get("type") or "").lower()
        if script_type == "application/ld+json":
            self._capturing = True
            self._parts = []

    def handle_data(self, data: str) -> None:
        if self._capturing:
            self._parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script" and self._capturing:
            self.blocks.append("".join(self._parts))
            self._capturing = False
            self._parts = []


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    counts = Counter(key for key, _ in pairs)
    duplicates = sorted(key for key, count in counts.items() if count > 1)
    if duplicates:
        raise ValueError(f"duplicate unique property: {', '.join(duplicates)}")
    return dict(pairs)


def html_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.html")
        if not any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts)
    )


def main() -> None:
    errors: list[str] = []
    block_count = 0

    for path in html_files():
        parser = JsonLdExtractor()
        parser.feed(path.read_text(encoding="utf-8"))
        for index, block in enumerate(parser.blocks, start=1):
            block_count += 1
            try:
                json.loads(block, object_pairs_hook=reject_duplicate_keys)
            except (json.JSONDecodeError, ValueError) as exc:
                relative = path.relative_to(ROOT)
                errors.append(f"{relative} JSON-LD block {index}: {exc}")

    if errors:
        raise SystemExit("Structured data validation failed:\n- " + "\n- ".join(errors))

    print(f"Structured data validation: PASS ({block_count} JSON-LD blocks checked)")


if __name__ == "__main__":
    main()
