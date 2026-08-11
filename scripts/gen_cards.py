#!/usr/bin/env python3
"""Generate a unique, on-brand featured card for every blog post.

Deterministic editorial covers (1200x630 webp): dark brand background, category
accent color, the post's actual title typeset large, and a per-slug geometric
motif so no two cards look alike. Replaces the shared og-share.jpg fallback and
runs as part of the publish pipeline so a duplicate featured image can never
ship again (scripts/check_blog_images.py enforces it).

Usage:  python3 scripts/gen_cards.py            # cards for posts on the fallback / missing files
        python3 scripts/gen_cards.py --all      # regenerate every generated card
Requires: pillow (pip install pillow). Fonts live in assets/build/fonts (OFL).
"""
import hashlib
import json
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "assets", "images", "blog", "cards")
W, H = 1200, 630
BG_TOP, BG_BOT = (7, 16, 10), (13, 27, 16)
WHITE = (255, 255, 255)
MUTED = (255, 255, 255, 115)
FAINT = (255, 255, 255, 60)
ACCENTS = {  # category -> brand accent
    "strategy": (172, 231, 29),      # lime
    "seo": (93, 202, 73),            # green
    "ads-social": (169, 139, 255),   # twilight tint
    "growth-stories": (240, 180, 41) # amber
}
FALLBACK_MARKER = "og-share"

MULISH = os.path.join(ROOT, "assets", "build", "fonts", "Mulish[wght].ttf")
INTER = os.path.join(ROOT, "assets", "build", "fonts", "Inter[opsz,wght].ttf")


def font(path, size, axes):
    f = ImageFont.truetype(path, size)
    f.set_variation_by_axes(axes)
    return f


def seed(slug):
    return int(hashlib.sha256(slug.encode()).hexdigest()[:8], 16)


def bg(draw):
    for y in range(H):
        t = y / H
        c = tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3))
        draw.line([(0, y), (W, y)], fill=c)


def motif(img, draw, slug, accent):
    """One of four brand-geometry motifs, chosen deterministically per slug."""
    s = seed(slug)
    kind = s % 4
    a25 = accent + (46,)
    a60 = accent + (110,)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    if kind == 0:      # concentric arcs bleeding off the right edge
        cx, cy = W + 60, 90 + (s // 7) % 240
        for i, r in enumerate((150, 230, 310)):
            d.arc([cx - r, cy - r, cx + r, cy + r], 90, 270,
                  fill=a60 if i == 0 else a25, width=10 - i * 3)
    elif kind == 1:    # diagonal beam, lower right
        off = (s // 11) % 160
        d.polygon([(W - 340 - off, H), (W - 180 - off, H), (W + 80, 210), (W - 80, 210)], fill=accent + (26,))
        d.line([(W - 250 - off, H), (W, 260)], fill=a60, width=6)
    elif kind == 2:    # dot grid, upper right
        ox, oy = W - 330, 70 + (s // 13) % 110
        for r in range(5):
            for c in range(8):
                d.ellipse([ox + c * 40 - 4, oy + r * 40 - 4, ox + c * 40 + 4, oy + r * 40 + 4],
                          fill=a25 if (r + c) % 2 else a60)
    else:              # radar rings, upper right (the product motif)
        cx, cy = W - 170, 130 + (s // 17) % 130
        for r in (36, 78, 120):
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=a25, width=4)
        d.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=a60)
    img.alpha_composite(layer)


def wrap_title(draw, title, f, max_w):
    words, lines, cur = title.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def render(slug, title, cat):
    accent = ACCENTS.get(cat, ACCENTS["strategy"])
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)
    bg(draw)
    motif(img, draw, slug, accent)
    draw = ImageDraw.Draw(img)

    x = 84
    eyebrow = font(INTER, 26, [14, 650])
    draw.text((x, 74), "LAWN & LAND MARKETING", font=eyebrow, fill=MUTED)
    # accent rule + category
    draw.rectangle([x, 122, x + 56, 127], fill=accent)
    cat_label = {"strategy": "STRATEGY", "seo": "SEO", "ads-social": "ADS & SOCIAL",
                 "growth-stories": "CLIENT STORIES"}.get(cat, "STRATEGY")
    draw.text((x + 74, 112), cat_label, font=font(INTER, 24, [14, 700]), fill=accent)

    # title block: autosize until it fits BOTH width (<=4 lines) and the vertical
    # band between the header (190) and the footer zone (H-116)
    max_w = W - x - 220
    top, bottom = 190, H - 116
    for size in (88, 80, 72, 66, 60, 54, 48):
        tf = font(MULISH, size, [800])
        lines = wrap_title(draw, title, tf, max_w)
        line_h = int(size * 1.16)
        total_h = line_h * len(lines)
        if len(lines) <= 4 and total_h <= (bottom - top):
            break
    y = top + max(0, ((bottom - top) - total_h) // 2)
    for ln in lines:
        draw.text((x, y), ln, font=tf, fill=WHITE)
        y += line_h

    draw.text((x, H - 84), "lawnandlandmarketing.com", font=font(INTER, 24, [14, 500]), fill=FAINT)

    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, f"{slug}.webp")
    img.convert("RGB").save(out, "WEBP", quality=88)
    return f"/assets/images/blog/cards/{slug}.webp"


def main():
    regen_all = "--all" in sys.argv
    blog_path = os.path.join(ROOT, "_blog.json")
    data = json.load(open(blog_path, encoding="utf-8"))
    changed = 0
    for p in data["posts"]:
        img = p.get("image") or ""
        local = os.path.join(ROOT, img.lstrip("/")) if img else ""
        needs = (FALLBACK_MARKER in img) or (not img) or (not os.path.exists(local)) \
            or (regen_all and "/blog/cards/" in img)
        if not needs:
            continue
        p["image"] = render(p["slug"], p["title"], p.get("cat", "strategy"))
        p["imageAlt"] = p["title"]
        changed += 1
        print(f"  card: {p['slug']}")
    if changed:
        open(blog_path, "w", encoding="utf-8").write(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"generated {changed} card(s)")


if __name__ == "__main__":
    main()
