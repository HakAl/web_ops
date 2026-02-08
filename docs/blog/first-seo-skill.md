# We Searched the Agent Skills Ecosystem for SEO

We expected to find one. The Agent Skills ecosystem has skills for planning, critique, code review, testing, frontend design. Someone must have built the basics — crawlability, meta tags, structured data.

We searched every repository we could find, starting with the official catalog and working outward:

- **anthropics/skills** — Anthropic's official skills list
- **agentskills/agentskills** — open standard reference
- **skillmatic-ai/awesome-agent-skills** — community catalog
- **Prat011/awesome-llm-skills** — community catalog
- **Broad GitHub** — sickn33/antigravity-awesome-skills, vercel-labs/agent-skills, OneRedOak/claude-code-workflows, muratcankoylan/Agent-Skills-for-Context-Engineering

We tried every keyword we could think of: SEO, technical SEO, sitemap, robots, canonical, JSON-LD, structured data.

Zero results. Not "a few weak matches." Zero SKILL.md files. Zero coverage.

## The Gap Was Bigger Than SEO

That search was part of a larger audit. We needed skills for six web ops disciplines — content strategy, UX evaluation, CSS architecture, technical storytelling, SEO, and accessibility testing. We ran the same catalog search for each.

| Discipline | Best Match | Gap |
|---|---|---|
| Content strategy | A general writing partner — no strategy layer | High |
| UX evaluation | A design review workflow — no formal heuristics | High |
| CSS architecture | An aesthetics guide — no layout methodology | High |
| Technical storytelling | A generic writing assistant | High |
| **SEO** | **Nothing** | **Total** |
| Accessibility testing | One shallow checklist buried in a larger workflow | High |

Six disciplines. All six: build from scratch. The ecosystem is engineering-workflow heavy with virtually no web ops coverage. SEO was just the cleanest zero.

## Why This Matters

Our agents build web pages. They write HTML, scaffold components, generate sitemaps. Without an SEO skill in the loop, those pages ship without discoverability checks. No canonical URL validation. No structured data. No robots.txt guidance. No performance baselines.

A page can be valid HTML, pass accessibility checks, render correctly in every browser, and still never appear in a search result. That's not a bug anyone catches in code review.

## What We Built

Ari authored `technical-seo-patterns` — the first SEO skill in the ecosystem. It covers the technical baseline a shipping team needs:

- On-page essentials: titles, meta descriptions, heading hierarchy, image alt text
- Canonical URL strategy to avoid duplicate-content traps
- Robots and sitemap hygiene so crawlers can reach everything published
- Structured data patterns (JSON-LD) for rich results
- Core Web Vitals checkpoints so performance doesn't silently degrade

It's not a keyword playbook. It's the set of checks that prevent a published page from being invisible by default.

## One Skill, Bigger Pattern

The SEO gap was the sharpest signal, but the real finding is structural. The Agent Skills ecosystem was built by engineers for engineering problems. Content strategy, UX evaluation, CSS architecture, storytelling, accessibility — none of these have meaningful skill coverage.

We built the SEO skill because we needed it. The other five gaps are still open.
