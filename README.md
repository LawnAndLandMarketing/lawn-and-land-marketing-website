# Lawn & Land Marketing Website

**Live site:** https://new.lawnlab.dev  
**Vercel project:** new-lawnlab-deploy  
**Auto-deploys:** Push to `main` → live in ~10 seconds

## How to Make Changes

1. Clone: `git clone https://github.com/LawnAndLandMarketing/lawn-and-land-marketing-website.git`
2. Edit any file (HTML, CSS, JS, images)
3. Commit and push to `main`
4. Site updates automatically via GitHub Actions → Vercel

## Structure

```
├── index.html              ← Homepage
├── assets/
│   ├── css/styles.css      ← Main stylesheet
│   ├── js/main.js          ← Main JavaScript
│   ├── images/             ← All images
│   └── logos/              ← SVG logos
├── about/                  ← About page
├── contact/                ← Contact page
├── programs/               ← Growth & Authority program pages
├── services/               ← Individual service pages
├── industries/             ← Industry-specific pages
├── case-studies/           ← Client case studies
├── resources/              ← Blog, guides, podcast
├── book/                   ← Mow Money book page
└── .github/workflows/      ← Auto-deploy config
```

## Rules

- **This repo is the single source of truth.** Never deploy via Vercel CLI directly.
- **Every change goes through git.** No exceptions.
- **Push to main = live.** There is no staging branch (yet).
- **Images go in `assets/images/`.** Logos in `assets/logos/`.
- **One CSS file:** `assets/css/styles.css` (plus page-specific CSS files).
