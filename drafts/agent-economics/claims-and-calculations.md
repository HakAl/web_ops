# Agent economics: claims and calculations

Draft revision and pricing recheck: 2026-09-30. This is an editorial evidence record, not a benchmark.
Run `python3 drafts/agent-economics/verify_calculations.py` from the repository root
to check the draft's numerical tables and worked examples.

## Sources and provenance

- Operator's question and title framing: `/Users/home/dev/cost/seed.md`.
- Decision framework and simple capacity model: `/Users/home/dev/cost/cost.md`.
- Corrected task calculations and model explanations: `/Users/home/dev/cost/answers.md`.
- Structural sweep: `/Users/home/dev/cost/answers.py` and `layer2.py`.
- [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing),
  standard Opus 5 and Sonnet 5 rows, rechecked 2026-09-30.
- [OpenAI pricing](https://developers.openai.com/api/docs/pricing),
  standard short-context Sol row, rechecked 2026-09-30.
- [GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra),
  input, cached input, output, and 1.25x cache-write rate, rechecked 2026-09-30.
  The current pricing-page extract does not expose Terra in its main table;
  the model page supplies the rates directly.
- [Cross-model review experiment](https://vibecoder.buzz/blog/cross-model-review.html),
  also read from `docs/blog/cross-model-review.md`. The new draft links only its
  reported regex-compilation finding. It does not repeat that post's research
  statistics or claims about current free-tier availability.

Prices below are USD per million tokens. Cache write uses the five-minute rate
for Anthropic. Sol's promotional pricing is listed as available at least through
2026-11-21. Recheck before publication if the date changes materially.

| Model | Fresh input | Cache read | Cache write | Output |
| --- | --- | --- | --- | --- |
| Opus 5 | 5.00 | 0.50 | 6.25 | 25.00 |
| Sonnet 5 | 2.00 | 0.20 | 2.50 | 10.00 |
| GPT-5.6 Sol | 4.00 | 0.40 | 5.00 | 20.00 |
| GPT-5.6 Terra | 2.00 | 0.20 | 2.50 | 12.00 |

The article normalizes high-tier task spend to $5. It does not assert that $5 is
an observed average. The earlier synthetic medium-task example remains $1.75 /
$0.70 for Opus/Sonnet and $1.40 / $0.78 for Sol/Terra in the source material;
those different task amounts are not used in the article.

## Release note

The operator completed their own whole-post edit and authorized publication on
September 30. The public copy preserves that wording. The opening generalization
about cheaper models making more mistakes is the operator's framing, not a result
established by the hypothetical model. The cost and throughput examples do not
measure named-model quality. The CI scenario remains hypothetical.

## Current revision

The September 30 edit keeps the opening attention calculation, four pricing rows,
and doubled-token examples. Official rates still match the snapshot below the
source list. The optional note after the main narrative cites those sources and dates the
recheck beneath the table. The formula, pricing rows, doubled-token examples,
and larger-task comparison now live in that note; the main text keeps the
$3-to-1.8-minutes example. These remain examples for the named models, not a claim that
those models are the latest releases.

From "Retries can be a good trade" onward, the article now uses a clearly
imagined CI-repair scenario. It makes no claim that this workflow was measured.
The earlier cross-model review is now a supporting link in the optional note.
Its local source was reread for the text-matching rule that could not compile.

The only numerical capacity claim left in the article is proportional: twice the
attention per task means half as many tasks in a fixed amount of available time.
It assumes comparable tasks and that human time is the limiting resource.

The retry probabilities, accepted-error percentage, rho explanation, and slot
counts are removed from the public-facing draft. Their derivations remain in the
historical register below for provenance. The audit no longer requires those
removed examples; it checks the current pricing table and opening arithmetic.
Six named checks cover four pricing rows, attention/doubled-token examples, and
draft publication/hygiene markers. This is not a prose or empirical-validity test.

## Historical claim register from the September 6 draft

| Claim in the draft | Evidence or derivation | Classification and limit |
| --- | --- | --- |
| The opening investigation and title | User's seed and the generated sweeps | Operator-provided context; no invented run results or claim of an observed production improvement |
| $3 buys 1.8 minutes at $100/hour; two minutes costs $3.33 | `3 * 60 / 100`; `2 * 100 / 60` | Exact arithmetic with an illustrative hourly value |
| Sonnet costs 40% across the selected categories | Divide each Sonnet rate by the paired Opus rate | Sourced price ratio, not a relative-capability claim |
| Terra costs 50% for input/cache and 60% for output | Divide each Terra rate by the paired Sol rate | Sourced price ratios; weighted task ratio lies between them |
| All four saving and attention rows | `saving = 5 * (1 - ratio * multiplier)`; `seconds = saving * 3600 / 100` | Calculated bounds; category mix is held fixed as token use grows |
| Doubling Sonnet tokens leaves $1; Terra saves $0 to minus $1 | Same formula at multiplier 2 | Assumes total task tokens, standard service, no unmodeled fees or discounts |
| $50 gives ten times the allowance of $5 | The saving is linear in high-tier spend with the other inputs fixed | Conditional arithmetic; no claim that larger tasks need proportionally less review |
| Retry costs are about $5.56 and $2.86 | `5 / .9`; `2 / .7` | Hypothetical per-attempt costs including the check, constant success probability, independent retries, perfect verifier, no retry cap |
| A 90% catch rate leaves about 4.1% wrong among accepted outputs | `(.30 * .10) / (.70 + .30 * .10)` | Assumes 70% attempt correctness and no false rejection of good output; also the eventual accepted-error rate under independent retries |
| A stricter score threshold can reject good work as well as bad | `layer2.gate_stats`, pass threshold applied to correlated quality/check scores | Structural model interpretation; not an empirical test-coverage percentage |
| Rho is score/quality correlation, separate from human review | `TaskClass.rho`, `gate_stats`, and `pipeline` in `layer2.py` | Correlation conditional on fixed task difficulty; do not label it an error-catch rate |
| The sweep maximizes good tasks/day and counts operator repair time | `answers._best`: capacity times `1 - P_esc`; `pipeline.a` includes expected repair | Finite search; no money budget or defect-rate constraint in this objective |
| A previous review exposed a regex that could not compile | Existing project's cross-model-review post, "The crash" | Reported project observation; no new reproduction claimed |
| 384 productive minutes/day | `8 * 60 * .8` | Invented operator workday |
| Human ceilings 76.8 and 38.4 tasks/day | `384 / 5`; `384 / 10` | Average steady-state capacities, not daily feature forecasts |
| Slot counts 4, 7, and 4 | `ceil(human_ceiling * machine_minutes / 1440)` | Average capacity with 24-hour slots, sufficient work, comparable accepted quality assumed |
| Seven slots cannot restore throughput when human time doubles | Agent capacity exceeds the reduced human ceiling; the minimum still equals 38.4 | Conditional bottleneck argument, not measured scaling behavior |
| A cheaper model may be worth trying where checks/retries avoid extra attention | Synthesis of the cost, retry, and capacity examples | Editorial decision framework; requires workflow measurements |

## Background: what the structural model assumes

The simple three-row capacity table is derived from `cost.md`. It is not output
from the more elaborate `layer2` sweep. The September 6 draft kept that distinction by
calling the rows hypothetical workflows and stating their inputs in full. The
September 30 revision removes that table from the article.

The structural sweep additionally assumes a distribution of task difficulty,
review effectiveness, specification effort, and later repair effort. It treats
retries as independent conditional on task difficulty. It searches a finite set
of checking thresholds and review durations, excluding policies needing more
than eight attempts on average. That is not a hard eight-attempt limit per task.

Its latent capability difference is measured in units of the model's quality
spread, called sigma. It is not a percentage degradation. Rho controls how
informative the automated score is; the gate threshold decides which scores
pass. Human review then gets its own opportunity to catch a defect.

| Symbol in the source | Human meaning |
| --- | --- |
| `mu`, `theta`, `sigma_theta` | Model capability, typical task difficulty, and variation in difficulty |
| `gap` | Hypothetical reduction in capability relative to the baseline |
| `rho` | How closely the automated score tracks true quality at a fixed difficulty |
| `s` | Score required to pass the automated check |
| `m`, `tau` | Review minutes per presented artifact and the assumed effectiveness of that review time |
| `g` in layer2 | Chance human review catches an incorrect artifact |
| `A`, `E_cyc` | Average attempts and review rounds per finished task |
| `P_esc` | Chance a defect survives the acceptance process |
| `a` or `h` | Human minutes per task, including expected later repair |
| `T` or `t` | Machine minutes per task, including retries |
| `W` | Concurrent agent slots |

No structural-sweep cell, sigma value, or optimal agent count is promoted to a
claim about a named model. The original capacity examples assume comparable
accepted quality; the sweep instead discounts output for escaped defects.
Matching throughput therefore cannot stand in for matching quality or total cost.

## Review and release boundaries

- Arithmetic audit compares computed values against the actual Markdown rows.
  It also checks that the worked-example values and scope statements remain in
  the draft. It cannot validate an empirical assumption or the prose's entire meaning.
- Named model prices are sourced; task costs, hourly value, and the CI-repair
  scenario are hypothetical. No real-world reliability improvement is claimed.
- No actual work history is invented. The first-person investigation follows the
  operator's seed; desired future measurements are framed as future work.
- The title comes directly from the operator's seed.
- Content and claim review occurs through personas in this same session. This
  is not an independent model-family review or external research approval.
- User read and any revisions precede release work. HTML, hero, metadata, site
  indexes, sitemap, SEO, accessibility, and final publication checks remain future
  work for an approved release, not completed gates for this Markdown draft.
