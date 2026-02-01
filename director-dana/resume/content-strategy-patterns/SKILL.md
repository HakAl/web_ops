---
name: content-strategy-patterns
description: >
  Editorial decision frameworks for content planning. How to choose topics, set
  publishing cadence, sequence content for audience growth, and run a content
  pipeline that ships consistently. Practitioner patterns, not marketing theory.
metadata:
  author: director-dana
  version: "1.0"
  created: "2026-02-01"
---

# Content Strategy Patterns

## Topic Selection

Not every idea is an article. The wrong topic wastes the writer's time and the reader's attention.

### The Three-Filter Test

Every topic candidate passes through three filters:

1. **Do we have something to say?** Not "do we know about this" — do we have a perspective, a result, a failure, or an insight that isn't already widely published? If the article could be written by anyone with Google access, it's not worth writing.

2. **Does the audience care?** The topic must solve a problem, answer a question, or challenge an assumption the reader actually has. "We used Maildir for inter-agent messaging" fails. "Our AI teams couldn't talk to each other" passes.

3. **Can we show the work?** Technical audiences trust evidence over claims. If we can't include specifics — data, code, research, before/after — the topic isn't ready. Bank it for later when we have the evidence.

A topic that fails any filter gets shelved, not killed. Circumstances change.

### Topic Sources (Ranked by Quality)

| Source | Why it works | Example |
|--------|-------------|---------|
| Something that broke | Readers identify with failure. Authentic. | "200 lines of garbage" scraper post |
| A question we couldn't answer | Curiosity is contagious. Investigation stories. | "Is our critic actually critiquing?" |
| A decision we had to defend | Forces clear reasoning. Shows tradeoffs. | "GitHub Pages vs dev.to as canonical" |
| Something we built | Build logs work when the decisions are interesting. | Dispatch protocol design |
| A pattern we noticed | Synthesis across experiences. Higher abstraction. | Plan-before-code workflow |

Bottom of the list: things we want to promote, company announcements, "thought leadership" pieces with no evidence. These have a place (release notes, changelogs) but they're not articles.

### The Backlog

Maintain a list of topic candidates with status:

- **Raw** — idea captured, not yet filtered
- **Filtered** — passed the three-filter test, has a one-sentence angle
- **Outlined** — narrative structure drafted, ready for a writer
- **Assigned** — writer is working on it
- **Review** — draft complete, in review pipeline

The backlog is not a queue. It's a menu. The next article to write is the one with the most momentum — the freshest evidence, the hottest insight, the writer who's excited about it.

## Publishing Cadence

### The Consistency Rule

A predictable rhythm matters more than volume. One article per month, reliably, beats three in January and none until April.

### Choosing the Rhythm

| Team size | Realistic cadence | Why |
|-----------|------------------|-----|
| 1 writer | Biweekly to monthly | Anything faster burns out or drops quality |
| 2-3 writers | Weekly to biweekly | Rotation prevents burnout, maintains voice |
| Content team (4+) | 2-3x per week | Needs an editor to maintain voice consistency |

Start slower than you think you should. Increase when the pipeline feels easy, not when you feel ambitious. Ambition creates a burst. Pipeline creates a cadence.

### Cadence Killers

- **Perfectionism** — "It's not ready yet" for the fifth week. Ship it. Publish and iterate.
- **Scope creep** — a 1,500 word article becoming a 5,000 word guide. Split it.
- **Approval bottlenecks** — if one person gates every publish, they're the throughput limiter. Distribute review or accept the cadence that one reviewer can sustain.
- **No backlog** — when you finish an article and have nothing queued, you start from zero. The backlog is the cadence engine.

## Content Sequencing

### The Momentum Principle

Content builds on itself. Each piece should make the next piece easier to write and easier for readers to find.

### Sequencing Patterns

**Foundation first**: establish what you do before explaining how you do it. The blog's first article should answer "who are these people and why should I care?" Everything after builds on that foundation.

**Alternate depth levels**: a deep technical dive followed by another deep dive loses casual readers. Alternate between accessible pieces (the story, the insight) and practitioner pieces (the implementation, the code).

**Reference forward**: when writing about topic A, mention that topic B exists. "We'll cover the dispatch protocol in a future post" creates anticipation and gives readers a reason to return.

**Don't repeat context**: if a previous article explained the team structure, link to it. Don't re-explain. Readers who need context can follow the link. Readers who don't shouldn't be forced through it again.

### The Content Map

Think of published content as a graph, not a list:

- **Entry points** — articles that make sense to a first-time reader. These need the most context, the broadest appeal, and the clearest "so what."
- **Deep dives** — articles that assume familiarity. These can use more jargon and go deeper because the entry points did the onboarding.
- **Connectors** — articles that link topics. "How X led us to Y" bridges different content areas.

Every new article should have at least one link to an existing article. Orphan content doesn't build a body of work — it builds a pile.

## Cross-Posting Strategy

### Canonical Source vs Distribution

Decide once, apply everywhere:

- **Canonical source** — the authoritative URL. Where you control the content permanently. Where SEO equity accumulates.
- **Distribution channels** — platforms where content gets discovered. Dev.to, Medium, Hashnode, LinkedIn. These drive traffic to the canonical source.

### Cross-Post Rules

1. **Publish canonical first** — the original URL must exist before the cross-post goes up.
2. **Set canonical_url** — every cross-post must declare the canonical URL. Without it, search engines see duplicate content.
3. **Same content, not same formatting** — adapt to platform conventions (dev.to frontmatter, Medium formatting) but don't change the substance.
4. **Link back** — cross-posts should link to the canonical source at least once. Footer link is minimum.
5. **Don't depend on platforms** — any platform can change terms, throttle distribution, or shut down. The canonical source is the insurance policy.

## Pipeline Management

### The Weekly Check

Every week, answer three questions:

1. **What's publishing this week?** — if the answer is "nothing," that's information. Adjust cadence or unblock the pipeline.
2. **What's in review?** — review is where articles die. If something has been in review for more than one cycle, it's blocked. Unblock it or shelve it.
3. **What's in the backlog?** — if the backlog is empty, schedule a brainstorm. If it's overflowing, filter harder.

### Pipeline Anti-Patterns

- **Infinite draft** — an article that's been "almost done" for weeks. Set a deadline. Ship or shelve.
- **Review as rewrite** — the reviewer rewrites instead of giving feedback. That's a voice inconsistency problem, not a review problem. Fix the style guide.
- **Writer's block as strategy** — waiting for inspiration instead of working the backlog. Inspiration follows from working, not the reverse.
- **Publishing without promotion** — writing an article and not sharing it anywhere is the same as not writing it. Every publish gets a distribution plan, even if it's just "post the link in three places."

## The Strategy Check

Before committing to a content direction, run this:

1. **Audience test**: can you name the person who reads this? Not a demographic — a person with a specific problem.
2. **Differentiation test**: what can we say that others can't? (Our unique experience, data, failures, systems.)
3. **Sustainability test**: can we maintain this at the planned cadence for six months?
4. **Evidence test**: do we have enough real material (projects, data, decisions) to support this direction?
5. **Sequence test**: do the first three articles build on each other?
