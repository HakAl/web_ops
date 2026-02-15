---
title: Your AI Reviewer Has the Same Blind Spots You Do
published: false
tags: ai, llm, codereview, programming
canonical_url: https://vibecoder.buzz/blog/cross-model-review.html
cover_image: https://vibecoder.buzz/blog/cross-model-review.jpg
---

Line 126 of our plan: `(\b\w+\b)(?:\s+\1){4,}`. A regex to catch adversarial token repetition. Expected precision: 95%+.

We reviewed it. Our architect reviewed it. It looked solid.

The pattern uses a backreference, `\1`. Parapet compiles patterns with Rust's regex engine. Rust's regex engine doesn't support backreferences. The pattern can't compile. It would panic at startup.

We sent the plan to five AI model families for independent review. GPT spent five minutes in the actual Rust codebase, found the compilation call, ran the pattern against `rg` (same engine) and came back with: `backreferences are not supported`. Separately, Qwen flagged the same pattern in two seconds through a completely different lens: untested assumptions about edge cases. Same regex. Two families. Two different problems.

## The Blind Spot You Can't See

Last month we built [Cold Critic](https://vibecoder.buzz/blog/cold-critic.html), an isolated reviewer that checks plans without knowing who wrote them. It counters self-preference bias: the tendency of a model to rate its own output higher than it deserves.

But Cold Critic is still Claude reviewing Claude's work. Different instance, same architecture, same training data, same gaps in knowledge. The regex backreference is exactly the kind of thing Claude would miss twice. Not because of bias, but because of shared knowledge boundaries.

Research calls this cognitive monoculture. Different model families produce genuinely different error distributions. Heterogeneous ensembles achieve ~9% higher accuracy than same-model groups on reasoning benchmarks ([2404.13076](https://arxiv.org/abs/2404.13076)). Not because any single model is smarter. Because they fail differently.

A recent paper on AI delegation ([2602.11865](https://arxiv.org/abs/2602.11865)) maps the mitigation ladder explicitly: contrarian prompting, then cross-model review. Our own team discussion flagged cognitive monoculture as a known gap months ago. So we built the next step.

## Different Brains, Different Lenses

We send the plan to five model families in parallel, each with a specific review lens:

| Family | Lens |
|--------|------|
| Kimi (Moonshot AI) | Internal coherence. Does each step follow from the last? |
| Qwen (Alibaba) | Hidden assumptions. What breaks if they're wrong? |
| Mistral | Gaps. What would block you from implementing this tomorrow? |
| DeepSeek | Reasoning. Reconstruct the argument. Where do you diverge? |
| GPT (OpenAI) | Ground truth. Does the plan match the actual codebase? |

Results come back. Claude clusters the findings by root cause, since different models often describe the same gap in different language. Present everything. The user triages.

Four of the five reviewers run on free-tier APIs. The ground truth reviewer uses OpenAI's Codex, and Claude orchestrates. Both are tools you're already paying for. The marginal cost of adding four independent model families to your review process is effectively zero. The architecture (independent parallel review with role-specific lenses, deduplicated by root cause) is portable to any orchestrator. The [skill](https://github.com/HakAl/team_skills/blob/master/collaborate/SKILL.md) runs from Claude Code, but the whole point is that the reviewers aren't Claude.

Research supports the approach: independent parallel review outperforms multi-round debate ([2507.05981](https://arxiv.org/abs/2507.05981)). You don't want models arguing with each other. You want them arriving independently and comparing notes after.

## The Test

The plan: tuning regex-based prompt injection detection in [Parapet](https://github.com/Parapet-Tech/parapet), a Rust security library. Seven steps: delete a noisy pattern, rewrite another, add four new attack categories, re-evaluate. Real math, real tradeoffs, already reviewed internally.

Five providers. All responded successfully. The four API providers returned in 1.7 to 6.6 seconds. The ground truth reviewer explored the full repository in about five minutes. Seven findings, four corroborated by multiple families.

**The crash.** GPT explored the Rust codebase, found the compilation call in `pattern.rs`, and ran the pattern against `rg`. Same regex engine, same error: backreferences not supported. Qwen, reviewing through an assumptions lens, independently flagged the same pattern for a different reason: untested edge cases where poetry or jargon could trigger false positives. The plan was confident about this pattern. Neither the author nor the internal reviewer caught either problem.

**The scope mismatch.** The ground truth reviewer traced through actual Rust source files (`trust.rs`, `l3_inbound.rs`, `defaults.rs`) and discovered that the plan's precision estimates were calibrated for tool results only. But the code scans all untrusted messages, including user chat, where roleplay and authority claims are common. The precision numbers were wrong because the plan assumed a narrower scope than the code implements. No plan-only reviewer could have found this. It required reading the codebase.

**The unreachable target.** Three providers (Kimi, Qwen, and DeepSeek) independently flagged the same gap: the plan states a 20% coverage target but forecasts 9-15%, with no mechanism to close the difference. The plan's own math section acknowledged this but never revised the number. Three brains, three lenses, same root cause.

**The honest separation.** Not everything landed. "Adversarial adaptation risk" is real in general but not actionable for this phase. The system separated weakly grounded concerns from grounded findings instead of inflating the count. Presenting everything doesn't mean presenting everything equally.

## What Corroboration Tells You

When two models from different families independently flag the same root cause, that's convergent evidence. When three do, you should probably listen.

But corroboration isn't the only signal. The test fixture finding came from a single provider. Deleting patterns without updating their test assertions would break the build. It was right. Single-provider findings aren't automatically weaker. They might just require information only one reviewer had.

The value isn't consensus. It's coverage. Five models see five different slices of the problem. Some slices overlap. That's corroboration. Some don't. That's the whole point.

We didn't need five models to be smarter than one. We needed them to be wrong about different things.
