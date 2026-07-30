# Routing Rules

## Canonical Rules
- Canonical contact route is `/contact/`.
- Canonical service hub is `/marketing-services/`.
- Canonical service detail pages live under `/marketing-services/...`.
- Programs live under `/programs/...`.
- Industry pages live under `/industries/...`.
- Resource pages live under `/resources/...` except contact, which is top-level at `/contact/`.
- Case studies live under `/case-studies/...` (reintroduced 2026-06-21 per builder directive; previously killed). No index page exists at `/case-studies/` itself yet, so its breadcrumb crumb is a non-link label. First page: `/case-studies/precision/`.

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

## Launch redirects (301) — old WordPress URLs
Implemented in `vercel.json` (`redirects`, `permanent: true` = 308, SEO-equivalent to 301). Each is
registered both with and without a trailing slash so either form resolves. They are active on the production
domain `lawnandlandmarketing.com` after cutover. Audited 2026-06-23 against `https://lawnandlandmarketing.com/page-sitemap.xml` (29 pages) plus the `/grow` funnel.

**Same URL, already rebuilt (no redirect needed):** `/`, `/about/`, `/contact/`, `/programs/`, `/privacy-policy/`, `/terms/`.

**Rebuilt at a new URL (301):**
- `/solutions/` -> `/marketing-services/`
- `/solutions/websites/` -> `/marketing-services/website-design/`
- `/solutions/local-seo/` -> `/marketing-services/local-seo/`
- `/solutions/reputation-management/` -> `/marketing-services/reputation-management/`
- `/solutions/paid-ads/` -> `/marketing-services/google-ads/` (Meta is its own page: `/marketing-services/meta-ads/`)
- `/solutions/lead-nurturing/` -> `/marketing-services/automation/`
- `/precision-case-study/` -> `/case-studies/precision/`
- `/rock-solid-case-study/` -> `/case-studies/rock-solid/`
- `/reviews/` -> `/resources/experiences-reviews/`
- `/blog/` -> `/resources/blog/` (individual posts handled by the blog-migration redirect map)
- `/blog/category/seo/` -> `/resources/blog/category/seo/` (both trailing-slash variants registered)
- `/our-team/` -> `/about/#team`
- `/is-marketing-right-for-us/` -> `/about/`
- `/author/matt-foreman/` -> `/matt-foreman/` (INVERTED 2026-07-07: the entity hub is now the canonical page; the old author-archive URL 301s to it. The previous alias in the other direction was removed from `vercel.json`.)
- `/schedule/` -> `/get-started/book-strategy-call/`
- `/podcast-sign-up/` -> `/resources/mow-money-mow-problems-podcast/`
- `/be-a-guest/` -> `/resources/mow-money-mow-problems-podcast/`
- `/submission-received/` -> `/confirmation/`

**Preserved funnels (rebuilt at the SAME URL, not redirected):**
- `/grow/` — the Facebook ad funnel. Rebuilt 2026-06-23 (`grow/index.html`, excluded from `build.py` via SKIP_DIRS). Self-contained funnel chrome (no main nav). Carries the legacy Meta Pixel `235509009483991`, Google Ads tag `AW-18165400861`, GHL booking calendar `u7agGU9Xwo0kjAsLlKif`, and `noindex` — so Facebook ads/redirects are untouched.
- `/checklist/` — GBP-checklist lead magnet (INDEXED SEO page). REBUILT 2026-06-23: modern on-brand dark page (`checklist/index.html`, self-contained, excluded from `build.py`). Two-column hero (value bullets + a NATIVE lead-capture form: First/Last/Email/Phone, the same fields as the old GHL form `OhY6Qt2Y4QWBBQlExOxg`). On submit it captures the lead (localStorage stub) and delivers the PDF; **TODO before launch: wire the capture to GHL** (inbound webhook or API) so leads are actually saved. Precision proof (+297% calls in five months) links to the case study. The `checklist-download` redirect still serves the PDF directly. No FB pixel yet (pending the site-wide pixel decision).

**Sunset funnels (301 to nearest live equivalent so old ad/email links don't 404):**
- `/free-tools/` -> `/downloads/free-tools-for-green-industry.pdf` (the re-hosted PDF)
- `/level-up-webinar/` -> `/`
- `/2025-plan/` -> `/resources/blog/`
- `/free-book-old/` -> `/`

**Dropped (no redirect, allowed to 404):** `/notapage/` (legacy test page).

## Remaining Link QA To Handle Later
- Decide whether any retired routes should eventually receive redirects at the hosting layer.
- If a route is intentionally reintroduced later, record that decision before adding it back into internal linking.

## 2026-07-30 migration consolidation
- Repaired the old WordPress SEO-category 404 by permanently redirecting both `/blog/category/seo`
  and `/blog/category/seo/` to the canonical SEO category hub.
- Added contextual links from the homepage, SEO category hub, and three relevant articles to the
  lawn-care and landscaping SEO service pages. These links are in body copy, not global navigation.
- Kept mismatched legacy article redirects out of this low-risk batch. Those topics need genuinely
  useful replacement articles before their redirects are changed.

## Killed routes — fuller list (keep out of nav, footer, CTAs, copy, breadcrumbs, sitemap, links)
`/services/` (+ children) · `/pricing/` · `/resources/guides/` · `/resources/contact/` ·
`/results/` · `/team/` · `/good-fit/` · `/book/` · `/podcast/` ·
`/tools/marketing-audit/` · older orphan/article URLs. Use the canonical equivalents instead
(`/case-studies/` was reintroduced 2026-06-21 as an approved silo and is no longer killed)
(`/marketing-services/...`, `/contact/`, `/resources/...`, `/get-started/book-strategy-call/`).

## Current build convention (updated 2026-06-15)
- Developed: the homepage, the 8 `/marketing-services/*` pages + hub, and both program pages
  (`/programs/growth/`, `/programs/authority/`).
- Still shells (don't deepen with long copy until their design is approved or they're scheduled):
  the 8 `/industries/*` pages, `/about/`, `/contact/`, and `/resources/*`.
  (The 8 industry pages are the next scheduled build.)
- See `page-registry.md` for per-page status and `build-status.md` for priorities.
