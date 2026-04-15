# Page Registry

Status key
- developed = real body content and strategic substance
- scaffolded = live shell with limited content depth
- planned = approved but not live
- killed = intentionally removed from scope
- legacy = non-canonical route still present or still leaking through links

## Approved Canonical Pages
| Section | Page | Route | Live? | Status | Notes |
|---|---|---:|---|---|---|
| Core | Home | `/` | yes | developed | Strongest page on the site so far; real strategic content and proof sections are present. |
| Core | About | `/about/` | yes | scaffolded | Solid H1 and framing, but page appears thin relative to importance. |
| Core | Contact | `/contact/` | yes | scaffolded | Canonical contact page is live, but appears thin and mostly shell-level. |
| Core | Get Started | `/get-started/book-strategy-call/` | yes | developed | Existing conversion page; should remain a strong CTA destination. |
| Programs | Programs hub | `/programs/` | yes | scaffolded | Strong direction, but still light; includes obvious placeholder content. |
| Programs | Growth | `/programs/growth/` | yes | developed | Live and materially built; still needs final QA against current messaging. |
| Programs | Authority | `/programs/authority/` | yes | developed | Live and materially built; still needs final QA against current messaging. |
| Marketing Services | Services hub | `/marketing-services/` | yes | scaffolded | Route is correct, but page body is very thin today. |
| Marketing Services | Website Design | `/marketing-services/website-design/` | yes | scaffolded | Correct route and H1; needs substantive body content. |
| Marketing Services | Local SEO | `/marketing-services/local-seo/` | yes | scaffolded | Live shell. |
| Marketing Services | GBP Management | `/marketing-services/gbp-management/` | yes | scaffolded | Live shell. |
| Marketing Services | Google Ads | `/marketing-services/google-ads/` | yes | scaffolded | Live shell. |
| Marketing Services | Meta Ads | `/marketing-services/meta-ads/` | yes | scaffolded | Live shell. |
| Marketing Services | Your AI Partner | `/marketing-services/your-ai-partner/` | yes | scaffolded | Live shell. |
| Marketing Services | Reputation Management | `/marketing-services/reputation-management/` | yes | scaffolded | Live shell. |
| Marketing Services | Automation | `/marketing-services/automation/` | yes | scaffolded | Live shell. |
| Industries | Industries hub | `/industries/` | yes | scaffolded | Live shell. |
| Industries | Lawn Care | `/industries/lawn-care/` | yes | scaffolded | Live shell. |
| Industries | Landscape Maintenance | `/industries/landscape-maintenance/` | yes | scaffolded | Live shell. |
| Industries | Landscape Design & Build | `/industries/landscape-design-build/` | yes | scaffolded | Live shell. |
| Industries | Outdoor Living / Hardscaping | `/industries/outdoor-living/` | yes | scaffolded | Live shell. |
| Industries | Irrigation Services | `/industries/irrigation/` | yes | scaffolded | Live shell. |
| Industries | Excavation | `/industries/excavation/` | yes | scaffolded | Live shell. |
| Industries | Septic Services | `/industries/septic-services/` | yes | scaffolded | Live shell. |
| Resources | Resources hub | `/resources/` | yes | scaffolded | Live shell; legacy guides/contact route drift has been removed. |
| Resources | Blog | `/resources/blog/` | yes | scaffolded | Live but needs content strategy and index depth. |
| Resources | Meet The Team | `/resources/meet-the-team/` | yes | scaffolded | Live shell. |
| Resources | Experiences / Reviews | `/resources/experiences-reviews/` | yes | scaffolded | Live shell. |
| Resources | Private Facebook Group | `/resources/private-facebook-group/` | yes | scaffolded | Live shell. |
| Resources | Mow Money, Mow Problems Podcast | `/resources/mow-money-mow-problems-podcast/` | yes | scaffolded | Live shell. |

## Killed / Non-Canonical / Legacy
| Type | Route | Current State | Action |
|---|---|---|---|
| killed | `/services/` | Returns 404 / intentionally retired | Keep removed from internal linking and do not reintroduce as canonical |
| killed | `/pricing/` | Returns 404 / retired | Remove lingering references and do not reintroduce as canonical page |
| killed | `/resources/guides/` | Page file deleted and removed from internal structure | Keep retired unless explicitly brought back with a new decision |
| legacy | `/resources/contact/` | Page file deleted; internal uses replaced | Continue using `/contact/` only |
| legacy | `/services/...` child routes | Internal uses replaced with `/marketing-services/...` equivalents | Keep retired and redirect later only if needed |

## Highest-Leverage Pages To Finish Next
1. `/programs/`
2. `/marketing-services/`
3. `/about/`
4. `/contact/`
5. core service detail pages starting with `/marketing-services/website-design/`, `/marketing-services/local-seo/`, `/marketing-services/google-ads/`

## Audit Notes
- The live homepage is ahead of the rest of the site.
- Secondary pages are often present structurally but not yet persuasive enough to be considered finished.
- Architecture cleanup should happen before large new page expansion so the internal link graph stops drifting.
