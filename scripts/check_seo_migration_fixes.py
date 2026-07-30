#!/usr/bin/env python3
"""Regression checks for the July 2026 SEO migration-consolidation batch."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def require_link(relative: str, href: str, anchor_text: str) -> None:
    html = read(relative)
    exact = f'<a href="{href}">{anchor_text}</a>'
    assert exact in html, f"{relative} is missing contextual link: {exact}"


def check_redirects() -> None:
    config = json.loads(read("vercel.json"))
    redirects = config["redirects"]
    expected = {
        "/blog/category/seo": "/resources/blog/category/seo/",
        "/blog/category/seo/": "/resources/blog/category/seo/",
    }
    for source, destination in expected.items():
        matches = [rule for rule in redirects if rule.get("source") == source]
        assert matches, f"missing redirect rule for {source}"
        assert len(matches) == 1, f"duplicate redirect rules for {source}"
        rule = matches[0]
        assert rule.get("destination") == destination, (
            f"{source} should redirect to {destination}, got {rule.get('destination')}"
        )
        assert rule.get("permanent") is True, f"{source} must be permanent"


def check_contextual_links() -> None:
    require_link(
        "index.html",
        "/marketing-services/lawn-care-seo/",
        "SEO for lawn care companies",
    )
    require_link(
        "index.html",
        "/marketing-services/landscaping-seo/",
        "SEO for landscaping companies",
    )
    require_link(
        "resources/blog/category/seo/index.html",
        "/marketing-services/local-seo/",
        "local SEO for green-industry companies",
    )
    require_link(
        "resources/blog/category/seo/index.html",
        "/marketing-services/lawn-care-seo/",
        "lawn care SEO",
    )
    require_link(
        "resources/blog/category/seo/index.html",
        "/marketing-services/landscaping-seo/",
        "landscaping SEO",
    )
    require_link(
        "resources/blog/lawn-landscaping-local-seo/index.html",
        "/marketing-services/lawn-care-seo/",
        "lawn care SEO",
    )
    require_link(
        "resources/blog/lawn-landscaping-local-seo/index.html",
        "/marketing-services/landscaping-seo/",
        "landscaping SEO",
    )
    require_link(
        "resources/blog/7-easy-steps-to-dominate-local-seo-for-your-landscaping-business/index.html",
        "/marketing-services/landscaping-seo/",
        "landscaping SEO services",
    )
    require_link(
        "resources/blog/the-ultimate-guide-to-online-landscape-marketing/index.html",
        "/marketing-services/landscaping-seo/",
        "SEO for landscaping companies",
    )


def check_generator_idempotency() -> None:
    generated_indexes = [
        "resources/blog/index.html",
        "resources/blog/page/2/index.html",
        "resources/blog/category/ads-social/index.html",
        "resources/blog/category/growth-stories/index.html",
        "resources/blog/category/podcast/index.html",
        "resources/blog/category/seo/index.html",
        "resources/blog/category/strategy/index.html",
    ]
    for relative in generated_indexes:
        count = read(relative).count(".blog-pagination{")
        assert count == 1, f"{relative} has {count} pagination style blocks; expected 1"


def check_link_visibility() -> None:
    homepage = read("index.html")
    assert ".svc-panel-content p a {" in homepage, (
        "homepage contextual service links need a visible inline-link style"
    )
    category = read("resources/blog/category/seo/index.html")
    assert ".blog-cat-intro a{" in category, (
        "generated category intro links need a visible inline-link style"
    )


def main() -> None:
    check_redirects()
    check_contextual_links()
    check_generator_idempotency()
    check_link_visibility()
    print("SEO migration consolidation checks: PASS")


if __name__ == "__main__":
    main()
