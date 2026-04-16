# Restart Guide

Use this file when coming back to the Lawn & Land website after time away.

## One-paragraph truth

The homepage is still the only intentionally developed page right now. Most other public pages remain in the temporary shell state: header + hero + blank-body placeholder + CTA/footer. The one exception is `/programs/`, which now has a simple live layout prototype with lorem placeholder content. A more aggressive redesign was attempted and rejected, then the simpler version was restored. Route hygiene is already clean, and the next real phase is still design refinement — not final long-form body writing.

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

Current exception:
- `/programs/` no longer uses the blank-body placeholder
- it currently has a simple review prototype with these sections:
  - program philosophy
  - quick breakdown
  - Growth Program
  - Authority Program
  - right-stage closing section
- copy inside that body is still placeholder/lorem and should be treated as layout scaffolding, not approved messaging

Current placeholder text:
- [Blank body — we will design this shortly.]

Do not expand non-home pages with long body copy unless the design phase has restarted.
Do not assume the current `/programs/` layout is approved; it is only the current review baseline.

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
- `/programs/` reopened as the active design exploration page
- a simple Programs prototype is currently live
- a stronger v2 redesign was rejected and reverted

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
- most non-home pages show hero + blank-body placeholder + CTA/footer
- `/programs/` shows the simpler prototype with five body sections, not the blank-body placeholder

## The next best move when this project resumes

Recommended order:
1. review Matt's detailed feedback on the current `/programs/` prototype
2. redesign `/programs/` from that feedback until the design direction is right
3. use the approved Programs direction to guide the non-home page system
4. only then decide what deeper content needs to be written

## Important guardrail

If the project is resumed months later, do not assume previously written redesigns should be restored.
The last explicit direction from Matt was to keep the simpler `/programs/` prototype live while he reviews it and prepares detailed feedback, and to keep other non-home pages blank-bodied until design is approved.
