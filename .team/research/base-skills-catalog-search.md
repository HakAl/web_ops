# Catalog Search: Base Skills for Web Ops Personas

**Bead**: _web_ops-eac
**Date**: 2026-01-31
**Purpose**: Library-first research per Engineering team pattern (_skills/.team/research/base-skills-catalog-search.md)

---

## Search Scope

Searched per protocol order:
1. anthropics/skills (official)
2. agentskills/agentskills (open standard reference)
3. skillmatic-ai/awesome-agent-skills (community)
4. Prat011/awesome-llm-skills (community)
5. Broad GitHub search (sickn33/antigravity-awesome-skills, vercel-labs/agent-skills, OneRedOak/claude-code-workflows, muratcankoylan/Agent-Skills-for-Context-Engineering)

---

## 1. Content Strategy / Editorial Planning (for Dana)

### What exists
- **Prat011/awesome-llm-skills/content-research-writer/SKILL.md** — Writing partner for outlining, research, hooks, section feedback. Covers blog posts, newsletters, tutorials. Per-piece assistance, no portfolio awareness.
- **anthropics/skills/doc-coauthoring/SKILL.md** (official) — 3-stage doc co-authoring workflow. Focused on specs/RFCs, not editorial content.
- **compound-engineering:every-style-editor** (installed plugin) — Copy editing mechanics, not strategy.

### Gap
No skill addresses editorial strategy as a discipline: content calendars, publishing cadence, audience segmentation, content pillar planning, topic sequencing, or editorial pipeline management.

### Decision
Build from scratch.

---

## 2. UX Heuristic Evaluation (for Dee)

### What exists
- **OneRedOak/claude-code-workflows/design-review/** — Comprehensive design review workflow with Playwright testing, triage matrix (Blocker/High/Medium/Nitpick). Covers interaction, responsiveness, visual polish, a11y, code health. Not a SKILL.md.
- **anthropics/skills/frontend-design/SKILL.md** (official) — Guidelines for *creating* interfaces. Building skill, not evaluation.
- **vercel-labs/agent-skills/web-design-guidelines/SKILL.md** — Thin wrapper fetching Vercel's guidelines. Audit-focused.

### Gap
No skill implements structured heuristic evaluation: Nielsen's 10 heuristics applied systematically, Gestalt principles as analytical lens, severity rating scales, or formalized usability inspection process.

### Decision
Build from scratch. Reference OneRedOak's phase-based structure and triage matrix.

---

## 3. Responsive Layout / CSS Architecture (for Blake)

### What exists
- **anthropics/skills/frontend-design/SKILL.md** (official) — Spatial composition, typography, color, motion. Aesthetics focus.
- **OneRedOak/design-review/design-principles-example.md** — CSS/Styling Architecture section: utility-first, BEM+Sass, CSS-in-JS. Responsive grid, spacing scale, design tokens. A checklist, not a skill.

### Gap
No skill covers CSS architecture systematically: custom property systems, fluid typography with `clamp()`, container queries, logical properties, modern layout patterns (subgrid, `aspect-ratio`), responsive methodology, progressive enhancement strategies.

### Decision
Build from scratch.

---

## 4. Technical Storytelling (for Nora)

### What exists
- **Prat011/awesome-llm-skills/content-research-writer/SKILL.md** — General writing partner. Blog posts, articles, tutorials. No technical content focus.
- **anthropics/skills/doc-coauthoring/SKILL.md** (official) — Internal docs workflow (PRDs, specs, RFCs).
- **anthropics/skills/brand-guidelines/SKILL.md** (official) — Brand voice consistency, not narrative craft.

### Gap
No skill addresses technical storytelling: narrative arc for technical content, the "so what" bridge, developer blog conventions, progressive disclosure of complexity, making technical work compelling.

### Decision
Build from scratch. Reference content-research-writer's workflow structure (outline -> draft -> feedback -> refine).

---

## 5. Technical SEO (for Ari)

### What exists
- **Nothing.** Zero SKILL.md files found for SEO across all repos searched. Every query variation returned zero results.

### Gap
Complete gap. Technical SEO is entirely absent from the Agent Skills ecosystem. No coverage of: on-page SEO, meta tags, structured data/JSON-LD, crawl optimization, robots.txt/sitemap, Core Web Vitals, canonical URLs, indexing diagnostics.

### Decision
Build from scratch. Greenfield domain.

---

## 6. Accessibility Testing Methodology (for Grace)

### What exists
- **OneRedOak/design-review/design-review-agent.md** — Phase 4 covers a11y (WCAG 2.1 AA): keyboard nav, focus states, semantic HTML, form labels, alt text, contrast. One phase of broader review, not dedicated.
- **anthropics/skills/webapp-testing/SKILL.md** (official) — Playwright-based functional testing. No a11y methodology.

### Gap
No dedicated accessibility testing methodology: WCAG 2.1/2.2 testing procedures, screen reader testing workflows (NVDA, VoiceOver), automated auditing (axe-core, Lighthouse, pa11y), keyboard-only testing protocols, ARIA validation, focus management testing.

### Decision
Build from scratch. Reference OneRedOak Phase 4 for basics.

---

## Summary

| Skill | Closest Existing | Gap | Approach |
|-------|-----------------|-----|----------|
| Dana: content-strategy-patterns | content-research-writer (writing only) | High — no strategy layer | Build from scratch |
| Dee: ux-heuristic-evaluation | OneRedOak design-review (workflow) | High — no formal heuristics | Build from scratch |
| Blake: responsive-layout-patterns | frontend-design (aesthetics only) | High — no CSS architecture | Build from scratch |
| Nora: technical-storytelling | content-research-writer (generic) | High — no technical narrative | Build from scratch |
| Ari: technical-seo-patterns | Nothing | Total — zero ecosystem coverage | Build from scratch |
| Grace: accessibility-testing-methodology | OneRedOak Phase 4 (shallow) | High — no dedicated methodology | Build from scratch |

**Bottom line**: All six build from scratch. The Agent Skills ecosystem is engineering-workflow heavy with virtually no web ops coverage.
