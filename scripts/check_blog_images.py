#!/usr/bin/env python3
"""Blog quality gate: fail the publish if featured images repeat or slugs collide.

Hard rules (exit 1 on violation):
  1. No post may use the shared brand fallback (og-share) as its featured image.
  2. No two posts may share the same featured image.
  3. No two posts may share the same slug.
  4. Every featured image file must exist.

Run in every publish pipeline (the operator runs it before opening a PR) and any
time by hand: python3 scripts/check_blog_images.py
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = json.load(open(os.path.join(ROOT, "_blog.json"), encoding="utf-8"))

errors = []
seen_img, seen_slug = {}, {}
for p in data["posts"]:
    slug, img = p["slug"], p.get("image") or ""
    if slug in seen_slug:
        errors.append(f"DUPLICATE SLUG: '{slug}' appears more than once in _blog.json")
    seen_slug[slug] = True
    if "og-share" in img or not img:
        errors.append(f"FALLBACK/MISSING IMAGE: {slug} -> '{img}'")
    elif img in seen_img:
        errors.append(f"DUPLICATE IMAGE: {slug} shares '{img}' with {seen_img[img]}")
    else:
        seen_img[img] = slug
    if img and not os.path.exists(os.path.join(ROOT, img.lstrip("/"))):
        errors.append(f"IMAGE FILE MISSING on disk: {slug} -> {img}")

if errors:
    print("BLOG IMAGE GATE: FAIL")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print(f"BLOG IMAGE GATE: OK ({len(data['posts'])} posts, all images unique and present)")
