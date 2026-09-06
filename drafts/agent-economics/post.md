---
title: You Can Parallelize Agents. You Cannot Parallelize the Engineer.
published: false
tags: ai, agents, productivity, programming
---

I went down a rabbit hole trying to answer a practical question: how much worse could a cheaper model be before it stopped being a bargain?

If it needs another attempt, I can let it run longer. If it takes twice as long, perhaps I can run two agents. At some point, enough cheap capacity ought to make up for the difference.

But what if the extra work lands on me?

I put together a model to vary the assumptions: how often an attempt succeeds, how useful the checks are, and how many minutes the operator spends specifying, reviewing, and repairing the work. The prices came from published API rates. Task sizes and behavior were hypothetical: I wanted to understand when the trade could work.

The first useful result was a conversion from dollars to minutes.

## What does the saving buy?

Suppose a task costs $5 on the expensive model and $2 on the cheaper one, including all the tokens used to finish it. You save $3.

At $100 an hour, that buys 1.8 minutes of your attention.

Spend two extra minutes checking the cheaper model's work and you have spent $3.33 to save $3. The API bill went down. The total went up.

Your hourly figure does not have to be a billing rate. It can be the value you assign to an hour you could spend elsewhere. The calculation is the same:

```text
extra minutes you can afford = dollars saved × 60 / hourly value
```

Here is the allowance for a hypothetical task that costs $5 on the higher tier. The token multiplier describes the cheaper model's total token use for the same finished task, with the same mix of billing categories.

| Comparison | Cheaper model's token use | Saving | Extra attention at $100/hour |
| --- | --- | --- | --- |
| Opus 5 → Sonnet 5 | Same | $3.00 | 108 seconds |
| Opus 5 → Sonnet 5 | 1.5× | $2.00 | 72 seconds |
| GPT-5.6 Sol → Terra | Same | $2.00–$2.50 | 72–90 seconds |
| GPT-5.6 Sol → Terra | 1.5× | $0.50–$1.25 | 18–45 seconds |

These use standard, short-context API rates checked September 6, 2026. Sonnet's rates are 40% of Opus's across the categories used here. Terra's are 50% of Sol's for input and cache charges, and 60% for output, hence the range. Sol's listed rates are promotional. These are API comparisons; subscription plans have different economics. [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), [OpenAI pricing](https://developers.openai.com/api/docs/pricing).

Extra tokens matter. At twice the token use, Sonnet's saving on that $5 task shrinks to $1. Terra breaks even or costs up to $1 more before anyone reviews the result.

There is a counterweight: a $50 task offers ten times the attention allowance of a $5 task, at the same price ratio and token multiplier. Cheap models have more room on expensive runs, provided the review burden and consequences of mistakes do not eat the larger saving.

## Retries can be a good trade

A lower first-pass success rate does not automatically make a model uneconomical.

Imagine an automated check that accepts every correct result and rejects every incorrect one. A rejected attempt goes straight back to the agent. Assume each retry has the same chance of success and the same cost as the first attempt, including the check.

For this example, a stronger model costs $5 **per attempt** and succeeds 90% of the time. A weaker one costs $2 per attempt and succeeds 70% of the time.

The expected cost of attempts and checks for a correct result is the attempt cost divided by its success probability: about $5.56 for the stronger model and $2.86 for the weaker one. It needs more attempts, but each is cheap enough to leave it ahead. If those retries need no additional attention from me, that can be a useful trade.

This example counts retries explicitly. The earlier token table already includes them in the task total. They belong in the bill once.

The perfect check is doing a lot of work in that argument.

Suppose the weaker model still gets 70 of every 100 attempts right on average, but the check catches only 90% of the wrong ones. It catches 27 of the 30 failures. Three slip through alongside the 70 correct results. About 4.1% of accepted results are wrong, even though the check catches nine out of ten mistakes. This assumes correct results are never rejected.

And retries may repeat the same mistake. A missing requirement or a shared blind spot does not disappear because I launch another session.

In our [cross-model review experiment](https://vibecoder.buzz/blog/cross-model-review.html), running a proposed regex exposed that it could not compile. An executable check can answer that question. Whether the feature solves the right problem asks more of the reviewer.

## What the model's controls mean

The model separates two questions that are easy to blur together: **how often the agent is right**, and **how well the check can tell**.

The capability gap shifts the hypothetical model toward worse first attempts. It is not a measured distance between Sonnet and Opus, or Terra and Sol.

The verifier setting, called `rho` in the calculations, describes how closely its score tracks actual quality. A value of 0.9 is a correlation, not a promise to catch 90% of mistakes. The threshold for passing that check also matters: making it stricter can send both bad results and good results back for another attempt. Human review happens after that automated gate.

I swept those settings across possible values. That explores different worlds; it does not tell me which world my workflow occupies. The calculation rewards good tasks completed per day and charges operator time for review and repair. Without a spending budget or a maximum acceptable defect rate, its busiest configuration is not automatically one I should use.

## Where more agents stop helping

Now give the operator an eight-hour day with 80% of it available for productive work. That is 384 minutes.

If each finished task takes five minutes of their attention, the ceiling is 76.8 tasks a day. At ten minutes, it is 38.4. These are average capacities for a stream of small, independent tasks, not a prediction about how many features anyone can ship.

Here are three hypothetical workflows. Machine time includes retries and automated checks. Human time includes specification, integration, review, and expected repair. Comparable accepted quality is an assumption in this illustration, not a result.

| Workflow | Machine minutes per task | Human minutes per task | Human ceiling, tasks/day | Agent slots to reach it |
| --- | --- | --- | --- | --- |
| Baseline | 60 | 5 | 76.8 | 4 |
| More automated retries | 120 | 5 | 76.8 | 7 |
| More retries and human work | 120 | 10 | 38.4 | 4 |

The slots are allowed to run 24 hours a day. One slot handles one run at a time, then takes another task. With enough work available, its capacity is its active minutes divided by machine minutes per task. Add slots until that capacity reaches the human ceiling, rounding up to a whole slot.

In the second row, more agents cover the extra machine time and recover the baseline throughput. In the third, four slots already produce as much work as the operator can process. Seven slots cannot recover the lost human capacity.

That is why there is no useful universal answer like “run four agents.” If the agents only run while I am working, I need more slots to provide the same machine capacity. If each result needs more of my attention, my daily ceiling falls. This is an average capacity calculation; deadlines, handoff timing, rate limits, and context switching can make the practical result worse.

Once the human is full, starting work faster only creates a queue.

## The number I need next

I would start a cheaper-model trial on work with clear acceptance criteria, executable checks, and a retry loop that can handle failures before asking me to intervene. Work that needs substantial judgment gets a different calculation. A stronger model may justify its price by needing less attention or producing fewer costly mistakes; that difference still needs to be measured.

For a batch of comparable tasks, I want the total token bill, time spent waiting when it blocks me, and my minutes spent specifying, reviewing, redirecting, and repairing. I also need to record defects found after acceptance. Matching throughput while quietly accepting more bad work would answer the wrong question.

The allowance from the first table is shared by all the extra costs. Spend it on review and it is no longer available to cover delay or recovery.

Before I add another agent, I want to know how many minutes of me each finished task needs.
