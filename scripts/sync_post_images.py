#!/usr/bin/env python3
"""Sync every article's social + schema image to its _blog.json featured image.

For each post: patch <meta property="og:image">, <meta name="twitter:image">, and
the BlogPosting schema "image" to the post's own card, so shares and rich results
carry the unique cover (gen_blog.py already stamps the on-page hero). Idempotent;
runs in the publish pipeline after gen_cards.py.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://lawnandlandmarketing.com"

data = json.load(open(os.path.join(ROOT, "_blog.json"), encoding="utf-8"))
patched = 0
for p in data["posts"]:
    img = p.get("image") or ""
    if not img.startswith("/"):
        continue
    full = SITE + img
    path = os.path.join(ROOT, "resources", "blog", p["slug"], "index.html")
    if not os.path.exists(path):
        continue
    h = open(path, encoding="utf-8").read()
    orig = h
    h = re.sub(r'(<meta property="og:image" content=")[^"]*(")', rf"\g<1>{full}\g<2>", h, count=1)
    h = re.sub(r'(<meta name="twitter:image" content=")[^"]*(")', rf"\g<1>{full}\g<2>", h, count=1)
    # BlogPosting schema image (compact JSON inside the ld+json script)
    h = re.sub(r'("@type":\s*"BlogPosting".*?"image":\s*")[^"]*(")',
               rf"\g<1>{full}\g<2>", h, count=1, flags=re.S)
    if h != orig:
        open(path, "w", encoding="utf-8").write(h)
        patched += 1
print(f"synced social/schema images on {patched} article(s)")
