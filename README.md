# Lawn & Land Marketing Website

Live site: https://new.lawnlab.dev
Vercel project: new-lawnlab-deploy
Auto-deploy: push to `main` -> GitHub Actions -> Vercel production

## What this repo is

This repo is the source of truth for the public Lawn & Land website.

Important: this website project is separate from any internal Ground Control concept or naming.

## Current state at a glance

The homepage is still the only intentionally developed public page right now.

Exception:
- `/programs/` now has a lightweight body-layout prototype live for review.
- That page currently includes a simple structure with placeholder/lorem content blocks for:
  - program philosophy
  - quick breakdown
  - Growth Program
  - Authority Program
  - right-stage closing section
- This simpler version was intentionally kept after a more aggressive redesign pass was rejected.
- Treat `/programs/` as an in-review layout prototype, not a finished design system.

All other public pages are intentionally being held in this temporary structure:
- header
- hero banner
- blank body placeholder
- CTA
- footer

The placeholder copy currently used on non-home pages is:
- [Blank body — we will design this shortly.]

This is still intentional for all non-home pages except the current `/programs/` prototype.
Do not start re-writing page bodies unless the design phase has been explicitly restarted.

## Canonical route rules

Use these routes as truth:
- `/marketing-services/` = canonical services hub
- `/contact/` = canonical contact route
- `/programs/...` = canonical program routes
- `/industries/...` = canonical industry routes
- `/resources/...` = canonical resource routes
- `/get-started/book-strategy-call/` = canonical primary CTA destination

Retired / non-canonical routes:
- `/services/`
- `/pricing/`
- `/resources/guides/`
- `/resources/contact/`
- older orphan routes like `/team/`, `/results/`, `/good-fit/`, `/book/`, and older article URLs should stay out of internal linking unless intentionally brought back

## What was already cleaned up

Structural cleanup already completed in this repo:
- `/services/` internal references replaced with `/marketing-services/`
- `/resources/contact/` internal references replaced with `/contact/`
- `/resources/guides/` removed from internal structure
- stale internal orphan links cleaned out of the internal link graph
- `resources/contact/index.html` deleted
- `resources/guides/index.html` deleted
- nav / footer / 404 / duplicated HTML were cleaned for route hygiene

## Where to restart quickly

Start here, in order:
1. `docs/website-source-of-truth/README.md`
2. `docs/website-source-of-truth/build-status.md`
3. `docs/website-source-of-truth/decisions.md`
4. `docs/website-source-of-truth/page-registry.md`
5. `docs/website-source-of-truth/restart-guide.md`

Those docs are the fastest way to recover context.

## Repo structure

```text
├── index.html                          # Homepage (only intentionally developed page right now)
├── about/
├── contact/
├── get-started/book-strategy-call/
├── programs/
├── marketing-services/
├── industries/
├── resources/
├── assets/
│   ├── css/styles.css
│   ├── js/main.js
│   ├── images/
│   └── logos/
├── docs/website-source-of-truth/
└── .github/workflows/deploy.yml
```

## Working rules

- This repo is the website source of truth.
- Every change should go through git.
- Push to `main` deploys production.
- Do not deploy directly with Vercel CLI as the normal workflow.
- Do not reintroduce retired routes unless there is an explicit new decision.
- Do not deepen non-home page bodies until design direction is approved.
- If restarting later, update the docs in `docs/website-source-of-truth/` in the same workstream as any structural decision.

## Recommended next phase

The next phase is still design, not copy.

Best restart path:
1. review Matt's feedback on the current `/programs/` prototype
2. decide what to keep / kill from that layout
3. redesign the Programs page with stronger visual hierarchy before writing final copy
4. only then use the approved design direction to guide other non-home pages

## Deployment

GitHub Actions workflow:
- `.github/workflows/deploy.yml`
- pushes to `main` trigger Vercel production deploy

## Maintainer note for future restart

If you come back cold later, assume this:
- homepage = live developed benchmark page
- everything else = intentionally held shell, except `/programs/` which now has a simple layout prototype under review
- route hygiene work is already done
- the decision that matters most is preserving the blank-body convention on non-home pages while using `/programs/` as the current design exploration page
