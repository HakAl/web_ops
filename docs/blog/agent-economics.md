---
title: You Can Parallelize Agents. You Cannot Parallelize the Engineer.
published: true
tags: ai, agents, productivity, programming
canonical_url: https://vibecoder.buzz/blog/agent-economics.html
cover_image: https://vibecoder.buzz/blog/agent-economics.jpg
---

Sometimes I get distracted and go a little too deep on a random subject. In this episode of "curiosity got the best of me," I decided to spend my time trying to answer: is it cheaper for a person to use mid-tier or high-tier models?

A cheaper model saves money on each task, but makes more mistakes. Mistakes mean I might have to pay attention and sort them out. Is it worth the discount?

I wanted to know how much extra work landed on me and built a hypothetical cost model to explore it.

## What does the saving buy?

Take a hypothetical task: $5 on the expensive model, $2 on the cheaper one, including all the attempts needed to finish it. You save $3 for that task.

To use a round number, suppose your time is worth $100 an hour. That saving buys 1.8 minutes of your attention.

Spend two extra minutes reviewing, and you've spent $3.33 to save $3. Token spend down. Total cost up.

Pick what an hour of your time is worth and do the math.

## Retries can be a good trade

A cheaper model can still be worth using even if it needs another try. Do I have to get involved each time?

Say you ask an agent to fix CI. An automated check is red, and the agent fixes it. No review, no attention.
You pay for the extra run, but you haven't had to figure out what broke or explain the fix.
If the work is just as good and costs less, that might be a fair trade.

Now say you have to sort out that failing test yourself. You diagnose it, explain it, wait for the fix, and check again. The agent's mistake is now another thing you have to do. A few rounds of that erase any savings.

Of course, your workflows can tell you if a test is failing. The agent can pass every check you gave it and still leave you with work to fix.

Trying again might just get you the same mistake or a different flavor of one. For instance, if the agent misunderstood your intent.
Someone has to notice and work out what to fix.

## Where more agents stop helping

If I have a series of tasks that are independent, I'll run agents in parallel.

In this scenario, I can become the bottleneck. The agents finish and reviews queue up for me. I have to run review, read the changes, triage findings, and sort it all out. Launching another agent adds another review to that queue.

If each finished task costs twice as much attention, I can get through only half as many in the same time. Another agent doesn't give me those minutes back. Obviously, a better harness, useful verification, or a model I don't have to correct as much might help.

Sometimes I just don't want to read any more LLM output and each review needs time I don't have.

## The number I need next

I'd try a cheaper model on work where I know what “done” looks like and can check most of it automatically. Then I'd compare similar tasks. What was the total cost? How much time did I spend steering?
What mistakes turned up after it declared the work done? I'd count the waiting, too, if it kept me from doing something else.

Maybe the more expensive model needs less of my attention. Maybe the cheaper one does just as well with good checks. I can't find that out by changing numbers in a hypothetical model. I have to try it on my own work.

Before I add another agent, I want to know how many minutes of me each finished task needs.

<details>
<summary>Prices, calculations, and assumptions</summary>

This cost model explores that question by changing how often the agent gets the work right, how useful the checks are, and how much time I spend explaining, reviewing, and fixing the work.
The prices came from published API rates: [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), [OpenAI pricing](https://developers.openai.com/api/docs/pricing), and the [GPT-5.6 Terra model page](https://developers.openai.com/api/docs/models/gpt-5.6-terra).
Task sizes and behavior were hypothetical. I wanted to see what would have to be true for each strategy to pay off.

To convert a saving into extra review time:

```text
extra minutes you can afford = dollars saved × 60 / hourly value
```

Here is what that looks like for a hypothetical task that costs $5 on the more expensive model. Tokens are the units used to bill for text sent to and from the model. “1.5×” means the cheaper model uses 50% more tokens to finish the same task, including retries.
Each comparison keeps the same mix of input, output, and cached tokens.

| Comparison | Cheaper model's token use | Saving | Extra attention at $100/hour |
| --- | --- | --- | --- |
| Opus 5 → Sonnet 5 | Same | $3.00 | 108 seconds |
| Opus 5 → Sonnet 5 | 1.5× | $2.00 | 72 seconds |
| GPT-5.6 Sol → Terra | Same | $2.00–$2.50 | 72–90 seconds |
| GPT-5.6 Sol → Terra | 1.5× | $0.50–$1.25 | 18–45 seconds |

Rates rechecked September 30, 2026 using the official sources above. These examples use standard API pricing below the long-context surcharge thresholds. Sonnet 5 costs 40% of Opus 5 across the billing categories used here. Terra costs 50% of Sol for input and cache charges, and 60% for output, which gives the range. Sol's rates are promotional. Subscription plans have different economics.

Extra tokens matter. At twice the token use, Sonnet's saving on that $5 task shrinks to $1. Terra breaks even or costs up to $1 more before anyone reviews the result.

There is more room on an expensive task. With the same relative saving, a $50 task buys ten times as much extra review time as a $5 task. That helps, provided the review and the consequences of mistakes do not grow just as quickly.

Related: our [cross-model review experiment](https://vibecoder.buzz/blog/cross-model-review.html), including a text-matching rule that looked plausible in review but could not compile.

</details>
