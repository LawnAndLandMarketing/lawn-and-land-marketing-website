#!/usr/bin/env python3
"""
Build all standardized pages for new.lawnlab.dev
Every page gets: canonical nav + hero banner + blank body + canonical footer
"""
import os
import json

REPO = "/tmp/lawnland-site"

# Read canonical blocks from homepage
def read_file(path):
    with open(path, 'r') as f:
        return f.read()

homepage = read_file(f"{REPO}/index.html")

# Extract blocks by line ranges (from our audit)
lines = homepage.split('\n')

# Find nav block
nav_start = None
nav_end = None
for i, line in enumerate(lines):
    if '<nav class="nav"' in line:
        nav_start = i
    if '</nav>' in line and nav_start is not None:
        nav_end = i
        break

# Find announcement bar
announce_start = None
announce_end = None
for i, line in enumerate(lines):
    if 'announcement-bar' in line and announce_start is None:
        announce_start = i
    if announce_start and '</div>' in line and i > announce_start:
        # Find the closing of announcement bar (3 lines after start)
        announce_end = announce_start + 3
        break

# Find footer
footer_start = None
footer_end = None
for i, line in enumerate(lines):
    if '<footer class="footer-v2">' in line:
        footer_start = i
    if '</footer>' in line and footer_start is not None:
        footer_end = i
        break

NAV_BLOCK = '\n'.join(lines[nav_start:nav_end+1])
FOOTER_BLOCK = '\n'.join(lines[footer_start:footer_end+1]) + '\n\n  <script src="/assets/js/main.js?v=49"></script>\n</body>\n</html>'

# Get the inline CSS from homepage <head> that's needed for mega menu
head_css_start = None
head_css_end = None
for i, line in enumerate(lines):
    if '<style>' in line and head_css_start is None and i > 15:
        head_css_start = i
    if '</style>' in line and head_css_start is not None and head_css_end is None:
        head_css_end = i
        break

MEGA_MENU_CSS = '\n'.join(lines[head_css_start:head_css_end+1]) if head_css_start else ''

# Announcement bar HTML
ANNOUNCE_HTML = '''  <!-- ANNOUNCEMENT BAR -->
  <div class="announcement-bar">
    <a href="/contact/" class="announcement-inner announcement-inner--link">
      <span class="announcement-text">🎉 Free strategy call available — book now to discuss your growth &nbsp;→</span>
    </a>
  </div>'''

# Hero CSS (from /programs/ page)
HERO_CSS = '''    .simple-hero {
      position: relative;
      padding: 40px 0 34px;
      min-height: 560px;
      display: flex;
      align-items: flex-end;
      background:
        linear-gradient(180deg, rgba(4,12,7,0.35) 0%, rgba(4,12,7,0.78) 46%, rgba(4,12,7,0.96) 100%),
        linear-gradient(110deg, rgba(4,12,7,0.90) 0%, rgba(4,12,7,0.64) 46%, rgba(4,12,7,0.82) 100%),
        var(--hero-image) center/cover no-repeat;
      border-bottom: 1px solid rgba(255,255,255,0.06);
    }
    .simple-hero::after {
      content: '';
      position: absolute;
      inset: auto 0 0;
      height: 140px;
      background: linear-gradient(180deg, transparent, rgba(7,16,10,0.95));
      pointer-events: none;
    }
    .hero-inner {
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: var(--max);
      margin: 0 auto;
      padding: 0 24px;
    }
    .hero-copy { max-width: 760px; }
    .hero-copy h1 {
      font-family: var(--font-h);
      font-size: clamp(36px, 5vw, 58px);
      line-height: 0.96;
      font-weight: 800;
      font-style: italic;
      color: var(--white);
      margin-bottom: 18px;
      letter-spacing: -0.03em;
    }
    .hero-copy p {
      max-width: 60ch;
      font-size: 18px;
      color: rgba(255,255,255,0.78);
      margin-bottom: 24px;
    }
    .hero-actions { display: flex; flex-wrap: wrap; gap: 12px; }
    .btn { display: inline-flex; align-items: center; gap: 8px; }
    .btn svg { flex-shrink: 0; }
    .hero-kicker {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 8px 14px;
      margin-bottom: 18px;
      border-radius: 999px;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.10);
      font-family: var(--font-l);
      font-size: 12px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: rgba(255,255,255,0.74);
    }
    .hero-kicker::before {
      content: '';
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--lime);
      box-shadow: 0 0 18px rgba(172,231,29,0.8);
    }
    @media(max-width:768px) {
      .simple-hero { min-height: auto; padding: 56px 0 28px; }
    }'''


def build_page(path, title, meta_desc, breadcrumbs_html, kicker, h1, subtext):
    """Generate a complete page HTML."""
    canonical = f"https://new.lawnlab.dev{path}"
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Lawn &amp; Land Marketing</title>
  <meta name="description" content="{meta_desc}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{title} | Lawn &amp; Land Marketing">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:type" content="website">
  <link rel="icon" type="image/svg+xml" href="/assets/logos/logo-badge.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Rethink+Sans:ital,wght@0,400;0,600;1,700;1,800&family=Mulish:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/styles.css?v=38">
  <style>
{MEGA_MENU_CSS.replace("<style>", "").replace("</style>", "")}

{HERO_CSS}
  </style>
</head>
<body>

{ANNOUNCE_HTML}

<!-- NAV with MEGA MENU (canonical — matches homepage) -->
{NAV_BLOCK}

  <!-- HERO BANNER -->
  <section class="simple-hero" style="--hero-image: url('/assets/images/programs-hero.jpg');">
    <div class="hero-inner">
      <div class="hero-copy" data-reveal="fade-up">
        <div class="crumbs">{breadcrumbs_html}</div>
        <div class="hero-kicker">{kicker}</div>
        <h1>{h1}</h1>
        <p>{subtext}</p>
        <div class="hero-actions">
          <a href="/contact/" class="btn btn--lime">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
              <line x1="16" y1="2" x2="16" y2="6"/>
              <line x1="8" y1="2" x2="8" y2="6"/>
              <line x1="3" y1="10" x2="21" y2="10"/>
            </svg>
            Schedule Strategy Call
          </a>
          <a href="/contact/" class="btn btn--ghost">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
            Contact Us
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- PAGE BODY (content to be added) -->
  <section style="padding: 80px 0;">
    <div style="max-width: var(--max, 1320px); margin: 0 auto; padding: 0 24px;">
      <!-- Content coming soon -->
    </div>
  </section>

  <!-- FOOTER (canonical — matches homepage) -->
{FOOTER_BLOCK}
'''
    return html


# ============================================================
# PAGE DEFINITIONS
# ============================================================

pages = [
    # Marketing Services (NEW)
    {
        "path": "/marketing-services/",
        "title": "Marketing Services for Landscaping Companies",
        "meta": "Every marketing service your landscaping company needs — website design, SEO, Google Ads, Meta Ads, automation — built as one machine.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Marketing Services</span>',
        "kicker": "Marketing Services",
        "h1": "Every service. One machine. Built for landscaping companies.",
        "sub": "Website design, SEO, paid ads, reputation management, and automation — all working together. No piecemeal vendors. No conflicting strategies."
    },
    {
        "path": "/marketing-services/website-design/",
        "title": "Landscaping Website Design",
        "meta": "Custom website design built specifically for landscaping companies. Turn visitors into booked estimates with conversion-focused design.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/marketing-services/">Marketing Services</a><span>/</span><span>Website Design</span>',
        "kicker": "Website Design",
        "h1": "Landscaping websites that turn visitors into booked estimates.",
        "sub": "Your website is the center of the machine. We build custom sites that load fast, look professional, and convert the traffic we send to them."
    },
    {
        "path": "/marketing-services/local-seo/",
        "title": "Local SEO for Landscaping Companies",
        "meta": "Local SEO services built for landscaping companies. Own the organic search results in the markets that matter most to your business.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/marketing-services/">Marketing Services</a><span>/</span><span>Local SEO</span>',
        "kicker": "Local SEO",
        "h1": "Own the organic search results in the markets that matter.",
        "sub": "Service area pages, local citations, and content strategy built specifically for how landscaping companies get found online."
    },
    {
        "path": "/marketing-services/gbp-management/",
        "title": "Google Business Profile Management for Landscapers",
        "meta": "Professional GBP management for landscaping companies. Win more map-pack calls and dominate local search results.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/marketing-services/">Marketing Services</a><span>/</span><span>GBP Management</span>',
        "kicker": "GBP Management",
        "h1": "Win more map-pack calls without guessing what Google wants.",
        "sub": "Google Business Profile optimization, review strategy, and local presence management — designed for landscaping companies that want to own the map."
    },
    {
        "path": "/marketing-services/google-ads/",
        "title": "Google Ads for Landscaping Companies",
        "meta": "Google Ads management built for landscaping companies. Capture intent from homeowners ready to hire right now.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/marketing-services/">Marketing Services</a><span>/</span><span>Google Ads</span>',
        "kicker": "Google Ads",
        "h1": "Capture intent from homeowners ready to hire right now.",
        "sub": "Search campaigns, local service ads, and conversion tracking — structured specifically for how landscaping leads actually convert."
    },
    {
        "path": "/marketing-services/meta-ads/",
        "title": "Meta Ads for Landscaping Companies",
        "meta": "Meta Ads (Facebook & Instagram) management for landscaping companies. Stay in front of local homeowners before they even search.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/marketing-services/">Marketing Services</a><span>/</span><span>Meta Ads</span>',
        "kicker": "Meta Ads",
        "h1": "Stay in front of local homeowners before they even search.",
        "sub": "Facebook and Instagram advertising that builds awareness, generates leads, and keeps your brand top-of-mind in your service area."
    },
    {
        "path": "/marketing-services/your-ai-partner/",
        "title": "AI Marketing Partner for Landscaping Companies",
        "meta": "AI-powered marketing tools and automation for landscaping companies. Smarter follow-up, faster execution, and operational leverage.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/marketing-services/">Marketing Services</a><span>/</span><span>Your AI Partner</span>',
        "kicker": "Your AI Partner",
        "h1": "Operational leverage, smarter follow-up, and faster execution.",
        "sub": "AI tools that help your team respond faster, follow up smarter, and eliminate the manual bottlenecks that cost you leads."
    },
    {
        "path": "/marketing-services/reputation-management/",
        "title": "Reputation Management for Landscaping Companies",
        "meta": "Reputation management services for landscaping companies. Turn happy clients into proof that compounds forever.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/marketing-services/">Marketing Services</a><span>/</span><span>Reputation Management</span>',
        "kicker": "Reputation Management",
        "h1": "Turn happy clients into proof that compounds forever.",
        "sub": "Review generation, response management, and social proof strategy — built to make your best work visible to every future customer."
    },
    {
        "path": "/marketing-services/automation/",
        "title": "Marketing Automation for Landscaping Companies",
        "meta": "Marketing automation built for landscaping companies. Remove lead leaks and speed up every handoff in your sales process.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/marketing-services/">Marketing Services</a><span>/</span><span>Automation</span>',
        "kicker": "Automation",
        "h1": "Remove lead leaks and speed up every handoff.",
        "sub": "Automated follow-up sequences, CRM integration, and workflow automation — so no lead falls through the cracks and your team stays focused."
    },

    # About section
    {
        "path": "/about/meet-the-team/",
        "title": "Meet the Team",
        "meta": "Meet the strategists, creatives, and operators behind Lawn & Land Marketing. The team that builds growth machines for landscaping companies.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/about/">About</a><span>/</span><span>Meet the Team</span>',
        "kicker": "Our Team",
        "h1": "The strategists, creatives, and operators behind the work.",
        "sub": "We're not a faceless agency. Meet the people who actually build, manage, and optimize your marketing every day."
    },
    {
        "path": "/about/experiences-reviews/",
        "title": "Client Experiences & Reviews",
        "meta": "See what landscaping company owners say about working with Lawn & Land Marketing. Real reviews, real results, real partnerships.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/about/">About</a><span>/</span><span>Experiences &amp; Reviews</span>',
        "kicker": "Experiences & Reviews",
        "h1": "What clients say after we build the machine with them.",
        "sub": "Real feedback from real landscaping company owners. No cherry-picked quotes — just honest experiences from companies at every stage."
    },

    # Industries
    {
        "path": "/industries/",
        "title": "Industries We Serve",
        "meta": "Digital marketing built exclusively for the green industry. Lawn care, landscaping, irrigation, excavation, outdoor living, and septic services.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Industries</span>',
        "kicker": "Industries",
        "h1": "We only work in the green industry. That's the whole point.",
        "sub": "Lawn care, landscaping, irrigation, excavation, outdoor living, septic — we know your customers, your seasonality, and your competitive landscape."
    },
    {
        "path": "/industries/lawn-care/",
        "title": "Marketing for Lawn Care Companies",
        "meta": "Digital marketing built for lawn care companies. Recurring route density, retention, and seasonal demand generation.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/industries/">Industries</a><span>/</span><span>Lawn Care</span>',
        "kicker": "Lawn Care",
        "h1": "Recurring route density, retention, and seasonal demand.",
        "sub": "Marketing built for the lawn care model — recurring revenue, tight service areas, and customers who need to find you before they find someone else."
    },
    {
        "path": "/industries/landscape-maintenance/",
        "title": "Marketing for Landscape Maintenance Companies",
        "meta": "Digital marketing for landscape maintenance companies. Position for contracts, upsells, and year-round value.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/industries/">Industries</a><span>/</span><span>Landscape Maintenance</span>',
        "kicker": "Landscape Maintenance",
        "h1": "Position for contracts, upsells, and year-round value.",
        "sub": "Marketing that helps maintenance companies land commercial contracts, grow residential routes, and build the kind of reputation that compounds."
    },
    {
        "path": "/industries/landscape-design-build/",
        "title": "Marketing for Landscape Design & Build Companies",
        "meta": "Digital marketing for landscape design and build companies. Higher-ticket projects need stronger positioning and proof.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/industries/">Industries</a><span>/</span><span>Landscape Design &amp; Build</span>',
        "kicker": "Landscape Design & Build",
        "h1": "Higher-ticket projects need stronger positioning and proof.",
        "sub": "When the average job is $15K+, your marketing has to do more than generate clicks. It has to build trust before the first phone call."
    },
    {
        "path": "/industries/outdoor-living/",
        "title": "Marketing for Outdoor Living Companies",
        "meta": "Digital marketing for outdoor living companies. Showcase premium installs and justify premium pricing.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/industries/">Industries</a><span>/</span><span>Outdoor Living</span>',
        "kicker": "Outdoor Living",
        "h1": "Showcase premium installs and justify premium pricing.",
        "sub": "Patios, pergolas, outdoor kitchens, fire features — the work sells itself when the marketing actually shows it off properly."
    },
    {
        "path": "/industries/irrigation/",
        "title": "Marketing for Irrigation Companies",
        "meta": "Digital marketing for irrigation companies. Own repair demand and system upgrade opportunities in your market.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/industries/">Industries</a><span>/</span><span>Irrigation</span>',
        "kicker": "Irrigation",
        "h1": "Own repair demand and system upgrade opportunities.",
        "sub": "Irrigation marketing that captures urgent repair searches and positions your company as the go-to for new installations and system upgrades."
    },
    {
        "path": "/industries/excavation/",
        "title": "Marketing for Excavation Companies",
        "meta": "Digital marketing for excavation companies. Project-based search demand with local trust as the competitive wedge.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/industries/">Industries</a><span>/</span><span>Excavation</span>',
        "kicker": "Excavation",
        "h1": "Project-based search demand with local trust as the wedge.",
        "sub": "Excavation work lives and dies on local reputation and search visibility. We build both so you're the first call, not the third quote."
    },
    {
        "path": "/industries/septic-services/",
        "title": "Marketing for Septic Service Companies",
        "meta": "Digital marketing for septic service companies. Urgent local intent that rewards clarity, speed, and reviews.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/industries/">Industries</a><span>/</span><span>Septic Services</span>',
        "kicker": "Septic Services",
        "h1": "Urgent local intent that rewards clarity, speed, and reviews.",
        "sub": "When someone needs septic service, they need it now. Marketing that makes your company the obvious, trustworthy choice in that moment."
    },

    # Programs (Growth and Authority — programs/index.html is the reference, skip it)
    {
        "path": "/programs/growth/",
        "title": "Growth Program for Landscaping Companies",
        "meta": "The Growth program builds your marketing foundation — website, SEO, ads, and automation for landscaping companies under $1M.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/programs/">Programs</a><span>/</span><span>Growth</span>',
        "kicker": "Growth Program",
        "h1": "Build the foundation. Generate the demand. Grow past the plateau.",
        "sub": "For landscaping companies ready to stop guessing and start building a real marketing engine. Website, SEO, ads, and automation — installed in the right order."
    },
    {
        "path": "/programs/authority/",
        "title": "Authority Program for Landscaping Companies",
        "meta": "The Authority program builds market dominance — advanced SEO, brand positioning, and category leadership for 7-figure landscaping companies.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/programs/">Programs</a><span>/</span><span>Authority</span>',
        "kicker": "Authority Program",
        "h1": "Build the category-leading brand in your market.",
        "sub": "For established landscaping companies that want to own their market. Advanced positioning, deeper SEO, and the kind of brand gravity that makes competitors irrelevant."
    },

    # Resources
    {
        "path": "/resources/",
        "title": "Resources for Landscaping Company Owners",
        "meta": "Free resources, guides, blog articles, and tools for landscaping company owners who want to grow smarter.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Resources</span>',
        "kicker": "Resources",
        "h1": "Guides, tools, and sharp advice for landscaping company owners.",
        "sub": "Everything we've learned about growing landscaping companies — packaged into articles, guides, and tools you can use right now."
    },
    {
        "path": "/resources/contact/",
        "title": "Contact Us",
        "meta": "Get in touch with Lawn & Land Marketing. Start the conversation about growing your landscaping company.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/resources/">Resources</a><span>/</span><span>Contact</span>',
        "kicker": "Contact",
        "h1": "Start the conversation or ask the right next question.",
        "sub": "Whether you're ready to go or just exploring — reach out. No pressure, no pitch. Just clarity on what makes sense for your company."
    },
    {
        "path": "/resources/blog/",
        "title": "Blog — Landscaping Marketing Insights",
        "meta": "Sharp takes and practical growth advice for green industry owners. SEO, ads, websites, automation — from the team that does it daily.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/resources/">Resources</a><span>/</span><span>Blog</span>',
        "kicker": "Blog",
        "h1": "Sharp takes and practical growth advice for the green industry.",
        "sub": "No fluff, no filler. Just real marketing insight from the team that builds growth machines for landscaping companies every day."
    },
    {
        "path": "/resources/meet-the-team/",
        "title": "Meet the Team",
        "meta": "Meet the people behind Lawn & Land Marketing. Strategists, creatives, and operators who build marketing machines for landscaping companies.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/resources/">Resources</a><span>/</span><span>Meet the Team</span>',
        "kicker": "Our Team",
        "h1": "See who you'll actually be working with.",
        "sub": "Real people, real expertise, real accountability. Meet the team that manages your marketing like it's their own business."
    },
    {
        "path": "/resources/experiences-reviews/",
        "title": "Client Experiences & Reviews",
        "meta": "Real reviews and experiences from landscaping company owners who work with Lawn & Land Marketing.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/resources/">Resources</a><span>/</span><span>Experiences &amp; Reviews</span>',
        "kicker": "Client Experiences",
        "h1": "See the feedback, trust signals, and client stories.",
        "sub": "We don't hide behind curated testimonials. Here's what real landscaping company owners have to say about working with us."
    },
    {
        "path": "/resources/private-facebook-group/",
        "title": "Private Facebook Group for Landscaping Owners",
        "meta": "Join the Lawn & Land Marketing private Facebook group. Extra training, industry insights, and direct access to the conversation.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/resources/">Resources</a><span>/</span><span>Private Facebook Group</span>',
        "kicker": "Facebook Group",
        "h1": "Extra training, insight, and direct access to the conversation.",
        "sub": "A private community for landscaping company owners who want to grow smarter. Real discussions, real strategies, no spam."
    },
    {
        "path": "/resources/mow-money-mow-problems-podcast/",
        "title": "Mow Money, Mow Problems Podcast",
        "meta": "The Mow Money, Mow Problems podcast — field-tested lessons on growth, operations, and marketing for landscaping companies.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/resources/">Resources</a><span>/</span><span>Podcast</span>',
        "kicker": "Podcast",
        "h1": "Field-tested lessons on growth, ops, and marketing.",
        "sub": "The Mow Money, Mow Problems podcast — real conversations with landscaping company owners and operators about what actually works."
    },
    {
        "path": "/resources/guides/",
        "title": "Free Marketing Guides for Landscaping Companies",
        "meta": "Download free marketing guides built specifically for landscaping company owners. SEO, ads, websites, and growth strategy.",
        "crumbs": '<a href="/">Home</a><span>/</span><a href="/resources/">Resources</a><span>/</span><span>Guides</span>',
        "kicker": "Guides",
        "h1": "Free guides built for landscaping company owners.",
        "sub": "Comprehensive, actionable guides on SEO, Google Ads, website design, and marketing strategy — written for the green industry."
    },

    # About
    {
        "path": "/about/",
        "title": "About Lawn & Land Marketing",
        "meta": "The only digital marketing agency built exclusively for lawn care and landscaping companies. Our story, mission, and why specialization wins.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>About</span>',
        "kicker": "About Us",
        "h1": "Built for landscaping companies. Nothing else.",
        "sub": "We're not a generalist agency that took on a few lawn care clients. We built this entire company around one industry — and that's what makes it work."
    },

    # Footer/utility pages
    {
        "path": "/contact/",
        "title": "Contact Lawn & Land Marketing",
        "meta": "Contact Lawn & Land Marketing to discuss your landscaping company's growth. Free strategy call, no pressure.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Contact</span>',
        "kicker": "Contact Us",
        "h1": "Let's talk about growing your landscaping company.",
        "sub": "Book a free strategy call or send us a message. No pitch, no pressure — just an honest conversation about what's possible."
    },
    {
        "path": "/good-fit/",
        "title": "Are We a Good Fit?",
        "meta": "Find out if Lawn & Land Marketing is the right partner for your landscaping company. Honest assessment, no pressure.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Are We a Good Fit?</span>',
        "kicker": "Good Fit",
        "h1": "Are we a good fit? Here's how to tell.",
        "sub": "We're not for everyone — and that's intentional. Here's who we work best with, and who might be better served elsewhere."
    },
    {
        "path": "/results/",
        "title": "Client Results",
        "meta": "See the results Lawn & Land Marketing delivers for landscaping companies. Real data, real growth, real companies.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Results</span>',
        "kicker": "Client Results",
        "h1": "Real results from real landscaping companies.",
        "sub": "We measure what matters — leads, revenue, and growth. Here's what happens when the full machine is running."
    },
    {
        "path": "/case-studies/",
        "title": "Case Studies — Landscaping Marketing Success Stories",
        "meta": "Detailed case studies showing how Lawn & Land Marketing helps landscaping companies grow. Strategy, execution, and results.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Case Studies</span>',
        "kicker": "Case Studies",
        "h1": "The full story behind the growth.",
        "sub": "Detailed breakdowns of how we've helped landscaping companies build demand, convert leads, and grow revenue — from strategy to results."
    },
    {
        "path": "/book/",
        "title": "Free Book for Landscaping Company Owners",
        "meta": "Get your free copy of our book on marketing for landscaping companies. Strategy, systems, and growth — all in one place.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Free Book</span>',
        "kicker": "Free Book",
        "h1": "Everything we know about growing landscaping companies. Free.",
        "sub": "The playbook we've built from working with 50+ landscaping companies — strategy, systems, and growth tactics in one place."
    },
    {
        "path": "/podcast/",
        "title": "Mow Money, Mow Problems Podcast",
        "meta": "Listen to the Mow Money, Mow Problems podcast. Real conversations about growing landscaping companies.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Podcast</span>',
        "kicker": "Podcast",
        "h1": "Mow Money, Mow Problems.",
        "sub": "Real conversations with landscaping company owners about growth, operations, marketing, and the messy stuff nobody talks about."
    },
    {
        "path": "/tools/marketing-audit/",
        "title": "Free Marketing Audit Tool",
        "meta": "Get a free marketing audit for your landscaping company. See where you stand and what to fix first.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Marketing Audit</span>',
        "kicker": "Free Audit",
        "h1": "See where your marketing stands — in 60 seconds.",
        "sub": "A quick, honest assessment of your landscaping company's online presence. No email required, no sales pitch attached."
    },
    {
        "path": "/get-started/book-strategy-call/",
        "title": "Book a Free Strategy Call",
        "meta": "Book a free 30-minute strategy call with Lawn & Land Marketing. Get clarity on how to grow your landscaping company.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Book Strategy Call</span>',
        "kicker": "Get Started",
        "h1": "Book your free strategy call.",
        "sub": "30 minutes. No pitch, no pressure. Just clarity on what it takes to grow your landscaping company and dominate your market."
    },
    {
        "path": "/privacy-policy/",
        "title": "Privacy Policy",
        "meta": "Privacy policy for Lawn & Land Marketing website and services.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Privacy Policy</span>',
        "kicker": "Legal",
        "h1": "Privacy Policy",
        "sub": "How we collect, use, and protect your information."
    },
    {
        "path": "/terms/",
        "title": "Terms of Service",
        "meta": "Terms of service for Lawn & Land Marketing website and services.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Terms of Service</span>',
        "kicker": "Legal",
        "h1": "Terms of Service",
        "sub": "The terms that govern your use of our website and services."
    },
    {
        "path": "/pricing/",
        "title": "Pricing — Lawn & Land Marketing Programs",
        "meta": "See pricing for Lawn & Land Marketing's Growth and Authority programs. Transparent investment for landscaping companies.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Pricing</span>',
        "kicker": "Pricing",
        "h1": "Transparent pricing for landscaping companies.",
        "sub": "Two programs, clear investment levels, and no hidden fees. See exactly what you get and what it costs."
    },
    {
        "path": "/thank-you/",
        "title": "Thank You",
        "meta": "Thank you for reaching out to Lawn & Land Marketing. We'll be in touch soon.",
        "crumbs": '<a href="/">Home</a><span>/</span><span>Thank You</span>',
        "kicker": "Confirmed",
        "h1": "You're in. We'll be in touch soon.",
        "sub": "Thanks for reaching out. One of our team members will follow up with you shortly to get the conversation started."
    },
]

# Build all pages
created = 0
skipped = 0
for page in pages:
    path = page["path"]
    file_path = f"{REPO}{path}index.html"
    
    # Skip the reference page
    if path == "/programs/":
        print(f"SKIP (reference): {path}")
        skipped += 1
        continue
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    html = build_page(path, page["title"], page["meta"], page["crumbs"], page["kicker"], page["h1"], page["sub"])
    
    with open(file_path, 'w') as f:
        f.write(html)
    
    print(f"BUILT: {path}")
    created += 1

print(f"\n✅ Done! Created {created} pages, skipped {skipped}")
