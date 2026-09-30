# Agent economics draft

Status: approved by the operator for publication on 2026-09-30. Release built and validated; deployment verification follows the push.
Issue: `_web_ops-agent-economics-2rg`.

## September 30 release

Public URL: https://vibecoder.buzz/blog/agent-economics.html

The final operator-edited CI example and introduction are preserved. The published
Markdown body and rendered HTML text match the saved draft. The draft's
`published: false` remains an archive flag; the copy in `docs/blog/` is marked
published and includes canonical and cover metadata.

Built the HTML page, 1600x800 JPEG cover, public Markdown copy, home/blog cards,
and sitemap entry. Native disclosure keeps the pricing note optional. Its table
and formula support keyboard scrolling on small screens. Links in article text
are underlined.

Checks completed:

- Six arithmetic/hygiene checks and `git diff --check`.
- Chromium at 1280, 390, and 320 pixels: disclosure toggles with Enter and Space,
  mobile table scrolls with the keyboard, no page overflow, no JavaScript errors.
- Axe WCAG A/AA checks: zero violations in all three viewports with the note open.
- Desktop and mobile screenshots inspected. No manual screen-reader test.
- Article/Markdown text parity; all local links and assets on the article,
  home page, and blog index; canonical, social metadata, image dimensions,
  156-character description, and local Article/BreadcrumbList JSON-LD checks.
- Official named-model prices were rechecked earlier in this session.

The full approved title is retained even though it exceeds the SEO skill's
suggested 60-character title length. Core Web Vitals require production data;
no field-performance claim is made. Automatic approval review rejected uploading
unpublished HTML to Schema.org as an external disclosure. Local structured-data
checks were used; external validator approval is not claimed.

Hero: `docs/blog/agent-economics.jpg`, generated with the built-in imagegen tool,
then resized/exported to JPEG (1600x800, 236,908 bytes). Exact prompt:

> Use case: stylized-concept. Asset: wide editorial blog hero, 1600x800 landscape composition. Concept: many parallel AI work streams converge on one human reviewer. Minimal, sophisticated editorial illustration on very dark charcoal-purple background (#13111a), restrained muted cyan and coral-red accents, subtle paper grain and soft lighting. Several thin cyan lanes carrying small completed document cards flow from the left toward a single small human seated at a desk on the right; the cards collect in a modest pile before the desk. The human attention bottleneck is visually clear, thoughtful rather than frantic. Lots of negative space, simple architectural geometry, no robots, no brains, no circuit-board clichés, no charts, no text, no letters, no numbers, no logos, no watermarks. All key content within center 85% of image.

## Read this first

[Post](post.md): **You Can Parallelize Agents. You Cannot Parallelize the Engineer.**

About 670 words in the main article, plus a roughly 400-word optional note. The title is the operator's line from `seed.md`. The article
follows the original question: can cheaper models plus more agents recover the
value of a stronger model when one person still specifies and reviews the work?

The narrative moves from the attention allowance created by a cheaper run, to
automated retries, to imperfect checking, to the operator's capacity limit.
Named models appear as dated price examples in the optional note. The main argument applies across
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

The current audit passed all six named checks on September 30. The September 6 audit covered 11;
retry-probability and capacity-table checks were removed with those examples.
The historical run also rejected incorrect saving, slot-count, and defect-rate
mutations. No API calls, model runs, or source-file edits occur
when the audit runs. This is arithmetic validation, not proof of the assumptions.

## September 30 voice pass

Operator requested a looser voice after supplying a new introduction. Preserved
that introduction verbatim. Edited the main body for everyday wording and
contractions, keeping the dollar example, imagined broken-link scenario,
waiting-changes-sides paragraph, and final sentence. The optional pricing note
is unchanged. This was a voice edit, not a fresh claim or pricing review. Six
existing arithmetic/hygiene checks pass; rendered disclosure behavior is still
a release-stage check. Local and uncommitted.

## September 30 structural edit

Applied the operator-accepted review with a cuts-and-moves pass. The opening now
connects parallel agents to the attention each result requires. Kept the operator's
opening question and "Token spend down. Total cost up." The dollars-to-minutes
example remains in the main article. Moved the formula, model table, pricing
sources, qualifications, and larger-task comparison into an optional `details`
note after the narrative. Replaced the experiment paragraph with a supporting
link in that note. Kept the retry example, waiting-changes-sides paragraph, and
narrative's final sentence. No new anecdote or claim of measured results.

The six arithmetic/hygiene checks still cover the article and its note together.
The disclosure markup needs rendered validation during HTML release preparation;
this edit validates the source only. Changes remain local and uncommitted.

## September 30 first revision

Nora edit: incorporated the operator's opening markup, repaired sentence breaks,
and kept "Token spend down. Total cost up." Changed the hypothetical model's
purpose from measuring an optimum to exploring when a strategy pays off; the
assumed inputs cannot establish an optimal real-world workflow. Used the value
of the reader's time instead of presenting $100/hour as a typical salary.

Added official pricing citations at first mention and refreshed the check date
below the table. Rates for the named models are unchanged. Terra's model page
now supplies a direct citation because its row is absent from the pricing-page
extract. The comparisons remain explicitly dated API examples.

Replaced the probability examples, rho section, and capacity table with an
imagined broken-link retry and the point where agents begin waiting for review.
The calculations remain in the evidence record as historical background.

Grace content review is a same-session check of the revised text, source support,
remaining arithmetic, and Markdown hygiene. No rendered-page or release checks
are implied by this draft edit.

## September 6 editorial review (historical)

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
