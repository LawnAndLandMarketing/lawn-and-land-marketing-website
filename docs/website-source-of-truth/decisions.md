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

## 2026-04-15 (continued)
- A second route-hygiene pass removed the remaining broken internal links to orphan routes like `/team/`, `/results/`, `/good-fit/`, `/book/`, and old article URLs.
- Top-priority thin pages were deepened in this workstream: `/programs/`, `/marketing-services/`, `/about/`, and `/contact/`.
- The next highest-leverage page work should move deeper into service detail pages rather than reopening top-level architecture decisions.

## 2026-04-15 (latest)
- Homepage remains the only intentionally developed public page for now.
- All non-home public pages should currently stay header + hero + blank-body placeholder + CTA/footer until the design direction is approved.
- Written body expansion on non-home pages should pause until that design phase begins.

## 2026-04-16
- `/programs/` has been reopened as the current design exploration page.
- A simple body-layout prototype was added to `/programs/` with placeholder/lorem blocks for philosophy, quick breakdown, Growth, Authority, and right-stage guidance.
- A more aggressive visual redesign pass for `/programs/` was attempted and then rejected.
- The simpler pre-v2 Programs version was restored and is the current live state to review from.
- For now, keep the simpler `/programs/` prototype live while Matt reviews and prepares detailed feedback.
- Do not assume the rejected v2 direction should be revived without explicit approval.

## 2026-06-13
- Header and footer are now truly single-source. `_header.html` (announcement bar + nav) and `_footer.html` are the only files to edit; `build.py` stamps them into every page and runs automatically on Vercel deploy via `vercel.json` buildCommand.
- The announcement bar was folded into the universal header and unified across all 31 pages (text + `/contact/` link). Previously the homepage used a relative link and `/404.html` had a stray promo.
- Replaced the old fragile `build-pages.py` (hardcoded `/tmp` path) with `build.py`. Refreshed `_footer.html` to match the current live footer (the partial had gone stale). Brought `/404.html` into the universal header/footer.
- Decision pending from Matt: begin building out the non-home page bodies ("build it out to the best solution") — establish a reusable page design system from the homepage, then roll out across the sitemap.

## 2026-06-14 — Industries locked · homepage deepened · Growth built · `.hl` marker
- **Industries — canonical 8 LOCKED:** lawn-care, lawn-maintenance, landscaping, outdoor-living,
  land-clearing, excavation, septic-services, holiday-lighting. Non-canonical industries (e.g. snow
  removal) were deleted; nav submenu, footer, and `sitemap.xml` reconciled. Icons: Landscaping =
  tree-palm, Lawn Care = sprout (Lucide). Mobile "Industries We Serve" is a compact 2-up grid.
- **Homepage conversion pass:** reordered to hero → stats → industries → services → proof → programs
  → Why L&L → testimonials → logo marquee → FAQ → CTA. Removed the unfinished Blog from nav/flow.
  Added a mini case-study proof row (3 real clients with photos + before→after numbers; no % badges).
  Moved the "Trusted By" logo marquee above testimonials onto the Twilight dot-grid band. Testimonial
  stars → gold-glow. "Why L&L" tightened ("5+ Years" badge → "100% Green Industry Focused"). Applied a
  verified pre-launch audit; softened the ROI claim to a defensible range (kept the dollar figure off
  the page so it never implies pricing). Unified section backgrounds to kill reorder seams. Fixed the
  mobile mega-menu (caret submenus expand instead of navigating).
- **`.hl` Twilight highlight — new reusable brand element:** skewed (−11°) `#6837EF` swipe behind the
  lower portion of one impact phrase, white text, sharp edges. Defined in `styles.css`; **locked into
  the brand kit** (brandkit.lawnlab.dev, §09 Typography). One phrase per surface; never on body or greens.
- **Growth Program page built:** scrapped the old lorem `/programs/` body; built `/programs/growth/`
  lean (Hormozi-style), hand-built (not the generated service template) reusing the same classes.
  Pain cards → four-pillar "What you get" on the Twilight textured band → 2-col Why Us → Twilight CTA.
  **Avatar correction (important):** Growth = $400K–$1M "six-figure" companies that grew OFFLINE and are
  trying to get FOUND for the first time — NOT vendor-sprawl/agency-scar pains (those are Authority).
  A lime-inverted "what you get" was tried and rejected ("too bright") → Twilight purple textured band.
- **Mobile marquee fix:** homepage logo marquee didn't start on iOS until tapped. Cause: 36 lazy, unsized
  logos collapsed the `max-content` track to ~0 width + no GPU layer promotion. Fix: reserve each logo's
  intrinsic size (`width=99 height=38`) + eager-load + promote the track (translateZ / will-change /
  translate3d keyframes). Desktop unchanged.

## 2026-06-15 — Growth SEO pass · footer · docs refresh
- **Growth SEO (from an external audit):** added `Service` + `BreadcrumbList` JSON-LD, `og:url`, Twitter
  card. Aligned the meta description to "six-figure lawn care and landscaping companies" (~155 chars) to
  match the body. Promoted the hero "Growth Program" kicker to the page `<h1>` (keyword in H1), demoting
  the emotional headline to `<h2>` — pixel-identical on screen. Reworked "Why Us" into two columns (image
  placeholder left, copy right, left-aligned). `og:image` deferred to launch.
- **Footer:** "Green industry specialists since **2022**" (corrected from 2020).
- **Schema/canonical convention:** schema uses the production domain (`lawnandlandmarketing.com`); page
  canonicals still point to staging (`new.lawnlab.dev`) and flip at launch.
- **Docs refresh:** brought `CLAUDE.md`, `README.md`, `PAGES_MANIFEST.md`, and the whole
  `docs/website-source-of-truth/` set current; rebuilt `sitemap.xml` to the real routes (the old one
  listed killed routes — `/services/...`, `/pricing/`, `/case-studies/`, fake blog posts).

## 2026-06-15 — Authority Program (flagship) built
- Built `/programs/authority/` as the flagship, cloned from the Growth structure and elevated for the
  **7-figure+** avatar (established, doing real revenue, wants to *dominate* — NOT Growth's get-found
  pains). Sections: hero ("be the most known") → 3 red pain cards (outranked by inferior competitors /
  patchwork vendors / plateaued) → Twilight four-pillar "domination" band (Total Search Domination /
  Everywhere They Look / A Reputation That Closes / Your Whole Marketing Team) → full "everything
  included" deliverables grid (~18 items) → **value play** ("a whole team for less than one hire" — uses
  the ~$60–80K employee-cost anchor, never our fee) → **Roadmap to Domination** timeline (Foundation →
  Climb → Market Dominance → Total Control) → partnership + credibility two-column (50+ clients,
  $300K–$14M+, 97% retention, NALP, Google Partner) → Twilight CTA. Built from the real contract + the
  New Horizon pitch deck. `Service` + `BreadcrumbList` schema, OG/Twitter. **No pricing.** Deliberately
  excluded the deck's "Seven Figure Agency" mention (third-party brand) and specific client P&L numbers;
  used L&L's own agency credentials as proof instead. Both program pages now cross-link.
- **Refined same-day per owner feedback:** dropped "Flagship" from the hero pill; `.hl` Twilight
  highlight applied to "THE company" (problem) and "For less than one hire." (value headline);
  removed the "$60–80K math" reframe line under the value cards and tightened the value→roadmap
  spacing; re-weighted the value cards to **40/60** with the Authority-team box emphasized (bigger
  header, brighter copy, stronger border + purple glow) as the obvious choice; **replaced the
  credibility stat row with the homepage "Proof, Not Promises" section** (real client results —
  Rock Solid, Precision, From The Ground Up). The agency credentials (50+ / $300K–$14M+ / 97% /
  NALP) still live in the Why-L&L partnership paragraph.
- **Universal (same session):** every hero/banner subhead is now **full white `#fff`** (was
  `rgba(255,255,255,0.78)` / `var(--body)` grey) — `.hero-copy p` on all `.simple-hero` pages +
  `.hero-sub` on the homepage. `styles.css?v=135 → 136`.

## 2026-06-15 — Programs hub + submenu icons
- Built the **`/programs/` hub** as a simple two-program window (owner: "a quick window into both
  programs"): hero → "Two Programs / Find the one built for your stage" → two cards (Growth = six-figure,
  Authority = seven-figure; reuses the homepage `.program-card` pattern, Authority featured) each linking
  into its program page → a "not sure which?" book-a-call line. Inspiration: lawnline.marketing/programs/.
- Nav Programs submenu icons: **sprout** for Growth, **trophy** for Authority (Lucide; stamped sitewide).
- Programs submenu refined (desktop + mobile): dropped the "Recommended Path" featured card; the two
  programs now show as side-by-side themed cards — **Growth in lime, Authority in the Twilight textured
  purple** (`.mega-grid--programs` + `.mega-item--growth/--authority` in styles.css; the Authority target
  pill changed green → twilight). About/Marketing-Services dropdowns untouched.

## 2026-06-15 — Programs section LOCKED (sans images)
- Both program pages (**Growth**, **Authority**), the **`/programs/` hub**, and the **nav submenu**
  are locked pending real images — treat the build/wireframe/content as final unless the owner reopens it.
- Ran a sitewide consistency pass on every program mention (homepage "Two Paths" section, hub cards,
  nav mega, footer, homepage FAQ + schema, service-page footer link lists). All consistent: naming
  ("Growth Program" / "Authority Program"), order (Growth → Authority), tier framing (Growth =
  6-figure / under $1M / foundation-and-get-found; Authority = 7-figure / over $1M / dominate), and
  no-pricing.
- **Label convention (locked):** compact pill/badge labels use the **digit** form ("For 6-Figure
  Companies"); running prose uses the **spelled** form ("six-figure"). Standardized the hub badge (the
  lone "Six-Figure" outlier) to digit so it matches the homepage badges + nav pills — also avoids the
  spelled form wrapping in the narrow nav pills.
- **Only remaining program to-do:** drop real images into the hero/Why-Us placeholders on the program pages.

## 2026-06-15 — Nav submenu overhaul (tightened all four dropdowns)
- **About:** removed the founder/right-rail card; the dropdown is now a compact single-column
  `.mega-panel--narrow` (380px) — About / Meet The Team / **Experiences & Testimonials**. The
  Experiences item is themed in the Twilight textured purple (`.mega-item--twilight`) with a
  glowing gold star icon, and links to `/resources/experiences-reviews/`.
- **Marketing Services & Industries:** the styled promo headline ("Most Companies Don't Need
  Another Vendor." / "We Only Work In The Green Industry.") is no longer an `<h4>` — moved to a
  `<div class="mega-fc-title">` that inherits the exact former `h4` look (Rethink Sans italic 800).
  This was an **SEO fix** — nav promo copy was polluting the page heading hierarchy. The Marketing
  Services body copy was rewritten to the "one connected system… run by a single team that owns the
  result" framing.
- **Resources — full rebuild:** the featured card is now a Twilight-textured, clickable testimonials
  card (glowing gold 5-star row, "Client Experiences" label, links to `/resources/experiences-reviews/`
  — same target as the About item, anticipating a page full of testimonial videos/screenshots). The
  six items are reorganized into two columns: **Mow Money, Mow Problems** (the Podcast → on-site page
  that will show off the show + let people apply as a guest · YouTube channel ↗ · the Book → Amazon ↗)
  and **Learn & Connect** (Green Industry Insights/Blog · Private Facebook Group ↗ "Service Area
  Experts" · Contact Us). External links open in a new tab (`target="_blank" rel="noopener"`).
- **Decision (flag for Matt):** the "Mow Money, Mow Problems" **Book** links straight to the **Amazon**
  product page (new tab) rather than a dedicated on-site page — simplest path, and Amazon already
  converts. Trivial to swap to a dedicated page later if we want on-site reviews/long-form.
- New nav CSS added to `styles.css`: `.mega-panel--narrow`, `.mega-grid--single`, `.mega-item--twilight`,
  `.mega-featured-card--twilight`, `.mega-fc-stars`, and `.mega-fc-title` (extends the former
  `.mega-featured-card h4` rule so the de-headinged titles keep the identical look). `styles.css?v=137 → 138`.
  Header re-stamped sitewide via `build.py`. Programs / hub / program pages untouched.

## 2026-06-15 — Industry-page framework locked + Landscaping built (1 of 8)
- **Reusable industry-page framework** (built on Landscaping; applies to all 8). Section order:
  hero + above-fold trust strip → answer-first definition + "Updated {Month YYYY}" → "why generic
  marketing fails" + **specialist-vs-generalist comparison table** → **seasonality module** ("we
  market your company one season ahead" — four season cards on the Twilight band; the centerpiece and
  biggest information-gain play) → "what we build" service grid (each card links to its
  `/marketing-services/*` page) → numbered 5-step process → **Proof, Not Promises** (the real homepage
  case row, reused) → "why us" + real credential strip → program-fit cards (Growth / Authority) →
  **visible FAQ accordion (answer-first) + FAQPage schema** → Twilight `svc-cta`.
- **Built for SEO + GEO + EEAT** (from fresh 2026 research + a Lawnline industry-page teardown): one
  keyword-bearing H1, question/claim H2s, answer-first ~40–75-word section openers, a comparison table
  + numbered list (high AI-citation formats), "information gain" only a specialist could write (the
  seasonality math + the three-businesses model: design qualifies → installs earn → maintenance sustains),
  a `@graph` JSON-LD block (Organization + Service + WebPage + BreadcrumbList + FAQPage), a visible
  freshness date, and internal links to every service page + both programs + a sibling industry.
  **Lawnline's industry pages carry NO FAQ and almost no seasonality depth — that gap is our edge.**
- **No invented facts:** proof = the three real homepage clients (all landscaping — Rock Solid,
  Precision, From The Ground Up); credentials = the real homepage/footer signals (NALP, Google Partner,
  100+ companies, 97%+ retention, since 2022). No pricing; the "cost" FAQ answers intent and routes to
  the free call.
- **CSS:** the framework lives in the Landscaping page's scoped `<style>` as reusable `.ind-*` classes
  (`.ind-sec`, `.ind-band`, `.ind-compare`, `.ind-seasons`, `.ind-svc`, `.ind-steps`, `.ind-cred`,
  `.ind-fit`, `.ind-faq`). For pages 2–8, copy that block per page; extract to a shared `industry.css`
  only if we later want to dedupe. **No global CSS change → no cache-bump** (still `styles.css?v=138`,
  `service-page.css?v=3`). Hand-built pages link both stylesheets and wrap content in `<main id="main">`.
- **Next:** roll the framework to the remaining 7 industry pages (lawn-care, lawn-maintenance,
  outdoor-living, land-clearing, excavation, septic-services, holiday-lighting) — each with its own
  seasonality, service emphasis, comparison rows, proof framing, and FAQ. Owner wants them crushed one
  at a time, not batch-generated.

## 2026-06-16 — Industry-page freshness: honest schema date only
- Removed the visible "Updated {Month}" chip (`.ind-updated`) from industry pages. The freshness signal
  now lives **only** in the page schema's `dateModified`, bumped **only on a real update**.
- **Rejected** auto-stamping the current month via script: that's "fake freshness" Google distrusts (it
  cross-checks the date against actual content change → can be discounted or hurt trust) and it violates
  our **no-invented-facts** rule — a bad look for a marketing agency. Earn freshness by genuinely
  refreshing the page (natural hook: a seasonal content refresh), and bump the schema date then.
- Applied to `/industries/landscaping/` and baked into `industry-page-template.md` (Non-negotiables → Freshness).

## 2026-06-16 — Landscaping page feedback (round 1)
- **Intro section** redesigned as a two-column block (`.ind-split`): image placeholder left; eyebrow +
  H2 ("You're not hard to hire. You're hard to find.") + the answer-first definition right-aligned on the
  right. Replaces the centered single-column intro (and fills the gap left by removing the "updated" chip).
- **Google Partner badge** now uses the real **multicolor Google "G" logo** everywhere on the page (hero
  trust strip + credential strip) — made a non-negotiable in `industry-page-template.md`.
- Trimmed the hero trust strip to 3 badges (removed "97%+ client retention"; it still lives in the
  credential strip below).

## 2026-06-16 — Sitewide service icons + "CRM & Automation" rename + landscaping tweaks
- **Canonical service icons (Lucide), consistent everywhere** — the submenu, service-page CTAs, homepage,
  hub, and industry grids now share one icon per service. New icons per owner: Website Design →
  `monitor-smartphone`, Google Ads → `badge-check`, Meta Ads → `book-user`, CRM & Automation →
  `refresh-ccw`; the rest standardized (Local SEO `search`, GBP `map-pin`, AI Partner `bot`, Reputation
  `star`). Machine source of truth: **`SERVICE_MAP` in `gen_service.py`**; registry in `navigation.md`.
  New Lucide paths pulled verbatim from source.
- **"Automation" → "CRM & Automation"** everywhere (display name only; slug stays
  `/marketing-services/automation/`). Updated `_content.json` (regenerated the page — now leans into CRM
  capture/track + automation follow-up), the submenu, footer, homepage tab, and hub.
- **Landscaping page:** seasonality headline + all "one season ahead" copy → **"ahead of the seasons"**
  (not limiting to a single season; still seasonal). Added an **8th service card — Your AI Partner — as
  the Twilight standout** (`.ind-svc--ai`, bot icon) emphasizing AI search ranking, AI implementation,
  and staying ahead of trends. (The intro two-column / Google-G / trust-strip tweaks from the prior round
  are also live.)

## 2026-06-16 — Landscaping: testimonials added + Why-Us restructured
- **Added a testimonials section** (`.testi-section`) right after "Proof, Not Promises" — three REAL video
  testimonials (Logan's Landscaping, Brothers Outdoor Services, VASH Landscaping; faces + quotes + gold
  stars), reused from the homepage, with a "See more client experiences" link to
  `/resources/experiences-reviews/`. Rationale: the proof row shows numbers; testimonials add the
  voices/faces. Real, attributed — never invented. (Now part of the framework: proof = numbers + voices.)
- **"Why Lawn & Land" restructured** to a two-column block (`.ind-split--flip`): copy left (left-aligned),
  image placeholder right. Removed the credential box (NALP / Google Partner / 100+ / 97% / since 2022) —
  those signals still live in the hero trust strip and the footer.

## 2026-06-16 — Template review pass (SEO tightening + reuse rules)
- Reviewed the landscaping page as the locked template (independent audit + own pass). Verdict: strong
  (~1,700 words, clean structure, full schema, real information-gain). Tightened + future-proofed:
- **On the page:** H1 now leads with the literal keyword ("Landscaping marketing for companies…");
  de-clichéd the testimonials H2 ("Don't Take Our Word For It" → "What landscaping owners say about
  working with us"); added an HTML TEMPLATE/REUSE comment on the proof+testimonials block.
- **Template rules added to `industry-page-template.md`:**
  - **The demand-cycle module is two layouts**, not a locked 4-season grid: (A) 4-season calendar for the
    seasonal trades; (B) demand-mode cards for the less-seasonal trades (septic =
    emergency/routine/real-estate/compliance; excavation + land-clearing = frost/dig-season + permit
    windows). Forcing four seasons on septic would be fluff that undercuts the "we know your business" promise.
  - **Proof/testimonial reuse rule:** every real testimonial/case number is a lawn/landscape client — keep
    the content on every page, but genericize the FRAMING to "green industry" + a bridge line ("the same
    system and team we'd put behind your [trade] business") on septic/land-clearing/excavation/holiday-lighting.
    Honest; never invent same-trade testimonials.
  - H1 must contain the literal "[industry] marketing" phrase; clever hooks stay as kickers, not the H1/money H2s.
- **Launch checklist:** flagged localizing the hero NALP badge (loads from the legacy WordPress domain) into `/assets/`.
- **Open for Matt:** (1) the "Why Lawn & Land" two-col slightly overlaps the hero strip + comparison table +
  FAQ on the "we only do green industry" message — option to evolve its copy to add team/years instead of
  restating focus; (2) confirm the demand-mode seasonality approach for septic / excavation / land-clearing.

## 2026-06-16 — Removed the standalone "Why Lawn & Land" section
- Eliminated the two-column "Why Lawn & Land" section from the landscaping page (and the framework). Its
  whole message ("we only work in the green industry") was already made — better — by the hero trust badge,
  the FAQ ("Do you only work with landscaping companies?"), and especially the **comparison table, which IS
  the "why us"** (specialist vs. generalist, with information gain). Cutting it removes a redundant beat with
  zero loss of argument and tightens the flow to proof → testimonials → program-fit → FAQ → CTA. The page is
  now 10 sections. Updated `industry-page-template.md`.

## 2026-06-16 — Third-party SEO audit: adopted the one held point (answer-first opener)
- The external auditor conceded our pushbacks (homeowner vocabulary was overcalled; the brand H2s and the
  "design-build" title scope stand; **no Review/AggregateRating on first-party testimonials** — self-serving,
  no rich result + manual-action risk). Its one fair remaining point: more **answer-first openers** for GEO.
- **Adopted:** rewrote the Process section opener to name the five steps up front (an extractable answer to
  "How we grow a landscaping company") while keeping the "no 50-item checklist, no guesswork" voice. The
  other section openers are already extractable, so no further changes.
- **Note for when About / Meet-the-Team are built:** industry pages should link to a **named human/agency
  authority** (Google "Authoritativeness"), not a generic shell — that's where deep EEAT lives, off the money page.

## 2026-06-16 — Built Lawn Care (page 2); extracted shared `industry.css`; acted on a 2nd template audit
- **Lawn Care page built** (`/industries/lawn-care/`) off the locked template — reframed for the recurring
  treatment-program business (route density + retention, not high-ticket installs): 4-season demand cycle
  (winter prepay/renewals → spring rush → summer fulfill + book fall → fall aerate/overseed/re-sign),
  lawn-care comparison rows + FAQ (retention + route-density Qs), proof/testimonials framed "lawn and landscape."
- **CSS extracted to a shared file** — RESOLVES the open sub-question below. The `.ind-*` framework was
  duplicated verbatim across landscaping + lawn-care; pulled it into **`/assets/css/industry.css`** (`?v=1`)
  and replaced each page's inline block with a one-line pointer comment + a `<link>`. Did this now (after
  page 2, before page 3) so the duplication never reaches three pages. No global CSS changed.
- **Second third-party audit of the template** (shared FYI, "change only if it changes things for you"):
  graded the structure A−, flagged process gaps, not content. Acted on the substantive ones in
  `industry-page-template.md`: (1) demand-mode trades CANNOT be written from the seed — research is mandatory;
  (2) lawn-care vs. lawn-maintenance keyword split must be decided BEFORE building lawn-maintenance (anti-
  cannibalization); (3) added an **answer-first verification step** to the build checklist (read only first
  sentences top-to-bottom); (4) the CSS extraction above; (5) a recommended build order (seasonal layout-A
  pages first, demand-mode layout-B last); plus a Lawnline re-verify caveat and a stronger septic bridge
  (bridge on the transferable local-demand mechanism, not client similarity).

## 2026-06-17 — Resolved the lawn-care/lawn-maintenance axis; re-pointed Lawn Care to recurring revenue
- A second review of the live Lawn Care page (third-party agent) confirmed the keyword-collision risk both
  template audits flagged: the page led on **"fill the route" / route density**, which is really the
  *maintenance* (mowing) page's mental model. Two pages leading on "the route" would cannibalize each other.
- **Owner decision:** Lawn Care's spine = **recurring revenue / program** (renewals, retention, LTV);
  Lawn Maintenance's spine = **route / mowing operations**. Locked in `industry-page-template.md`.
- **Re-pointed the Lawn Care page accordingly:** H1 "…fill the route" → "…**grow recurring revenue**"; hero,
  intro definition, why-generic + seasons ledes, services H2, program-fit, Growth card, and CTA all moved to
  the recurring-program story. Route density kept as a *supporting* beat (one comparison row, the Meta Ads
  geo-targeting tactic, its dedicated FAQ). Also tightened the two hook-first openers to **answer-first** (the
  new build-checklist step in action) and bumped `dateModified` to 2026-06-17 (honest — real content edit).
- The review's other points: schema verified clean from source (entities swapped, honest date — no action);
  "homeowner" vocabulary left as-is (owner-focused ratio is fine, same call as landscaping); the universal
  **footer tagline** was narrowing to "landscaping companies" on every page — broadened to "your business."
- **Reminder for the lawn-maintenance build:** route/density is ITS headline; do not reuse Lawn Care's spine.

## 2026-06-17 — Built Lawn Maintenance + Outdoor Living (industry pages 3 & 4)
- Built both off the locked template after a real research pass per page (parallel research agents +
  Lawnline re-verify, per the playbook). Both verified on preview (valid `@graph`, one H1, no console errors)
  and pushed; staging deploys automatically.
- **Lawn Maintenance** (`/industries/lawn-maintenance/`) — the property's upkeep business (mowing, cleanups,
  bed maintenance). **Route density is the headline** — the "windshield time" margin spine lawn-care ceded,
  so the two pages don't compete. 4-season cycle: winter lock routes/prepay → spring sign-up rush → summer
  tighten + pre-sell fall → fall cleanups/leaf + snow upsell + re-sign. FAQ explicitly disambiguates
  lawn-care vs lawn-maintenance and links the sibling, so Google reads them as distinct.
- **Outdoor Living** (`/industries/outdoor-living/`) — high-ticket design-build/hardscape. Spine = the
  **portfolio (the product) + the long, financed sale**. Demand cycle is **inverted** vs. the recurring
  trades: winter is prime SELL/design season (fill the spring build calendar); summer is for building +
  harvesting reviews; fall re-opens selling + pitches financing. Keyword-differentiated from Landscaping
  (hardscape/structures/financing here; softscape/green/install + maintenance there).
- **Lawnline re-verify findings:** they now have BOTH a lawn-maintenance page (already mentions route
  density/retention) and a hardscape/outdoor-living page — but **neither has an FAQ or a real demand cycle**,
  and the hardscape page never mentions financing. So our edge on both is depth: visible FAQ + quarter-by-
  quarter demand cycle (+ financing on outdoor living). Benchmark snapshot updated.
- **Remaining: 4** — holiday-lighting (last seasonal/layout-A), then the demand-mode trio
  septic-services / land-clearing / excavation (layout-B, each needs a fuller research pass).

## 2026-06-17 — Built the final 4 industry pages; all 8 complete; demand-mode pattern proven
- Built **Holiday Lighting, Land Clearing, Excavation, Septic Services** off the locked template (researched
  per page; Lawnline re-verified). All 8 canonical industry pages are now developed. Each verified on preview
  (valid `@graph`, one H1, no console errors), pushed; staging deploys automatically.
- **The big one for this batch: NO four-season calendar on these trades.** Three are project/demand-driven,
  one is hyper-seasonal-but-compressed. So the demand-cycle module flexes (the `.ind-seasons` grid takes any
  4 cards): **holiday-lighting** = phase cycle (pre-sell → booking → install → takedown/re-book; "ahead of
  the season" still fits); **land-clearing** = pipeline / ground-access / burn windows / fire-mitigation;
  **excavation** = pipeline / residential-vs-commercial two-buyer split / dig conditions / 811+permits;
  **septic** = emergency / routine / real-estate / compliance. Each `.hl` headline reflects the REAL cycle
  ("how septic demand actually shows up", "how clearing work actually comes in", etc.), not "ahead of the seasons".
- **Cannibalization discipline held:** clearing↔excavation carry mirrored disambiguation FAQs (clearing =
  remove what's on the land; excavation = shape the earth; clearing first) and cross-link; excavation↔septic
  cross-link so septic install/compliance stays on the septic page.
- **Off-trade proof reuse:** all four use real lawn/landscape proof genericized to "green industry" + a
  per-trade bridge. Septic is the hardest stretch, so it bridges on the **transferable local-demand mechanism**
  (found-first + reviews + follow-up), not client similarity, per the §7 septic note.
- **NEW BRAND RULE applied: no em dashes in customer-facing copy.** Came in via the owner's build prompt; all
  four new pages were authored em-dash-free (commas/periods/restructure). The earlier four pages (landscaping,
  lawn-care, lawn-maintenance, outdoor-living) and the shared nav/footer still contain em dashes. **Open
  question for the owner:** do a careful sitewide em-dash pass for consistency, or leave the earlier pages as
  is? (A blind find/replace is unsafe; em dashes sometimes need a period vs comma vs restructure.)
- Added the no-em-dash rule to `industry-page-template.md` non-negotiables; updated the build-order note (all
  8 done), `page-registry.md`, `build-status.md`, `CLAUDE.md`.

## 2026-06-17 — Repositioned the septic page from "services" to "installers" (owner's real prospect)
- **Decision (owner):** the real prospect in this vertical is the **septic installer**, not the pump-and-service
  company. Pure installers (install + drainfield replacement, no pumping/emergency), even mix of replacement +
  new construction. So the page was **repositioned**, not tweaked.
- **Key insight:** a septic *installer* is a high-ticket, project-based, permit-gated business — structurally
  much closer to **Excavation** than to a pumping company. It's won on licensing, permit-fluency, system-design
  capability, and proof, not on emergency speed-to-answer.
- **What changed:** the whole spine. H1 "get found first when an emergency hits" → **"win more install and
  drainfield jobs."** Demand modes flipped from service (emergency / routine / realtor / compliance) to install
  (**failed-system replacement / new construction / real-estate upgrade / compliance & permits**). `.hl` headline
  "how septic demand actually shows up" → **"how install work actually comes in."** Comparison rows, services,
  FAQ, and the proof bridge all re-pointed to the high-ticket, two-buyer (failed-system homeowner + builder/GC)
  install business. Softened the LSA claim (LSA leans service/repair; install eligibility is a launch-verify item).
- **Slug renamed** `/industries/septic-services/` → **`/industries/septic-installation/`** (pre-launch, so clean;
  no redirect needed). Nav label "Septic Services" → **"Septic Installation"**, mega-menu microcopy updated, and
  every reference re-pointed: `_header.html`, `_footer.html`, homepage industry card, `sitemap.xml`, the
  excavation cross-link, and all docs. `build.py` restamped; verified zero orphan `septic-services` links.
- **The other 7 pages and the canonical-8 list are unchanged** — this is a refinement of one industry, not a
  re-scope. Excavation↔septic cross-links still hold (excavation defers septic installs to this page).
- **Audit follow-up (same day):** a third-party review flagged the predicted risk — repositioning to "installer"
  made septic structurally close to **Excavation** (shared two-buyer split, near-identical "Runs two engines" +
  high-ticket comparison rows, a duplicate process step). Core keywords don't collide, but the *section content*
  did, dampening both pages' topical distinctiveness. **Fix:** re-pointed septic's spine to **the licensed
  septic-system specialty** (license, permits/perc tests, conventional/mound/ATU/engineered systems, passing
  inspection — the moat an excavator cannot claim); rewrote the comparison table so it shares **zero** row labels
  with Excavation; de-duped process step 4; demoted the two-buyer split to a supporting beat (kept in the demand
  cards, removed as a comparison row). Verified zero shared comparison-row labels between the two pages.
- **Full-site septic sweep (per owner):** swept the whole site for septic references and aligned them to the
  installer framing — the Industries-hub list + meta/OG ("septic" → "septic installation"), the four reuse-rule
  HTML comments (old slug → new), the mega-menu microcopy. Confirmed point-of-sale septic is claimed only here.
- **Explicit decision: installer-only.** We have **consciously vacated the septic-pumping/service keyword space**
  (real volume, but not the owner's prospect). A separate service page remains a future option and would NOT
  cannibalize the installer page (different spine) — ironic, since the old pump-service page was *further* from
  Excavation than the installer page is. 301 redirect from the old slug added to the launch checklist.

## 2026-06-17 — Completed the sitewide em-dash pass (RESOLVES the open question above)
- **Decision (owner): yes, full sitewide pass.** Done. Removed every em dash from customer-facing copy across
  the whole site, **672 → 0**. The rationale that won it: for a *marketing agency's own* site, em-dash overuse
  is the single most recognizable "AI-written" tell, so it's a real credibility issue; and the half-done state
  (4 clean pages, rest not) was the worst version.
- **Done by hand, judged per instance** (not a blind find/replace, which would create comma splices and run-ons):
  parentheticals with internal commas → parentheses; list lead-ins → colons; tag-ons / causal "so" / expansions →
  commas; strong contrasts and punchlines → periods. **En dashes in ranges preserved** (Sept–Nov, 3–5 yrs, $60K–$80K).
- **Fixed at the SOURCE so it stays clean going forward:** `_header.html` + `_footer.html` (8 em dashes stamped
  into all 32 pages — the biggest single win, ~38% of the total), `_content.json` (regenerated the 7 service
  pages), the `gen_service.py` template (the "what's included" subhead + the FAQ placeholder), and
  `PAGE_TEMPLATE.html`. So future regenerated/stamped pages are born em-dash-free.
- **Verified:** 0 em dashes across all HTML and all build sources; `build.py --check` passes; `_content.json`
  valid; homepage + a regenerated service page render with no console errors. (Docs/`.md`/code-comments are not
  customer-facing and were left as-is, except where edited.)

## 2026-06-17 — Killed heading "widows" (a lone word on a heading's last line) sitewide
- **Problem (owner-reported):** the two-line intro hooks on the industry pages (e.g. "Filling the
  pipeline is the hard / part.") were stranding a single word on the last line — "a bad look." Seen on
  desktop *and* sometimes mobile.
- **Root cause:** `text-wrap: balance` (already global on headings) evens line *widths*, not word
  *counts*. With a hard `<br>` or a long compound word it can legitimately leave one word alone. So
  `balance` can never *guarantee* against it — wrong tool for the guarantee. Confirmed by measuring real
  render boxes in the browser, not eyeballing.
- **Fix — two layers:**
  1. **Widow-guard in `main.js`** (`?v=54`): on load, for every heading (`h1–h4`) outside nav/footer,
     it glues the last two words of each `<br>`-delimited segment with a non-breaking space, so the last
     line always carries 2+ words **at any viewport width and on future copy**. Skips the animated hero
     H1 and any heading already hand-glued. Inserts only ` ` (never reorders/removes), so it cannot
     break layout — worst case it does nothing. Handles words inside `.hl` / gradient spans correctly.
  2. **Hard-glued the 8 industry intro-hook H2s in the HTML** too (belt-and-suspenders — those stay
     fixed even with JS disabled, since they're the most visible headings).
- **Verified** by measuring rendered line boxes (Range API) across 5 structurally-distinct page types
  (industry, homepage, Growth, Authority, service template) at **1280 and 375** — **zero** single-word
  last lines anywhere, including the multi-segment `<br>` headers and span-wrapped phrases.
- **Why JS, not pure CSS or hand-gluing every heading:** CSS can't guarantee it; hand-gluing every
  heading is unmaintainable and breaks on new copy. The guard is automatic, future-proof, and degrades
  gracefully.

## 2026-06-17 — Comparison table goes to stacked cards on phones (no sideways scroll)
- **Problem (owner-reported):** the "green-industry specialist vs. generalist agency" table
  (`.ind-compare`, shared on all 8 industry pages) looked great on desktop but on mobile it was a
  horizontally-scrolling table — the row labels (left) and the whole "generalist" column (right) sat
  off-screen, and nothing signals there's more to swipe to. With most traffic on mobile, half the
  section was effectively invisible.
- **Fix (CSS only, `industry.css?v=2`, `@media max-width:680px`):** the `<table>` reflows into
  **stacked cards**, one per comparison row. Each card = the criterion as an italic heading, then the
  **Lawn & Land** answer (green eyebrow + green left-accent + faint green tint = the "winner") and the
  **A generalist agency** answer (muted) below it. Column headers (`<thead>`) hide on mobile; each
  cell gets its own label via CSS `::before` so the side is always clear. No markup change — pure CSS,
  so it covers all 8 pages at once and is keyed only on the existing `.row-label` / `.col-us` /
  `.col-them` classes.
- **Desktop is byte-for-byte unchanged** (everything is inside the mobile media query; verified the
  table still renders as `display:table` with visible `<thead>`, 560px min-width, no pseudo-labels).
- **Verified** on the preview at 390px (land-clearing + septic-installation): zero page-level
  horizontal scroll, cards render with correct labels and the green keyword highlights intact; and at
  1280px the original table is untouched.

## 2026-06-17 — Built the About page (real content, owner-led, SEO/E-E-A-T)
- **Built from the owner's REAL content, no invented facts.** Pulled the live legacy pages
  (`/about/`, `/is-marketing-right-for-us/`, `/reviews/`) via raw-HTML extraction (WebFetch truncated
  on the heavy Avada markup; curl + a tag-stripper got the real copy). Preserved the real mission
  ("your personal team", "not just another statistic") and the real owner bio (Matt Foreman; prior
  agency Shoot To Thrill Media, 2016; deliberate pivot to the green industry) nearly verbatim,
  emoji-free per brand.
- **Structure** (existing components, modeled on the Growth page): hero (team-hero bg, keyword H1/H2)
  → mission → Meet the Owner (real family photo `assets/images/matt-foreman.jpg`, 1200x1800, portrait)
  → why-specialization (Twilight band, 3 cards) → values/transparency (3 cards, incl. the "we publish
  our worst review" ethos borrowed from Reviews) → condensed good-fit / not-a-fit framework → stat band
  → Twilight CTA.
- **Schema:** `@graph` = Organization + Person (Matt, founder) + AboutPage + BreadcrumbList (production
  domain, staging canonical). Strong E-E-A-T.
- **Bonus-page verdict (owner asked):** the good-fit/not-a-fit framework → folded into About (high trust
  + SEO). The Reviews testimonials + "Lyle / worst review" story → stay a dedicated Reviews page; About
  only borrows the transparency ethos.
- **Team decision (owner delegated):** consolidate, don't split. One strong owner-led About page beats a
  thin standalone "Meet the Team" page for SEO/E-E-A-T; the owner section is structured to add real team
  members later. **PENDING OWNER OK:** retire `/resources/meet-the-team/` from nav submenu + footer
  (fold into About) + launch redirect. Not changed yet.
- **Stats reused (VERIFY before launch):** 100+ companies, 97% retention (owner chose 97% over the
  legacy 95-96%), since 2022, NALP membership. All already published elsewhere on the new site.
- **Verified** on preview at 1280 + 390: clean H1->H2->H3 outline, no horizontal scroll, fit + owner
  sections stack on mobile, family photo well-framed, 0 em dashes, 0 emoji, widow-guard handles the
  hero `<br>`, `build.py --check` in sync.

## 2026-06-17 — Meet the Team consolidated into About; About polish
- **Team consolidation EXECUTED** (owner delegated the call, then supplied the source). Extracted the
  real team from the legacy `/our-team/` page (raw-HTML parse: each photo's `<img>` immediately precedes
  that person's name heading, so the mapping is structural, not guessed). 10 members (Matt Foreman is
  the separate Meet-the-Owner section, so excluded from the grid): Leadership (Sandi Jaramillo, Juan
  Calderon, Honey Zamora, Damien Friedenthal) + Green Marketing Specialists (Anne Venus, Daisy Llorico,
  Jez Pangan, Matt Jones, Nadia Louw, Patricia Caretiro). Headshots downloaded + optimized to
  `assets/images/team/<slug>.jpg` (520x520, ~50-75KB each).
- Added a **Meet the Team** grid to About (`#team`, square cards, Leadership 4-col / Specialists 3-col,
  2-col on mobile). Standalone `/resources/meet-the-team/` shell **deleted**, removed from `sitemap.xml`,
  and nav + footer links updated. **Final state (owner decision, same day): the "Meet The Team" nav
  submenu item and footer link were SUNSET entirely** — not repointed. The team lives on only as the
  About `#team` section (reachable via the About nav item); there is no standalone team label anywhere
  in the chrome. Verified 0 `/about/#team` links and 0 "Meet the Team" nav/footer text sitewide. Launch
  301 `/resources/meet-the-team/` → `/about/#team` noted on the checklist.
- **Retention stat → `97%+`** (owner confirmed: actually upper-97 to low-98, comfortable saying over 97).
- **Owner family photo mobile reframe:** was `aspect 4/3 @ object-position 26%` (too much sky above his
  head); now `4/5 @ 42%` so the family fills the frame. Desktop unchanged (`4/5 @ 30%`, owner liked it).
- **CSS gotcha fixed:** `.team-card img` needed `height:auto` — the `height="520"` HTML attribute was
  overriding `aspect-ratio:1/1` and rendering tall cards. (The owner photo already had `height:auto`.)

## 2026-06-17 — About page: external SEO audit response (EEAT anchor)
- Auditor graded the page on EEAT + conversion (correct lens for an About page) and compared it to
  Lawnline. Net: we win on trust/team-depth/human-founder; close gaps were technical + scope.
- **Schema was already present** (auditor couldn't see it on a rendered fetch and assumed it might be
  missing). Confirmed Organization + Person + AboutPage + BreadcrumbList. **Added** `memberOf` (NALP) and
  `employee` (the 10 team members as Person entities) to the Organization node.
- **Scope language widened** — it said "built exclusively for lawn care and landscaping companies" in
  meta/OG/schema/hero, too narrow for an 8-trade site. Now leads with "green-industry marketing agency"
  and names the breadth (lawn & landscape -> land clearing, excavation, septic). Earns the head term
  "green-industry marketing agency" once, visibly (hero).
- **Third-party reviews:** added an outbound "Read our reviews on Google" link (owner-supplied
  share.google link) in the stat band — stronger EEAT than on-page testimonials.
- **Roster / the Jez photo bug:** owner confirmed all names + titles accurate. BUT the legacy
  `/our-team/` page has a FIRED employee's old photo (Ali Mustafa, "Facebook Ads Specialist") sitting in
  **Jez Pangan's** card — proven by the image's `alt` text. My position-based scrape inherited it.
  Replaced with a clean **"JP" initials placeholder** (`.team-ph`); **need Jez's real headshot from the
  owner.** (The owner's live WP site still shows Ali's face under Jez's name — flagged to fix there too.)
- **Declined (owner):** a scale dollar figure (they don't have Lawnline-size numbers and won't fabricate)
  and a hard tenure reframe (the bio already honestly carries "Shoot To Thrill, 2016" + "green industry
  since 2022"; being the smaller, more-honest option is the brand edge, so no "10+ years" inflation).
- **Parked (post-launch):** per-person team bios / deeper team entities; A/B-watch the "we lean on AI"
  line for the more traditional buyer.

## 2026-06-19 — Built the Experiences & Reviews page (social-proof EEAT anchor)
- **Purpose:** the trust/social-proof hub, built to rank + feed AI/crawlers + convert. Owner wants it to
  grow into a big "wall" of testimonial videos + review screenshots ("wow, look at all these").
- **Populated now with REAL existing content** (pulled from the homepage, no inventing): 6 video
  testimonials (Peter Logan/Logan's, Phillip Sirmon/P&C, Zach Franz/Rock Solid, Rick McCarty/Brothers,
  Prentiss Holt/VASH, Nate Moses/Precision) + 3 case studies (Rock Solid $700K→$1.3M, Precision 200→600
  calls/mo, From The Ground Up $1.8M→$3.2M) + the "they stay" retention line + the worst-review
  transparency play.
- **Built to grow:** reuses the homepage `.testi-card` / `.testi-video-wrap` components (so the
  click-to-play already works via existing `main.js`) and the `.proof-cases-grid`. The video grid
  auto-flows, with an HTML comment template for adding a card. Screenshot wall + more videos get added
  as the owner sends the Google Drive content.
- **Reviews-microsite cross-link strategy (owner):** owner bought `lawnandlandmarketingreviews.com` (an
  exact-match "[company] reviews" domain) to rank for "[company] reviews" queries. This page links OUT
  to it (dofollow, `See all our reviews`) + to the Google Business reviews; the microsite should link
  BACK to the main site (owner's side). Cross-link confirmed live (microsite returns 200).
- **Schema:** `CollectionPage` + `BreadcrumbList`. **Deliberately NO `Review` / `AggregateRating`** on
  first-party testimonials (established rule; Google won't show self-serving stars and it risks a
  penalty). VideoObject held until real per-video metadata (upload dates) exists.
- Verified on preview: click-to-play spawns the right YouTube iframe, 6/6 thumbnails load, mobile +
  desktop clean, no orphans/scroll, em-dash + emoji free, `build.py --check` in sync.

## 2026-06-19 — Experiences page revisions (owner feedback)
- **Removed the "worst review" transparency section** — owner reversed course, does not want that route.
  (Was a strong EEAT signal per the auditor, but owner's call; gone from the page.)
- **Removed the TOP Google-reviews link** (intro). Owner: videos are the highest-value proof, Google is
  the lowest, and he doesn't want to funnel people to Google from the top. **One** Google link remains,
  in the bottom cross-link band (owner approved keeping that one).
- **Added a 5-star signal** at the top of the "Our clients say it best" section (gold stars + "Five-star
  rated by green-industry owners across the country" — qualitative, no fabricated numeric average).
- **Added an 11-screenshot wall** (masonry `.shot-wall`, real screenshots pulled from the legacy
  `/reviews/`: Google reviews, client texts, social posts) in `assets/images/reviews/`. Scales as more
  are added (HTML comment template included).
- **VIDEO HOSTING — open decision (owner):** owner's Drive folder has 16 raw .mp4 testimonials (24-84MB
  each, growing). Raw video can't live in the static repo, and Drive embeds get throttled on a public
  page. Recommended **YouTube** (matches the existing 6, free, scales, no quota, best for SEO). Awaiting
  owner's choice before wiring more videos in.

## 2026-06-19 — Built the vertical video testimonial wall (22 Shorts)
- **Video hosting RESOLVED:** owner chose YouTube. Team uploaded 22 short-form (9:16) testimonial
  **Shorts** across 8 clients (Zach/Rock Solid, Tami/Artistic Landscape Features, Rick/Brothers Outdoor,
  Phillip/P&C, Peter/Logan's, Nate/Precision, David/Creative Edge, Tim/Hill) as Public, and dropped the
  embed links in a Google Sheet. Built a dense **vertical wall** (`.vt-grid` / `.vtcard`, 5-up desktop /
  2-up mobile), **interleaving clients** so the top rows show variety. Reused the existing
  `.testi-video-wrap` click-to-play JS (just overrode the aspect to 9/16 via `.short-vid`).
- **Replaced the 6 older landscape testimonial cards** on this page (went all-vertical for consistency +
  density; the landscape 6 still live on the homepage). Can re-add them as a "featured" row if the owner
  wants.
- **Thumbnails:** YouTube serves a clean 9:16 vertical poster at `i.ytimg.com/vi/<id>/oardefault.jpg`
  (confirmed for all 22). Hotlinked, no hosting needed.
- **VideoObject schema** for all 22 (name = the YouTube title, description = per-clip summary,
  thumbnailUrl, embedUrl, contentUrl, uploadDate=2026-06-19 approx). This is the video-rich-result /
  AI-crawl signal.
- **Flag for owner:** Tami's YouTube *descriptions* say "Building Growth Landscaping" but her business
  (and the video titles) say "Artistic Landscape Features" — the descriptions on those 3 videos should
  be corrected on YouTube. The page uses the correct "Artistic Landscape Features."

## Open Decisions To Track Later
- **PENDING OWNER:** confirm `lawnandlandmarketingreviews.com` links back to the main site (reviews
  cross-link strategy); review screenshots still welcome to grow the screenshot wall.
- **PENDING OWNER:** real headshots for **all 10 team members** (About `#team`). All cards are now
  **initials placeholders** (`.team-ph`) by owner request — the scraped `/our-team/` photos were
  unreliable (the Jez slot alone served a fired employee's photo, then a third person), so we cleared
  them all; owner is sending fresh photos. Names + titles are confirmed accurate (and in the schema).
- **Industry-page content + template** — RESOLVED 2026-06-15: the reusable framework is built and
  proven on `/industries/landscaping/` (see the dated entry above). Remaining work is rolling it to the
  other 6 industries, one at a time. Sub-question RESOLVED 2026-06-16: the `.ind-*` CSS was extracted to a
  shared `/assets/css/industry.css` after page 2 (see the dated entry above).
- **About / Contact / Resources** design direction.
- **Service-page finishing inputs** — real FAQ answers (→ add `FAQPage` schema), verified conviction
  stats, real images.
- Whether retired routes get hosting-layer redirects at launch vs. simply staying out of internal linking.


## 2026-06-21
- **Reintroduced the `/case-studies/` silo** (previously killed) to host migrated case studies, recorded here per the routing rule that intentional reintroductions need a decision. Page 1: `/case-studies/precision/`. No index page at `/case-studies/` itself yet, so its breadcrumb crumb is a non-link label.
- **Migrated the Precision Landscape Management case study** from the legacy WordPress `/precision-case-study/` onto the new design system: preserved the substance (135 to 536 calls / +297%, 98 to 360 first-time callers, 295 to 1,407 impressions, 2 to 6 sales team, 15%+ conversion, 10x+ ROI, the seven service sections, Nate's video, the sticky table of contents, the narrative arc) and rebuilt the shell.
- **Corrected a published math error:** the old page claimed impressions "grown over 475%"; 295 to 1,407 is +377% (nearly 4.8x). Standardized on +297% for calls.
- **Modernized:** AdWords to Google Ads; removed the FREE-Google-Verified-Management bar, the Ultimate Checklist lead magnet, the Service Area Expert program framing, and the "lead acceleration session" CTA. Every CTA routes to `/get-started/book-strategy-call/`.
- **Reframed the Google-Guaranteed "quote"** as plain explanatory copy rather than a statement attributed to Google (it was not a verifiable Google quote). Flagged for owner confirmation.
- **Media:** Nate's testimonial uses the YouTube click-to-play pattern (vertical Short `q--6TsFlnLI`). Headline numbers are native data viz; dashboard screenshots are clearly-labeled placeholders pending real captures (we did not embed the dated low-res WordPress screenshots).
- **Cross-linked** from the experiences hub and the lawn-care / lawn-maintenance / landscaping / outdoor-living proof cards. **Launch 301:** `/precision-case-study/` to `/case-studies/precision/`.
- (Same day, earlier) Removed the `/resources/` hub page and `/resources/private-facebook-group/` shell; the Resources nav top-level is now a non-link label and the footer Private Facebook Group link points to the external group.


## 2026-06-21 (continued) — case study hybrid template
- **Established the reusable case-study template** (`case-study-template.md`): hero -> "At a Glance" conversion unit -> sticky-ToC deep dive. Precision is page 1; clone it for future case studies.
- **Added the "At a Glance" / "The short version" block** under the hero (situation-to-outcome narrative + the single stat band + a spend-anchored ROI line + CTA + "full breakdown" hand-off), so the page serves both the 60-second skimmer and the deep reader. Moved the stat band into this block (one instance, no duplicate).
- **Swapped the testimonial to the full-length 16:9 Nate Moses video** (`ajusL5iAs0Q`, "Our Phone Doesn't Stop Ringing", from the homepage) via click-to-play, replacing the vertical short. Caption uses his real approved quote plus the precise 135 to 536 figure. ToC + heading now read "the owner" (template-generic); the caption names the person.
- **Dropped in the real proof screenshots**, pulled from the legacy WordPress case study and re-hosted under `assets/images/precision/` (website, LSA dashboard, GBP, Featured Snippet, CRM lead, Missed Call Text Back, Google reviews) with descriptive alt text. The LSA screenshot corroborates the "$250/week, 9 leads" copy. Per owner instruction: re-host on our site, do not hotlink WordPress; leave a slot blank if an image is unavailable (none were).
- **ROI line carries no dollar figure** pending an owner-confirmed spend (per directive: drop the placeholder rather than guess). The 10x ROI multiple + Nate's approval to republish remain owner actions before this indexes. VideoObject `uploadDate` set to 2026-06-19 to match the testimonial set (owner can correct to the true date).


## 2026-06-21 (update) — Precision revenue trajectory + 23x ROI + visual polish
- **Revenue trajectory added** (Results section): native ascending bar chart, $4.4M (joined) to $7.8M (year 1) to $11.2M (year 2), with an explicit **honest-attribution note** - these are company-wide results, Precision is a strong operator in its own right, and our marketing was one of the **core drivers** and the marketing partner, not the sole cause (owner's framing: make the role known without over-claiming the revenue).
- **ROI updated 10x to 23x** everywhere on the page (stat band, At-a-Glance ROI line, secondary stat, OG description, conclusion); 23x is owner-provided.
- **"The short version" block** now sits on the Twilight textured + dot-grid band (matches the homepage stats bar / `.ind-band`).
- **GBP then-to-now comparison** (4.5 stars / 43 reviews to 4.8 stars / 320+ reviews); the current-state GBP screenshot is still pending (it was shared inline, not as a hostable file).


## 2026-06-21 (update) — Rock Solid Landscape case study built
- **Built `/case-studies/rock-solid/`** into the case-study framework (cloned from the Precision reference). Rock Solid Landscape, Wauseon, OH, owner Zach Franz. An **organic/SEO-led** story (no paid ads), distinct from Precision's paid-led one.
- **Fixed the framework-flagged issues:** the old page's generic title ("Digital Marketing Blueprint for 7-Figure Businesses") + Precision's meta description -> client-specific; verified the math (+378% impressions, +466% clicks are correct); removed WordPress cruft, the FREE-Google promo bar, and the banned Gemini-generated image.
- **Revenue framing reconciled** to Zach's on-record "about $700K to over $1M" (matches the embedded video, titled "$700K to Over $1M"), with the mandatory attribution-honesty note. **Flagged for owner:** the existing site proof cards say "$1.3M" for Rock Solid; the canonical figure needs an owner decision. We used the conservative, video-matching "over $1M" and did NOT change the proof cards.
- **AI-search claim reframed** for defensibility: kept the real, Rock-Solid-specific proof (a ChatGPT screenshot naming them the top recommendation for Wauseon, OH) but dropped the "we dominate AI search" overclaim and the unprovable "thanks to our AI-EO" causation, and added a point-in-time caveat (AI answers change).
- **New reusable element:** a **month-by-month results table** (`.cs-table`) showing the GBP ramp (Months 1/3/6). Real screenshots (#1 Google ranking, ChatGPT, GBP) re-hosted under `assets/images/rock-solid/`; the two source matplotlib charts rendered natively instead.
- Cross-linked from the experiences hub + 4 industry proof cards; sitemap + 301 added. No ROI multiple (none available; the revenue trajectory is the return).


## 2026-06-21 (update) — Client Results roster page + case-study interlinking
- **Built `/client-results/`** (builder directive): a tiered "Client Results" ROSTER, nested under About (breadcrumb Home / About / Client Results; an About-dropdown nav item; NO new top-level nav, NO anchored sub-links). **Tier 1** = deep featured case studies (Precision + Rock Solid cards, exact case-study stats, "Read the full case study →"). **Tier 2** = lighter roster cards for the other named testimonial owners (Tami, Rick, Phillip, Peter, David, Tim, Greg) with qualitative blurbs (NO fabricated numbers) linking to the experiences hub.
- **Distinctness held:** Client Results = results/roster + case-study depth; Experiences = the video-and-screenshot wall. They cross-link, not duplicate.
- **Hub-and-spoke interlinking wired:** Client Results Tier 1 → case studies; experiences hub → "See all client results"; each case study's Explore → "All Client Results"; existing industry/experiences proof cards already link the case studies.
- Schema: CollectionPage + ItemList (the 2 case studies) + BreadcrumbList. Inline `.cr-*` CSS. Sitemap + nav updated. **Future trigger:** once ~4-5 full case studies exist, evaluate a dedicated `/case-studies/` index in addition to the roster.


## 2026-06-21 (update) — Rock Solid revenue figure resolved to $1.4M
- **Owner confirmed Rock Solid hit $1.4M in their first full year** (from about $700K, a clean 2x). Standardized the figure across the whole site: the Rock Solid case study (At a Glance, stat band, return line, secondary stat, the revenue bar chart now an exact 2x, conclusion, meta/OG/Article schema), the Client Results roster Tier 1 card, the 11 proof cards that previously said "$1.3M" (homepage, 8 industry pages, experiences hub, Authority program), and the landscaping/lawn-care FAQ answers (also bumped "tripled" to "more than tripled" calls to match the ~4x). Reframed "crossed seven figures" to "doubled, to $1.4M" / "first full year" where it described revenue.
- **Kept (consistent with $1.4M, not contradictory):** Zach's VideoObject keeps its real YouTube title ("...from $700K to Over $1M..."). Nearby written captions/stat copy use $1.4M so the spoken rounding does not read as a competing figure. Program-tier copy ("companies over/under $1M") is unrelated and untouched.
- Resolves the standing legacy revenue-figure mismatch flag. No before/after GBP review count for Rock Solid (owner has no historical number; the current 49 stays as the single point).

## 2026-06-21 — Service-page FAQs answered + FAQPage schema live
- Owner supplied all 40 FAQ answers via the pre-launch sheet; reviewed, tightened, and wired in.
- 7 generated services: answers live in `_content.json` as `faqAnswers` (parallel to `faqQuestions`);
  `gen_service.py` renders them and emits per-page `FAQPage` JSON-LD. website-design (template): hand-edited.
- Decisions: website-cost FAQ KEEPS the $15K–$50K range, framed as competitor/market context (not our price) —
  the one sanctioned exception to the no-pricing rule, owner-approved. Second-GBP answer reframed to the
  Google-compliant "only with a real location" path (avoids listing-suspension risk).
- 5 technical answers authored by Claude (owner-flagged): local SEO vs map pack, GBP vs local SEO,
  Google Ads vs LSA, avoiding wasted ad spend, boosting vs real campaign.
- `FAQPage` schema is now satisfied for service pages (was gated on real answers). Still pending elsewhere.

## 2026-06-21 — Conviction-stat update + case-study sign-offs/confirmations (sheet rows 6-12)
- **Google Ads conviction stat** swapped from "$2 profit per $1 (Google Economic Impact)" to L&L's own
  result: "8-12%" typical campaign conversion rate vs a ~3-6% industry average (owner direction). Lead/sub
  updated; statSource note = "Lawn & Land client averages" (internal only, not rendered). Other 6 service
  conviction stats confirmed accurate by owner.
- **Case-study sign-offs RECEIVED:** Precision + Rock Solid owners approved names/numbers/video/screenshots
  (cleared to index at launch). Precision LSA figures ($250/wk, 9 leads) confirmed correct.
- **From The Ground Up** ($1.8M to $3.2M) numbers confirmed; case study NOT yet built (awaiting owner go-ahead).
- **GHL calendar** confirmed at 20 minutes (matches site copy; no change needed).

## 2026-06-21 — og:image share graphic added sitewide
- Owner-provided 1200x630 brand card ("digital marketing built for the green industry" + logo),
  optimized to a 164KB JPEG at `assets/images/og-share.jpg`. Wired `og:image` (+ width/height/alt)
  and `twitter:image` into all 33 indexable pages (website-design template -> 7 generated; sitewide
  insert for the rest). Absolute URL is staging (`new.lawnlab.dev`); flips to production at launch
  alongside the canonicals/og:url. Same graphic on every page (one brand card). Remaining launch SEO
  task: `robots.txt` + the staging->production domain flip.

## 2026-06-21 — Heading-overflow collision fix (widow-guard) + multi-device walkthrough
- BUG (reported on the gbp-management FAQ): the widow-guard (main.js) glued the last two words of
  every heading with a non-breaking space; for "GBP Management, answered." that made "Management,
  answered." one unbreakable ~401px unit, wider than the 300px FAQ heading column, so it overflowed
  and collided with the FAQ cards (and stranded "GBP" alone on line 1).
- FIX (systemic, all headings): the widow-guard now REVERTS the glue whenever it makes a heading
  wider than its box (scrollWidth > clientWidth) -> wraps naturally instead of overflowing. Re-runs
  debounced on resize, so the no-overflow guarantee holds at any window width, not just load width.
- FAQ heading column widened 300px -> 350px (gap 64 -> 56) so medium service names fit the intended
  2-line break ("GBP Management," / "answered."). 7/8 names wrap 1-2 clean lines; Reputation
  Management (longest, 411px) takes 3; none overflow.
- WALKTHROUGH: overflow detector run across the major layouts (homepage, service + hub, industry,
  program, about, contact, case study, client-results, experiences) at mobile 375 / tablet 768 /
  desktop 1440. Zero collisions or horizontal overflow found anywhere besides the now-fixed FAQ.
- Versions: main.js v54->55, service-page.css v3->4 (bumped sitewide).

## 2026-06-22 — Repo cleanup / optimization pass
- Image optimization: the 3 hero backgrounds (team-hero, reviews-hero, programs-hero — the last is the
  default hero on ~30 pages) were 2816px / ~1.9MB each; resized to 1760px + recompressed (q70, dark-
  overlaid so imperceptible) -> ~684KB each. matt-foreman.jpg 1200x1800/524KB -> 933x1400/380KB. Total
  ~3.9MB trimmed off the deploy. Logos (logo-badge.svg 1MB, logo-horizontal.svg 632KB) are base64
  rasters in an SVG wrapper — left untouched (on every page; re-exporting risks breaking branding;
  flagged to owner). Case-study screenshots left as-is.
- Docs brought current: README + build-status + service-page-template now reflect that FAQ answers +
  FAQPage schema, conviction stats, og:image, team headshots, and case-study sign-offs all landed
  2026-06-21; only placeholder images + robots.txt + the staging->production flip remain.
- Removed stray .DS_Store; build --check green, generator regenerate-clean, 0 broken links, 0
  [NEEDS YOUR INPUT] / em-dashes / emoji.
- NOTE: .git history is ~102MB (large image blobs committed before .gitignore existed). Not rewritten
  (force-push would disrupt the Vercel/GitHub integration); optional future cleanup via BFG if desired.

## 2026-06-22 — Blog built (index + post template) + first real post migrated
- The shelved article.css was re-oriented (was sidebar-left/TOC -> now content-left/sidebar-right) and
  is now the blog stylesheet. Two page types: blog INDEX (/resources/blog/, card grid + category filter,
  .blog-* classes) and individual POST (.article-* classes: hero, two-column, sticky right sidebar with
  About-the-Author + the contact .cform [GHL webhook] + related; pull-quote, lime callout, FAQ, CTA).
- Author = Matt Foreman; avatar at assets/images/matt-author.jpg (face-cropped from matt-stage-speaker.jpg).
- First real post migrated as the populated demo: "Why Landscaping SEO Gets Traffic But Not Qualified
  Leads" at its REAL slug, pulled via the WordPress REST API (/wp-json/wp/v2/posts?slug=...&_fields=...).
  That REST pipeline is the clean path for the eventual 81-post import. Em-dashes converted to brand style.
- OPEN: blog currently lives at /resources/blog/; may move to /blog/ at import to preserve the 81 existing
  /blog/<slug>/ URLs exactly. The other 80 posts are NOT yet imported (deferred by owner).

- Author/EEAT system (2026-06-22): built from the owner's directive. /author/matt-foreman/ hub
  (indexable; photo + long bio + podcast/book/LinkedIn/L&L profile pills + "Articles by Matt Foreman"
  archive grid; Person + Book + ProfilePage @graph). Every article: byline name links to the author
  page, a reusable "About the author" end block (short bio), sidebar trimmed to a teaser. Each article's
  BlogPosting sets author -> #matt-foreman (by @id, not a string) + publisher -> #organization; the Person
  @id is the SAME #matt-foreman as the About page (one unified entity). The eventual 81-post import MUST
  stamp the byline link + end block + BlogPosting schema into every post. Author CSS in article.css (v=3);
  em-dash-free. OWNER TO CONFIRM (general copy is live now, do not block): named award(s)+year, named
  conferences, Matt's PERSONAL LinkedIn (sameAs currently uses the L&L company LinkedIn as a stand-in).

- Blog framework follow-up (2026-06-22, from the EEAT auditor review): added gen_blog_schema.py, a
  reusable + idempotent generator that injects FAQPage JSON-LD into each blog post from its visible
  .article-faq Q&A (run after writing/importing posts). Added FAQPage to the live article (4 Q&A, text
  matches the visible FAQ). Set sample-post to robots noindex,follow (template/filler; the related-article
  + author-archive links point to it as placeholders until real posts exist -- resolve those at import).
  Verified all three EEAT schema connections resolve: author-page Person #matt-foreman; article BlogPosting
  author by @id == that Person (not a string); FAQPage matches the visible FAQ. Call-duration: the site is
  uniformly 20-minute (no 30-min exists anywhere); the filler article CTA was rewritten to a 20-minute strategy call. SKIPPED per owner: the article's generic body copy (intentional filler until the import).

## 2026-06-23 — Industry FAQ accuracy pass · program images · exclusive accordion · service-scope guardrail
- **Exclusive FAQ accordion (industry pages):** `/industries/*` FAQs use native `<details>`, which open
  independently (all could be open at once). Added a handler in `main.js` that closes sibling `<details>`
  when one opens (one open at a time), scoped to `.ind-faq > details`; JS-off degrades to native independent
  toggles. Bumped `main.js?v=56` sitewide. Verified live.
- **Program "Why us" images landed** (first real images dropped into placeholders): `/programs/growth/`
  (`assets/images/growth-why.jpg`, a real sod/hardscape job site) and `/programs/authority/`
  (`assets/images/authority-why.jpg`, a podcast/video-call still). Both optimized to 1200x900 (~250KB) with
  EXIF/GPS stripped (source phone photos carried GPS). Process: pull from owner's Drive -> resize/compress
  (Pillow) -> strip metadata -> swap the `.why-ph` placeholder contents for `<img style="...object-fit:cover">`.
- **Industry FAQ rewrite — POV correction + service-scope accuracy (owner review).** Two systemic problems
  found: (a) some questions were written in the CONTRACTOR's voice (pricing a job, "when should I clear my
  land", permits/burning) instead of as questions a contractor asks their MARKETING agency; (b) copy
  hallucinated services L&L does NOT offer (running renewals, rebooking, reactivating customers, deposits,
  waitlists/overflow, takedown, social-media management, running the client's email list). Fixed per page,
  visible copy + FAQPage JSON-LD kept in lockstep, em-dash-free:
  - **landscaping:** new-website (you WILL get a new site, no Frankenstein builds), spring-timing (winter =
    pre-positioning, dropped the unrealistic "selling installs in Dec/Jan"), slow-season (realistic, then the
    competitors-coast + SEO-lead-time opportunity).
  - **outdoor-living:** lead-gen reframed to owning your leads via Google + AI search (dropped Houzz); spring
    now embraces paid (high intent = lowest CPA / highest ROI) + always-on + not set-and-forget; portfolio
    answer lists real channels (website, GBP, press releases, paid ads — NO social mgmt). Also fixed the
    comparison-table row that claimed we build Houzz/Instagram.
  - **lawn-care:** spring-rush split by channel (SEO a season ahead since it is slow to compound; paid ads
    ~1-2 weeks pre-season to build momentum + let learning settle; hold ads through peak); retention answer
    no longer implies L&L runs the client's renewals (renewal/prepay systems are theirs; our job is the
    marketing around them).
  - **lawn-maintenance:** spring-rush aligned to the channel-split strategy; REMOVED the question "What
    happens to the leads after they come in?"; commercial/HOA reframed as an honest hybrid (relationships are
    theirs to build, the research experience — site / branding / reputation / reviews — is ours).
  - **land-clearing + excavation:** FULL FAQ rewrites (all 7 questions each) from the marketing-agency POV;
    every contractor-voice question killed.
  - **holiday-lighting:** FULL PAGE revisit. The "we do the client's sales/ops" hallucination ran through the
    meta tags, schema description, intro lede, comparison table, the season module, BOTH service cards
    (CRM + AI), the 5-step, the proof + testimonial intros, the Growth program card, and the FAQ — all
    reworked to what L&L actually does (demand-gen Meta ads, web/SEO/GBP presence, lead capture +
    speed-to-lead, reputation/reviews, permanent-lighting marketing). Repositioned the whole page around the
    OFF-SEASON gap-filler thesis for lawn/landscape companies (esp. northern winters): "if you're not
    offering holiday lighting yet, you should, and here's how we market it." New FAQ leads with that + a
    dedicated Meta ads question (Meta is the emphasized channel — best ROI for this trade).
- **NEW GUARDRAIL — owner's #1 accuracy rule (now in repo + agent memory):** website copy may claim ONLY
  L&L's 8 real services (Website Design, Local SEO, Google Ads, Meta Ads, GBP Management, Your AI Partner /
  AI search, Reputation Management, CRM & Automation = lead capture + speed-to-lead follow-up). NEVER imply
  L&L does the client's sales, renewals, rebooking, deposits, waitlists, social-media management, or email
  list. Frame relationships + renewals as the client's; L&L's role is the marketing around them. Industry-page
  FAQs answer questions a contractor asks their marketing agency, never customer-to-contractor questions.
  When auditing, scan the WHOLE page (meta description, OG/Twitter tags, JSON-LD, service cards, modules),
  not just the visible FAQ — the overreach hides everywhere.
- **OPEN — accuracy sweep (next session):** the same service-scope overreach still lives in BODY copy on
  other pages. Confirmed still-to-fix: **lawn-care** (comparison rows "Sells prepay and renewals" +
  "Protects retention... renewals", the seasonal "Sell prepay & renewals" module, 5-step "automated
  follow-up and renewals... all run for you", CRM card "renewal reminders") and **outdoor-living** (the
  "Knows your season" comparison row + the "How long until I see results?" FAQ still lean on the OLD
  "don't advertise in spring" stance, now contradicting the new spring-positive Q2). Sweep the remaining
  industry + program/service pages for the same pattern.
- **Images (2026-06-23, later):** all 8 `/industries/*` intro placeholders (`.ind-ph`) now hold real
  owner-provided photos (`assets/images/<industry>-intro.jpg`): landscaping, lawn-care, lawn-maintenance,
  outdoor-living, land-clearing, excavation, septic-installation, holiday-lighting. Each PNG -> 1400x788
  JPEG (~240-350KB), EXIF/GPS stripped, shown in the template 4:3 box via object-fit:cover (center-cropped
  on desktop, full 16:9 on mobile). Source: the owner's shared Drive folder, one file named per page. (Plus
  the two `/programs/*` "Why us" images earlier the same day.) Remaining placeholders: homepage CTA +
  service-page screenshots.
## 2026-06-26 — Production operations baseline, audit rollback, combo pages, and footer badge
- **Production state:** the canonical public site is `https://lawnandlandmarketing.com` on Vercel project `lawnland-site`. Future verification should hit the custom domain directly, not stale/duplicate Vercel aliases.
- **Audit reconciliation:** safe audit fixes stayed live, but risky homepage performance overrides were rolled back after confirmed brand-font and nav-hover regressions. Homepage LCP/performance work is now preview-only unless Matt explicitly approves production after visual/interaction QA.
- **Homepage performance guardrail:** do not trade Rethink Sans, dropdown behavior, mobile menu behavior, hero fidelity, or CTA behavior for Lighthouse numbers. Critical CSS/font-path changes must prove both LCP and CLS and pass desktop nav hover + mobile menu + computed-font checks.
- **Combo-page program:** service × industry pages should be contextually linked from relevant industry service cards, not stuffed into the main nav/footer. Preserve parent service/industry links, sitemap entries, unique business spine, no cannibalization, and no em dashes.
- **Thanks for Preparing:** `/thanks-for-preparing/` is live as the post-booking prep video page. Keep it focused on pre-call education and use recovered/source-verified video assets when editing.
- **Universal footer:** the legal/footer badge text is `Grown In St. Petersburg, FL` with the Landscaping palm SVG. Desktop legal row is copyright left, badge centered, Terms/Privacy right. Mobile legal row shows Terms/Privacy, then copyright, then the palm badge centered at the very bottom.
- **Cache-bust discipline:** current stylesheet cache-bust is `styles.css?v=156`. Any future CSS change should bump the relevant `?v=` query sitewide before deploy.
- **Docs baseline:** newest operating reference is `docs/website-source-of-truth/current-state-2026-06-26.md`; audit rollback handoff is `docs/audit-rollback-handoff-2026-06-25.md`; combo-page directive is `docs/directives/combo-pages-agent-directive.md`.
- **Mow Money, Mow Problems system page (2026-07-07):** `/marketing-services/mow-money-mow-problems/` is the branded name of L&L's whole digital-marketing system AND the genuine trademark specimen for USPTO Serial No. 99184265 (IC 035). It must stay REAL use: publicly reachable, indexable (never noindex), footer-linked sitewide (top of the Marketing Services column), working strategy-call CTAs, in `sitemap.xml`. Write the mark exactly **Mow Money, Mow Problems** (comma + capitalization locked); ™ on the H1 and the attribution line ("…is a digital marketing service of Lawn and Land Marketing LLC."). Hand-built page (hub-page chrome + inline style block) — never add the slug to `_content.json`/gen_service.py. Distinct from the podcast page under Resources; this one reads as a *service* brand on purpose.
- **Matt Foreman entity hub (2026-07-07):** `/matt-foreman/` is the single canonical page for the PERSON entity (entity SEO / AI search / speaking + press). `/author/matt-foreman/` deleted + 301'd (both legacy alias redirects in `vercel.json` were pointing the OTHER way and were removed to prevent a loop). The Person `@id` `https://lawnandlandmarketing.com/#matt-foreman` NEVER changes; only `url`/`mainEntityOfPage` moved. Person `sameAs` = PERSONAL profiles (LinkedIn/Instagram/Facebook personal + Amazon book + Apple/Spotify/YouTube podcast + podcast site), never the company socials. gen_blog.py stamps ALL articles into the hub (`auth_path`). The media-kit bios + the one-line "entity sentence" are LOCKED wording; reuse verbatim on external profiles. Speaking section facts are owner-supplied (Seven Figure Agency, 2025 + 2026); never invent appearances. Title stays "Founder & Owner" (owner decision, not CEO).

## 2026-07-30 — Post-migration SEO consolidation batch
- **Decision:** prioritize a low-risk redirect and internal-link batch before publishing replacement
  articles for mismatched legacy redirects. The production audit found the new site technically healthy,
  but several old URLs still carried visibility and the new vertical SEO pages were underlinked.
- **Redirect repair:** both variants of `/blog/category/seo/` now permanently redirect to
  `/resources/blog/category/seo/`.
- **Internal authority:** the homepage Local SEO panel, generated SEO category hub, local SEO guide,
  seven-step landscaping SEO article, and landscape marketing guide now point contextually to the
  lawn-care and/or landscaping SEO service pages.
- **Generator durability:** SEO category intro links live in `_blog.json` via `introHtml` so `gen_blog.py`
  preserves them. The generator now normalizes its pagination CSS, fixing a pre-existing non-idempotent
  behavior that had duplicated the same style block on every run.
- **Deferred intentionally:** do not redirect the old blogging, email-marketing, or CRM article URLs to
  another broad destination. Restore each topic with a useful, current replacement page first, then change
  its old redirect to the matching replacement.
