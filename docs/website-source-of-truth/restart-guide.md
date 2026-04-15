# Restart Guide

Use this file when coming back to the Lawn & Land website after time away.

## One-paragraph truth

The homepage is the only intentionally developed page right now. All other public pages were intentionally reset to a temporary shell state: header + hero + blank-body placeholder + CTA/footer. Route hygiene was already cleaned up, canonical routes are set, and the next real phase is design — not more long-form body writing.

## The fastest possible restart path

Read these in order:
1. `README.md`
2. `docs/website-source-of-truth/build-status.md`
3. `docs/website-source-of-truth/decisions.md`
4. `docs/website-source-of-truth/page-registry.md`
5. `docs/website-source-of-truth/routing-rules.md`

If that is all you read, you should still be operational quickly.

## Current website convention

Homepage:
- intentionally developed
- keep as the current strongest benchmark page in the repo

All other public pages:
- header
- hero banner
- blank body placeholder
- CTA
- footer

Current placeholder text:
- [Blank body — we will design this shortly.]

Do not expand non-home pages with long body copy unless the design phase has restarted.

## Canonical routes

These are the routes to treat as truth:
- `/marketing-services/`
- `/contact/`
- `/programs/...`
- `/industries/...`
- `/resources/...`
- `/get-started/book-strategy-call/`

## Retired / non-canonical routes

Keep these out of internal linking unless there is an explicit decision to bring them back:
- `/services/`
- `/pricing/`
- `/resources/guides/`
- `/resources/contact/`
- older orphan routes such as `/team/`, `/results/`, `/good-fit/`, `/book/`, and legacy article URLs

## What work has already been completed

Structural work already done:
- nav / footer / 404 / duplicated page HTML cleaned for canonical routing
- `/services/` family retired from internal linking in favor of `/marketing-services/`
- `/resources/contact/` retired from internal linking in favor of `/contact/`
- `/resources/guides/` retired and removed
- stale orphan internal links cleaned from the repo

Current page-state work already done:
- non-home pages reset back to shell state intentionally
- homepage left as the only developed page

## If you need to verify the state quickly

Check these live URLs first:
- `/`
- `/about/`
- `/contact/`
- `/programs/`
- `/marketing-services/`
- `/get-started/book-strategy-call/`

Expected outcome:
- homepage has real content
- non-home pages show hero + blank-body placeholder + CTA/footer

## The next best move when this project resumes

Recommended order:
1. design the shared non-home page body system
2. choose the first page type to fully design
3. apply the design system to a small set of pages
4. only then decide what deeper content needs to be written

## Important guardrail

If the project is resumed months later, do not assume previously written body expansions should be restored.
The last explicit direction from Matt was to keep non-home pages blank-bodied until design is approved.
