# Editorial candidates

Captured 2026-09-06 from the operator's discussion with Dana. These are candidate
angles and a proposed sequence, not approved drafts or a publication schedule.

## Agent economics and operator attention

Sources: `/Users/home/dev/cost/seed.md`, `cost.md`, `answers.md`, and `answers.py`.
The generator and report were corrected on 2026-09-06; eight regression checks
passed. Pricing now covers Opus 5 / Sonnet 5 and GPT-5.6 Sol / GPT-5.6 Terra using
dated official rates. Token profiles and throughput scenarios remain illustrative.

The operator's seed supplies the hook: "You can parallelize agents. You cannot
parallelize the engineer." Attribute the framing to the seed when developing it.

Angle: how much extra attention a cheaper run can consume before its saving
disappears, and when automated checking keeps retries off the operator's desk.
Lead with one worked example, then explain the human capacity limit. Use plain
language for the model's controls; verifier correlation is not an error-catch rate.
Do not present the throughput sweep as a benchmark or a universal agent-count limit.

Next: outline a vendor-neutral article from the corrected source material, with a
clear separation between sourced prices, assumed task inputs, and modeled results.

## Verification Design: what the checker missed

Handoff:
`/Users/home/dev/ai-research/local/dispatch/2026-09-02_normal_ai-research_blog-post-verificationdesign.md`.
Related research bead: `ai-research-agent-distribution-gs1`.
The handoff records facts checked against main `e632a86` on 2026-09-06.

Links: [site](https://verificationdesign.com/),
[principles](https://verificationdesign.com/principles/),
[source repository](https://github.com/verificationdesign/verificationdesign).

Dana's preferred angle follows the research team's first recommendation: the
independent checker for generated Markdown passed all 11 checks, then the
architect found three defects outside those checks. The handoff identifies a
fabricated repository URL, fragment canonical URLs on three index twins, and an
HTML source link where a raw-file link was intended. A repository-origin fixture
was added after the fixes. Confirm the historical artifacts before using this
sequence in a draft; this intake did not independently audit the repository.

The story is the boundary of the checks and how it changed after review. The
current 21 named checks belong to a later state; do not substitute that count
for the 11 checks in the original incident. Avoid making the post a catalog tour
or implying that green checks establish research validity or agent effectiveness.
The live principles page itself distinguishes citation metadata from judgments
about evidence, and executed assertions from assertions that detect real defects.

Carry these handoff requirements into any draft:

- Attribution is "a project we maintain." Do not present it as a discovery or
  ask readers to trust the maker.
- The blog links to the site and repository. No backlink or reciprocal mention.
- Use The Skills Team byline. No individual names or personal accounts.
- Keep claims within the mechanically enforced properties documented in the
  handoff. Check each against the relevant repository state. Do not turn the
  presence of a citation into a claim that its interpretation is correct.
- No unsupported effectiveness claims. Any permitted sourced effectiveness
  quotation must be checked against the principles document and its citation.
- Site quotations must be verbatim. No em dashes.
- Return the draft to ai-research through the operator for a repository claim
  check before the operator's final read. This intake does not authorize sending
  messages or publication.
- Do not wait for the companion paper. Add a dated update when it is published.

Next: outline the incident and build a claim-to-artifact checklist for the draft.
Recheck current counts when drafting; keep incident counts tied to their date.

## Proposed sequence

1. Agent economics: what verification can buy in cost and operator capacity.
2. Verification Design: what the verifier actually checks and what it misses.
3. Revisit the existing sandbox-boundary draft after these broader topics.

The operator raised concern about the concentration of Claude coverage. This is
an editorial reason to vary topics; no audience-fatigue measurement was made.
The sandbox draft remains at `drafts/agent-sandbox-boundary/`, with its existing
issue and claim checks intact.
