# Deployment & Infrastructure — Source of Truth

> **Read this before touching deploys, Vercel, domains, or the publish pipeline.**
> Last verified live: 2026-07-18. If reality and this doc disagree, fix the doc in the same commit.

## The one-paragraph version

Push to `main` on **lawnHQ/lawn-and-land-marketing-website** → two deploys fire: Vercel's GitHub integration AND the Actions workflow (`.github/workflows/deploy.yml`), both targeting the **production project `lawnland-site`**. Production domain: **lawnandlandmarketing.com**. After every deploy, **verify the change on the live domain** — never trust a green check alone.

## Vercel projects (team `lawn-and-land-marketing`, ID `team_sPQaPdEOVQaR42djHV2cTm51`)

| Project | ID | Serves | Role |
|---|---|---|---|
| **`lawnland-site`** | `prj_JKvED0gkEFd1PEHj2jGhX5Yiro9O` | **lawnandlandmarketing.com** | **PRODUCTION — the only project that matters for the live site** |
| `new-lawnlab-deploy` | `prj_YtCgrRYudSseihUZHkHsKvOrXC6R` | new.lawnlab.dev | Old pre-launch staging. Still auto-deploys from `main` (harmless mirror). Do NOT point tooling at it. |
| `lawn-and-land-marketing-website`, `lawnlab-dev`, `lawn-land-site`, … | — | — | Historical/abandoned explorations. Ignore. |

**GitHub:** the repo lives in the **`lawnHQ`** org (migrated from `LawnAndLandMarketing`, July 2026). Old-org remotes still push via redirect; update remotes when convenient.

## How a deploy actually happens

1. **Vercel git integration** on `lawnland-site`: builds every push to `main` automatically.
2. **GitHub Actions** (`deploy.yml`): runs `build.py --check` + `check_links.py` gates, then `vercel deploy --prebuilt --prod` **to `lawnland-site`** (`VERCEL_PROJECT_ID` in the workflow env; `VERCEL_TOKEN` is a repo Actions secret).

They're redundant on purpose. **History lesson (2026-07-18):** the git-integration webhook silently skipped one commit — deployment READY, homepage a commit behind, no error anywhere. Until that day, `deploy.yml` pointed at the *staging* project, so there was no backstop. Both paths now target production.

### The iron rule: verify on the domain

A "successful" deploy is a claim, not a fact. After every deploy, curl the live domain for a marker you just shipped:

```bash
curl -s "https://lawnandlandmarketing.com/<changed-path>" | grep -c "<something-new-on-that-page>"
```

Notes: the edge cache can serve `/` stale for ~15+ min (`x-vercel-cache: HIT`, query-string busting does NOT work on static routes) — but if a *new* path or `/index.html` also lacks your change, it's not cache: the deployment content is wrong or production never deployed. Check `lawnland-site`'s latest deployment sha vs your commit before debugging anything else.

## Tokens & access (for agents)

- **Local `vercel` CLI:** project and deployment read access was verified 2026-07-30. Production writes
  still go through the GitHub `main` pipeline described above; do not bypass it with an ad hoc CLI deploy.
- **`~/.github_token`**: classic PAT, `repo` scope only — no `workflow` scope (can't push workflow-file changes over HTTPS; **push via SSH**, which auths as the org) and no `read:org` (use `GH_TOKEN=$(cat ~/.github_token) gh …`, not `gh auth login`).

## Publishing an article — the checklist (every item, same commit)

The 2026-07-18 cornerstone shipped with the sitemap forgotten. Never again:

1. Article page: `resources/blog/<slug>/index.html` (clone the newest article's structure).
2. `_blog.json` entry (newest first) — image path + alt; `gen_blog.py` stamps the article hero, blog index, category hubs, author hub, **and the homepage latest-3 section**.
3. **`sitemap.xml` — HAND-MAINTAINED.** Add the URL yourself (`priority 0.6`, today's `lastmod`).
4. Schema on the page: BlogPosting (incl. `wordCount`, `articleSection`, `keywords`) + FAQPage + **BreadcrumbList** (not in the old template — copy from the land-clearing guide).
5. `og:image` / `twitter:image` + **correct** `og:image:width/height` and hero `<img>` width/height. Gotcha: `gen_blog.py` re-stamps article heroes with default `1200x630` attrs — re-fix after any gen run.
6. Internal links FROM the relevant service/industry pages TO the article (the cluster matters).
7. **External links to third parties (competitors especially): `rel="noopener nofollow"`** — never pass equity to sites competing on our terms. Internal links stay followed.
8. Images: WebP only (`cwebp -q 82`), real dimensions, lazy-load below the fold.
9. `python3 gen_blog.py && python3 build.py && python3 build.py --check && python3 scripts/check_links.py` — all green before commit.
10. Push → **verify on the live domain** (iron rule above) → owner submits the URL in Search Console (URL Inspection → Request Indexing).

## Related systems

- **Homepage "Latest Playbooks" section**: auto-stamped by `gen_blog.py` between `HOME-BLOG:START/END` markers in `index.html`. Edit the shell freely; never hand-edit between the markers.
- **Competitor Radar** (`lawnHQ/competitor-intel`): tracks our rankings + competitors daily; its autonomous operator opens content PRs against this repo. Its docs: that repo's `README/AGENTS/PLAYBOOK`.
- **Client sites**: separate Vercel projects per client (`client-site-*`). Same iron rule applies — verify on the client's live domain after deploy.
