# Agent sandbox boundary draft package

Status: rev 1 draft, unpublished. Source material is `/Users/home/dev/wip/blog-notes-stay-in-project-2026-09-03.md` plus the operator's brief of 2026-09-03.

## Contents

1. `post.md`: full draft with dev.to front matter, `published: false`.
2. `claims-and-verification.md`: every claim, its source, and whether this session verified it, plus the pre-publish checklist.

## Team notes, 2026-09-03

**Dana, plan.** This is a Failure-First Arc with a second act. The operator's original frame was "how to keep Claude Code in its directory." The brief widens it to "the project directory is not the agent's boundary," and that is the durable piece. Claude Code supplies the experiment. The conclusion applies to any coding agent. Order: two layers, round one holds, failure one (the reported hole gets used), round two hard close, failure two (exit codes), round three design, round four Chrome temp, round five socket, round six (new: it still does not run), then the four-point boundary mismatch, then the authority argument. The reproduction appendix stays at the end with the version warning repeated.

**Dana, scope call.** The brief asked for the failed approaches with observable symptoms, the five named tests, a prominent version warning, and the Mach wildcard framed as a testing concession. All four are in. One addition beyond the brief: round six. While verifying rounds four and five, Chrome still failed under the final config, at a Mach service registration and a sysctl. That is new evidence for the brief's own thesis, so it went in rather than into a follow-up. Flagging it because it changes the story from "we accepted one global widening and it worked" to "we accepted one global widening and it still does not work."

**Dee, voice.** The brief's own snippet was flagged as accidentally first person. The blog is first person by protocol, and the last five posts all are, so the draft stays first person. The brief's block quotes were written as "we"; converted to "I" so the post sounds like one person. Title check against the last five: no leading "I", no parenthetical, no "Our". Proposed title is "The Project Directory Is Not Where Your Agent Ends." Alternate if Dana wants the hook moment up front: "Claude Code Reported the Hole, Then Climbed Through It." The first is the thesis; the second is the anecdote. Recommending the first, with the anecdote as the TL;DR's second sentence.

**Dee, pattern check on the ending.** Memory hole post ended on a soft second-person offer. Prompt injection ended on a disclosure section. Cross-model review ended on a one-line reversal. This one ends on a flat declarative about the boundary. No bolded list, no callback to the title. Distinct from the last three.

**Nora, cuts.** The notes' "Lessons for the post" list was folded into the four-point "boundary mismatch" section rather than kept as a list of seven. The pytest recipe stayed because it is the one thing a practitioner can paste. The "Division of labor" table stayed because it is the clearest statement of the two-layer idea. The Round 5 residual-risk paragraph moved down into "What the sandbox is actually around" so the socket point lands once, in the argument, instead of twice.

**Ari, SEO notes for build.** Primary phrase: "Claude Code sandbox." Secondary: "PreToolUse hook," "allowAllUnixSockets," "MAC_CHROMIUM_TMPDIR." The last two are rare strings that people will search when they hit the exact errors; the post quotes the errors verbatim for that reason. Meta description candidate, under 160: "I tried to keep Claude Code's writes inside one project. The fence held, the agent used the gap, and the browser reopened it. Where an agent's boundary really is." Slug `agent-sandbox-boundary`.

**Grace, gates before build.** Claims 2, 8, 20, 23, 28, 30, 32 in the verification table are open. Claim 23 matters most: the post must not say socket binding is impossible with `allowUnixSockets` unless someone tests it, because one closed issue suggests a directory entry worked. The current wording is hedged and passes. Placeholder replacement for the home path and session id is a hard blocker.

## Not in this package

- HTML page, hero image, blog index, home page, sitemap: Blake, after Dana's read and user sign-off on the draft.
- dev.to crosspost payload: after publish.
