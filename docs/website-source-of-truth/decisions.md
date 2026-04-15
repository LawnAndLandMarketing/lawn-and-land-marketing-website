# Website Decisions Log

## 2026-04-14
- This public website build should stay separate from the internal Ground Control concept and naming.
- The repo should maintain a dedicated website-specific source-of-truth folder for architecture and progress tracking.
- `/marketing-services/` is the canonical service section.
- `/services/` is intentionally not part of the approved website and should be retired from all internal linking.
- `/pricing/` is intentionally not part of the approved website and should not be reintroduced as a canonical page.
- `/contact/` is the canonical contact route.
- `/resources/contact/` is non-canonical and should be removed from internal linking.
- `/resources/guides/` is out of scope and should be retired.
- Approved sitemap includes Home, About, Programs, Marketing Services, Industries, Resources, and Get Started / Book Strategy Call.
- Lawnline (`https://lawnline.marketing/`) is the primary public benchmark to beat on structure, SEO strength, and overall execution quality.

## 2026-04-15
- Approved structural cleanup pass has been applied in the repo.
- `_nav.html`, `_footer.html`, homepage/service CTAs, duplicated page HTML, and `404.html` were updated to remove the retired route drift.
- `resources/contact/index.html` and `resources/guides/index.html` were deleted from the repo.
- Next work should shift from route hygiene to finishing the highest-leverage thin pages.

## Open Decisions To Track Later
- Whether any retired routes should be redirected intentionally versus simply removed from internal linking.
- Exact completion order of service pages after top-level architecture cleanup is done.
- Whether additional proof-heavy pages like results or case studies should return later in a different form.
