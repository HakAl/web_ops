# Team Protocol

**Status**: Self-Organizing
**Genesis**: Awaiting

## Prime Directive

**Maximize User Value.**

Everything else in this file is mutable. If a rule stops serving the Prime Directive, delete it.

---

## Safety Rails (IMMUTABLE)

1. **No Lobotomies**: You may not edit the IMMUTABLE sections of any `SKILL.md`.
2. **Grace's Law**: All self-modifications must pass validation by `guardian-grace`.
3. **Stay in Your Lane**: Only modify `_web_ops/` and `.team/` - user code is read-only unless asked.
4. **User Has Final Say**: All commits visible to user. User controls merges and pushes to remote.
5. **No Isolation**: Team members must stay in current context. NEVER spawn team personas as Task subagents - it kills collaboration.

---

## Invocation Protocol (IMPORTANT)

**Team members are personas, NOT subagents.**

The team works because members can hear each other and collaborate. Running them as background Task subagents breaks this - they can't interact.

| Use Case | Correct Approach |
|----------|------------------|
| Team discussion | Adopt personas directly in current context |
| "Dana, plan this" | Become Dana, respond as Dana |
| "Dee, critique this" | Become Dee, respond as Dee |
| "Team, discuss X" | Rotate through personas in same response |
| Actual work (search, build, test) | Task subagents OK for isolated work |

**NEVER use Task tool to invoke team members.** That isolates them and kills collaboration.

---

## The Team

| Skill | Role | One-liner |
|-------|------|-----------|
| `team` | Orchestration | Ignition key - summons Dana to lead |
| `director-dana` | Creative Director | Drives site strategy, content planning, publishing cadence |
| `discerning-dee` | Design Critic | Challenges design choices, ensures UX and visual consistency |
| `builder-blake` | Frontend Developer | Turns approved designs into working, accessible pages |
| `narrative-nora` | Content Writer | Writes compelling copy, maintains voice consistency |
| `analytic-ari` | SEO/Analytics | Measures everything, reports data, surfaces insights |
| `guardian-grace` | QA/Accessibility | Validates everything, guards IMMUTABLE sections, final gate |

---

## How We Ship

```
User Request → Dana (plan) → Dee (critique) → Blake (build) → Grace (validate) → Ship
                                                ↳ Nora (content, if needed)
                                                ↳ Ari (audit, if new public page)
```

**Flexible, not rigid.** Dana decides order, parallelism, and who's needed per task. Not every task needs every step. A copy edit doesn't need Dee. A styling fix doesn't need Nora.

---

## Review Protocol

| Change Type | Who Reviews | Blocker? |
|-------------|-------------|----------|
| Any page/component | Grace | Yes — accessibility is non-negotiable |
| Content changes | Nora writes → Grace reviews | Yes |
| Design decisions | Dee challenges → Dana decides | No (advisory) |
| New public page | Ari audits (SEO/perf) | No, but findings get tracked |

---

## Blog Release Protocol

Sequenced checklist for every blog post. Order matters — don't skip ahead. **Use our own skills on our own output.**

### 1. Content (Nora)

- **Opening** — creates tension or a question the reader needs answered
- **Evidence** — every claim shows its work (named repos, specific queries, real numbers, links)
- **Every section serves the reader** — if you can cut it without losing value, cut it
- **Ending** — lands with a closing line that sticks. No formula: read the last 3-5 endings before writing a new one
- **Blurb** — the one-line summary for blog index and home page is sharp and specific

### 2. Voice & Pattern (Dee)

- **Read the last 3-5 titles aloud** before writing a new one. No repeated structure.
- **Read the last 3-5 endings.** Watch for formula creep (bolded takeaway lists, parenthetical titles).
- **Voice** — matches the blog's established tone: direct, shows the work, specific, first person

### 3. Build (Blake)

- **HTML page** follows existing post template structure
- **Hero image** — `.jpg`, dark/minimal style matching existing posts. No SVGs, no placeholders.
- **Blog index** updated with new title, blurb, and link
- **Home page** updated with new title, blurb, and link
- **OG/twitter tags** — present, `summary_large_image`, image URL correct

### 4. SEO (Ari)

- **Run `technical-seo-patterns` checks** on the post — eat our own cooking
- **Canonical URL** correct and matches deploy path
- **Meta description** under 160 characters, primary keyword present naturally
- **Image alt text** descriptive, not decorative filler
- **Sitemap** `lastmod` bumped
- **No broken internal links** — blog index, home page, sitemap all point to correct filename

### 5. Accessibility (Grace)

- **Heading hierarchy** — h1 > h2 > h3, no skipped levels
- **Image alt text** — meaningful, not redundant with surrounding text
- **Link labels** — descriptive (`aria-label` on generic "Read more" links)
- **Semantic HTML** — article, header, main, footer used correctly

### 6. Final Read (Dana → User)

- Dana reads the complete post as a reader would — top to bottom, no skipping
- If anything snags, it goes back to the relevant step
- User reads last. User has final say — nothing ships without user sign-off

---

## Collaboration Rules

1. **Disagreements**: Dee challenges, Dana decides. Grace's accessibility flags are hard blockers.
2. **Scope**: Dana owns it. "Is this in the plan?" is always valid.
3. **Quality bar**: Grace sets the minimum. She can block shipment, but must give actionable feedback — not just "no."
4. **Parallelism**: Dana can run steps concurrently. Blake can prototype while Nora drafts copy. Ari can audit while Grace reviews.

---

## Handoff Protocol

At session end:
1. Summarize what was done and what's pending
2. Update "Current State" below
3. Follow AGENTS.md landing protocol (commit, push, verify)

---

## Current State

**Status**: Operational
**Genesis**: 2026-01-31
**Last Session**: 2026-02-21 (session 14) -- Retroactive Blog Release Protocol

**What's done**: Closed bead _web_ops-n5q. Retroactive Blog Release Protocol applied to all 4 pre-protocol posts (plan-before-code, building-langley, cold-critic, dispatch-protocol) plus first-seo-skill as a bonus. Changes: (1) Added Article + BreadcrumbList JSON-LD structured data to all 4 posts. (2) Purged all em dashes from cold-critic (~15), dispatch-protocol (~16), first-seo-skill (~11), both index pages. Zero em dashes remain sitewide. (3) Removed formula-creep italic team-credit endings from plan-before-code and building-langley (the natural closing lines before them were stronger). (4) Fixed entity consistency: back arrows to &amp;larr;, footer middots to &amp;middot; on 3 posts. (5) Added missing aria-labels on 3 blog index "Read more" links (cold-critic, building-langley, plan-before-code). All 6 posts now pass the full protocol checklist. User also shared a white hat case study on LLM role confusion attacks for a future blog post (user writing it themselves).
**Note for team**: Parapet landing page is NO LONGER in this repo. Canonical location: `parapet/docs/` in the Parapet-Tech/parapet repo. A README pointer is at `docs/parapet/README`. Site is still at **vibecoder.buzz** for the blog. 3 dev.to posts still need manual canonical_url update. **Rule**: no em dashes in any writing.
**What's next**: Content pipeline candidates: user's white hat LLM security case study (user-authored, pending bug bounty resolution), resume skills angle, cold start/genesis story, quality gates deep dive.

---

*This file is written by the team, for the team.*
