# Agent economics draft

Status: first full draft, 2026-09-06, ready for the operator's read. Unpublished.
Issue: `_web_ops-agent-economics-2rg`.

## Read this first

[Post](post.md): **You Can Parallelize Agents. You Cannot Parallelize the Engineer.**

About 1,500 words. The title is the operator's line from `seed.md`. The article
follows the original question: can cheaper models plus more agents recover the
value of a stronger model when one person still specifies and reviews the work?

The narrative moves from the attention allowance created by a cheaper run, to
automated retries, to imperfect checking, to the operator's capacity limit.
Named models appear as dated price examples. The main argument applies across
providers. No task quality or productivity measurements are invented.

## Supporting material

- [Claims and calculations](claims-and-calculations.md): source paths, rate card,
  derivations, claim limits, and a plain-language glossary for the original model.
- [Arithmetic audit](verify_calculations.py): standard-library script that checks
  the actual Markdown table values and the worked examples.

Run from the repository root:

```bash
python3 -B drafts/agent-economics/verify_calculations.py
```

Observed: 11 named checks passed. Three additional in-memory mutations were
rejected: an incorrect saving, an insufficient agent count, and an incorrect
accepted-defect percentage. No API calls, model runs, or source-file edits occur
when the audit runs. This is arithmetic validation, not proof of the assumptions.

## Editorial review

These are sequential persona passes in one session, not independent agents or
an external research review.

**Dana, direction.** Question arc, practitioner audience. Keep the seed's framing
and explain the trade rather than ranking models. A normalized $5 task makes the
comparison easier to follow than the synthetic token profiles. The Verification
Design incident remains a separate possible follow-up.

**Nora, structure and edit.** Opening follows the operator's supplied research
question. Each section advances the calculation. The draft includes the case for
cheaper models, the value of a larger savings allowance, and the limits of ideal
retries. The ending identifies the next measurement rather than repeating a
takeaway list. A tightening pass reduced the opening and repeated qualifications.

**Dee, voice and readability.** Reviewed against the memory-hole, prompt-injection,
cross-model-review, cold-critic, and blog-index title patterns. The title comes
from the seed and has no parenthetical. Two small tables carry the main numerical
comparisons. Rho is explained where introduced; the complete symbol glossary is
in the supporting notes. No em dashes or local filesystem paths occur in the post.
The build will need responsive overflow and proper table headers for the five-column
capacity table.

**Grace, claims.** Rechecked official pricing and the linked prior experiment.
The arithmetic audit passes, including checks that deliberately wrong values
fail. The first table uses total-task token costs; the retry example explicitly
uses per-attempt costs. The 4.1% example concerns defects among accepted outputs,
not all attempts. Capacity assumes 24-hour agents and comparable accepted quality.
The structural sweep is not presented as a benchmark or a money-optimal policy.
Front matter remains `published: false`; Markdown formatting is clean. Browser
accessibility and deployment checks do not apply to this draft-stage artifact.

**Dana, final draft read.** The article answers the starting question and preserves
the counterargument: more cheap agents can cover machine work when checks keep
human effort low. The user should now be able to judge the article's voice and
depth from a complete piece.

## Proposed listing copy

Slug: `agent-economics`.

Blurb / meta description candidate:

> A cheaper AI run buys a small allowance for extra review. The math changes when retries stay automated and one engineer becomes the bottleneck.

Byline at build: The Skills Team.

## Next stage

Operator read and revisions, then release preparation if requested: HTML, hero
image, canonical URL and social metadata, blog/home listings, sitemap, SEO and
accessibility checks, and the final publication read. No site files or crosspost
payloads were changed during drafting. Recheck named prices at release time.
