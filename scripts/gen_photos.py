#!/usr/bin/env python3
"""Photographic featured images for blog posts (gpt-image-2).

Replaces the typographic cards with realistic, topic-matched editorial photos —
the Lawnline-level bar. One scene per post, derived from its title/topic, with a
consistent house style: photoreal green-industry scenes, warm natural light,
ABSOLUTELY NO TEXT in the image (the card's title does the talking below it).

Key sourcing (in order): $OPENAI_API_KEY, then Doppler (project mac-claude/prd,
the machine's granted consumer). If no key is available the script exits 0 and
the typographic cards remain — the image gate stays satisfied either way.

Usage:
  python3 scripts/gen_photos.py --selftest      # print mapped prompts, no API
  python3 scripts/gen_photos.py --limit 1       # generate ONE (eyeball first!)
  python3 scripts/gen_photos.py                 # all posts still on cards/fallback
  python3 scripts/gen_photos.py --slug <slug>   # regenerate a specific post
Requires: pillow.
"""
import argparse
import base64
import io
import json
import os
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "assets", "images", "blog", "photos")
MODEL = os.environ.get("PHOTO_MODEL", "gpt-image-2")   # house rule: latest OpenAI image model, never gpt-image-1
W, H = 1200, 630

# topic keyword -> scene. First match wins; order = specificity.
SCENES = [
    ("aeration|overseed", "a core lawn aerator machine pulling fresh soil plugs across a lush green lawn, plugs scattered on the grass, early autumn morning light"),
    ("holiday light|christmas light", "a professional installer on a ladder hanging warm white holiday lights along a beautiful home's roofline at dusk, cozy glow, ladder and clips visible"),
    ("septic", "a concrete septic tank being lowered by excavator into a clean open trench on a residential lot, fresh earth, professional installation in progress"),
    ("excavat", "a modern excavator moving earth on a residential construction site, piles of soil, morning light, operator silhouette in the cab"),
    ("land clearing|forestry|mulch", "a forestry mulcher attachment shredding thick brush at the edge of a wooded property line, wood chips flying, dramatic side light"),
    ("hardscap|paver|outdoor living|patio", "a craftsman's gloved hands laying natural stone pavers on a sand bed for a backyard patio, string lines and rubber mallet visible, finished fire pit blurred in the background"),
    ("website|web design", "over-the-shoulder view of a laptop on a workbench in a landscaper's shop showing a blurred green website layout, work gloves and plans beside it"),
    ("google ads|ppc|advertis|\\bads\\b", "a business owner's desk with a laptop showing softly blurred colorful analytics charts, printed graphs, calculator and coffee, a green lawn visible through the window behind"),
    ("review|reputation", "a smartphone held above a wooden table displaying a softly blurred five-star review screen, scattered gold star cutouts and a small potted plant nearby"),
    ("seo|search|rank", "a landscaping company work truck parked curbside with a phone mounted on the dash showing a softly blurred map with location pins, neighborhood street in background"),
    ("\\bai\\b|artificial intelligence", "a tablet resting on a stack of landscape design plans displaying softly blurred futuristic garden analytics, drafting tools nearby, greenhouse light"),
    ("lawn care|fertiliz|treatment", "a lawn care technician in work boots applying treatment with a spreader across a striped emerald lawn, granules visible in the hopper, golden hour"),
    ("mow|maintenance", "a professional zero-turn mower cutting crisp stripes into a large green lawn, clippings bag and trimmer on a trailer nearby, bright summer morning"),
    ("landscap", "a landscaping crew planting shrubs along a fresh mulch bed at an upscale home, wheelbarrow and spades in frame, vibrant greens, late afternoon sun"),
]
DEFAULT_SCENE = ("a well-organized landscaper's planning desk: printed charts with softly blurred figures, a tablet, "
                 "work gloves and a measuring tape, with a healthy green lawn visible through the window")

STYLE = (" — photorealistic editorial photograph for a professional marketing blog, shallow depth of field, "
         "warm natural light, rich greens, crisp detail. Absolutely no text, no lettering, no numbers, "
         "no logos, no watermarks anywhere in the image. No close-up faces. Landscape orientation.")


VARIANTS = [  # deterministic per-slug so same-topic posts still look distinct
    "shot from a low angle", "shot from slightly above", "wide establishing shot",
    "tight detail shot", "in soft overcast light", "at golden hour",
    "on a bright clear morning", "at blue-hour dusk with warm accents",
]


def scene_prompt(title, cat="strategy", slug=""):
    import hashlib
    import re as _re
    t = (title or "").lower()
    scene = DEFAULT_SCENE
    for pat, s in SCENES:
        if _re.search(pat, t):
            scene = s
            break
    v = VARIANTS[int(hashlib.sha256((slug or t).encode()).hexdigest()[:6], 16) % len(VARIANTS)]
    return f"{scene}, {v}{STYLE}"


def get_key():
    k = os.environ.get("OPENAI_API_KEY")
    if k:
        return k
    try:
        r = subprocess.run(["doppler", "secrets", "get", "OPENAI_API_KEY", "--plain",
                            "--project", "mac-claude", "--config", "prd"],
                           capture_output=True, text=True, timeout=15)
        if r.returncode == 0 and r.stdout.strip().startswith("sk-"):
            return r.stdout.strip()
    except Exception:
        pass
    return None


def generate(key, prompt):
    body = json.dumps({"model": MODEL, "prompt": prompt, "size": "1536x1024",
                       "quality": "high", "n": 1}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/images/generations",
                                 data=body, method="POST",
                                 headers={"Authorization": f"Bearer {key}",
                                          "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        data = json.loads(r.read())
    return base64.b64decode(data["data"][0]["b64_json"])


def to_card(raw):
    from PIL import Image
    img = Image.open(io.BytesIO(raw)).convert("RGB")
    # center-crop to 1200x630 aspect, then resize
    target = W / H
    w, h = img.size
    if w / h > target:
        nw = int(h * target)
        img = img.crop(((w - nw) // 2, 0, (w + nw) // 2, h))
    else:
        nh = int(w / target)
        img = img.crop((0, (h - nh) // 2, w, (h + nh) // 2))
    return img.resize((W, H), Image.LANCZOS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--slug")
    ap.add_argument("--all", action="store_true", help="also replace existing photos")
    args = ap.parse_args()

    blog_path = os.path.join(ROOT, "_blog.json")
    data = json.load(open(blog_path, encoding="utf-8"))

    if args.selftest:
        for p in data["posts"][:14]:
            print(f"\n• {p['title'][:64]}\n  -> {scene_prompt(p['title'], p.get('cat'), p['slug'])[:160]}…")
        return

    key = get_key()
    if not key:
        print("No OPENAI_API_KEY available (env or Doppler mac-claude/prd) — skipping photo "
              "generation; typographic cards remain.")
        return

    done = 0
    for p in data["posts"]:
        img = p.get("image") or ""
        photo_path = f"/assets/images/blog/photos/{p['slug']}.webp"
        eligible = ("/blog/cards/" in img) or ("og-share" in img) or (not img) \
            or (args.all and "/blog/photos/" in img) or (args.slug == p["slug"])
        if args.slug and p["slug"] != args.slug:
            continue
        if not eligible:
            continue
        if os.path.exists(os.path.join(ROOT, photo_path.lstrip("/"))) and not (args.all or args.slug):
            p["image"] = photo_path
            continue
        prompt = scene_prompt(p["title"], p.get("cat"), p["slug"])
        print(f"  generating: {p['slug']}", file=sys.stderr)
        raw = generate(key, prompt)
        os.makedirs(OUT_DIR, exist_ok=True)
        to_card(raw).save(os.path.join(OUT_DIR, f"{p['slug']}.webp"), "WEBP", quality=88)
        p["image"] = photo_path
        p["imageAlt"] = p["title"]
        done += 1
        if args.limit and done >= args.limit:
            break
    open(blog_path, "w", encoding="utf-8").write(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"generated {done} photo(s)")


if __name__ == "__main__":
    main()
