# Routing Rules

## Canonical Rules
- Canonical contact route is `/contact/`.
- Canonical service hub is `/marketing-services/`.
- Canonical service detail pages live under `/marketing-services/...`.
- Programs live under `/programs/...`.
- Industry pages live under `/industries/...`.
- Resource pages live under `/resources/...` except contact, which is top-level at `/contact/`.

## Killed Routes
These should not appear in nav, footer, CTAs, page copy, breadcrumbs, sitemap planning docs, or internal links.
- `/services/`
- `/pricing/`
- `/resources/guides/`

## Legacy Routes
These are legacy or non-canonical and should be removed from internal linking or redirected intentionally.
- `/resources/contact/` → use `/contact/`
- legacy service detail routes under `/services/...`
- any pricing references that imply `/pricing/` is a live page

## Sitewide Link Hygiene Rules
1. Main navigation must point Marketing Services to `/marketing-services/`, not `/services/`.
2. Footer service links must point to `/marketing-services/...` routes only.
3. Contact links should resolve to `/contact/` unless a specific CTA should go directly to `/get-started/book-strategy-call/`.
4. Killed pages should not remain discoverable through 404 pages, popular links, or footer lists.
5. If a route is intentionally retired, document it in `decisions.md` and remove it from `page-registry.md` as canonical.

## Cleanup Status
- Main nav now points Marketing Services to `/marketing-services/`.
- Homepage service CTAs now use `/marketing-services/...` child routes.
- Internal linking no longer exposes `/resources/contact/`.
- `/resources/guides/` has been removed from internal structure and the page file was deleted.
- 404 page has been cleaned so it no longer promotes the retired service/contact/guides routes.

## Remaining Link QA To Handle Later
- Review older secondary links to non-canonical or missing pages such as `/results/`, `/team/`, and a few legacy blog/article routes.
- Decide whether any retired routes should eventually receive redirects at the hosting layer.
