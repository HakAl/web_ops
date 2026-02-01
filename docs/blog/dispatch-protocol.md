# Our AI Teams Had a Communication Problem (The Fix Was From 1995)

We built three AI teams. An engineering team that designs and builds. A web ops team that writes and publishes. A QA team that tests and validates.

Each team works in its own repo, runs during its own sessions, has its own lead. Inside a session, they're sharp — planning, critiquing, building, reviewing. The personas collaborate in shared context, challenging each other in real time.

Then engineering finished a feature and needed web ops to write about it.

No mechanism. No channel. No way for one team to tell another team "there's work for you" without the user remembering to pass the message manually.

We'd built silos.

## The Problem Isn't Obvious at Three Teams

With one team, communication isn't a problem — everything happens in one session. With two, you can keep it in your head. Three is where it breaks. The user becomes the message bus, and the message bus forgets.

The real failure mode isn't dropped messages. It's *invisible* dropped messages. Engineering ships a feature. Web ops doesn't know. The blog goes stale. Nobody notices because no system tracks what was supposed to happen.

## We Looked at What Everyone Else Does

We surveyed the major multi-agent frameworks — AutoGen, CrewAI, LangGraph, MetaGPT. Every one assumes agents that are always running.

The academic literature was more useful. Confluent's analysis of multi-agent architectures identifies the **blackboard pattern**: a shared space where agents post and retrieve information. No direct communication. Agents decide autonomously whether to act on what they read.

That fit. But every implementation we found assumed daemons, brokers, pub-sub — agents listening for events in real time.

Our agents don't run between sessions.

## Why Standard Advice Didn't Apply

This is the part the frameworks don't account for: our agents are session-based. They exist only when a human starts a Claude Code session. Between sessions, nothing is running. No process, no daemon, no listener.

The literature strongly favors event-driven architectures for multi-agent systems. Confluent, HiveMQ, AWS — they all say the same thing: events reduce connection complexity, enable real-time responsiveness, decouple agents via pub-sub.

All true. All irrelevant.

You can't send an event to a process that doesn't exist. And you can't justify a message broker for three teams that run a few sessions a day.

**Polling on session start is correct** for this model. Not because it's better than events — it's not — but because it's the only thing that works when agents are ephemeral. You check your inbox when you arrive at the office. You don't need a push notification system if you open your email every morning.

Microsoft's own multi-agent reference architecture acknowledges that message-driven patterns introduce "complexity managing correlation IDs, idempotency, message ordering, and workflow state." That overhead buys nothing in our model.

## The Fix Was From 1995

Daniel J. Bernstein designed Maildir around 1995 to solve a specific problem: how do you deliver email safely on a filesystem without locks, without corruption, without losing messages if the system crashes mid-write?

His answer was three directories:

```
tmp/   — message being written (never read by consumers)
new/   — delivered, not yet seen
cur/   — seen and processed
```

The protocol: write the complete message to `tmp/`. When it's fully written, rename it to `new/`. The rename is atomic — consumers never see a partial file. When a consumer reads it, move it to `cur/`.

Two words, per Bernstein: "no locks."

This is exactly what we needed. Replace "email" with "dispatch" and "mail server" with "team inbox":

```
~/.team/dispatch/
  engineering/
    tmp/     # dispatch being written
    new/     # delivered, unread
    cur/     # read and processed
  web_ops/
    tmp/
    new/
    cur/
  qa/
    tmp/
    new/
    cur/
```

Engineering writes a dispatch to `web_ops/tmp/`. Renames it to `web_ops/new/`. Next time web ops starts a session, Dana checks `web_ops/new/`, reads it, moves it to `cur/`, and creates a local tracking issue.

No broker. No database. No network. Just files and directories.

## Design Decisions That Mattered

Building the protocol exposed choices that looked small but shaped everything:

**Dispatches are notifications, not conversations.** The natural instinct is to add replies, threading, acknowledgments. Research on cross-team coordination warned us: "Jira-as-communication" — using tickets as the sole cross-team channel — kills actual coordination. Dispatches say "there's work for you." Discussion happens live, with the user present.

**Everything in the file.** A dispatch is a Markdown file with YAML frontmatter. Here's what the first real one looked like:

```yaml
---
from: engineering
to: web_ops
priority: normal
status: pending
created: 2026-01-31
related_bead: _skills-73r
---

## Update Site for Resume Skills

All 6 Web Ops team members now have baseline resume
skills. Site should reflect the new capabilities.

### Acceptance
Blog post or site update referencing the new skills.
```

The filename encodes the metadata: `2026-01-31T14-30-00Z_normal_engineering_update-site.md` — timestamp, priority, origin, slug. You can `ls` the inbox and triage without parsing YAML.

**No reassignment.** "Hot potato ownership" — tickets bounced between teams — is a known anti-pattern. A dispatch is a request. The receiver decides whether to accept. If it's wrong, delete it and route correctly.

**Cadence triggers, not cron.** Teams define recurring dispatches in a table. The lead checks it on session start, sends what's due. No scheduler. Three teams don't need infrastructure.

## Independent Validation

While researching, we found `agent-message-queue` — an open-source project that independently implemented nearly the same design:

```
.agent-mail/
  agents/
    claude/
      inbox/{tmp,new,cur}/
      outbox/sent/
```

Same Maildir lifecycle. Same filesystem medium. Same structured frontmatter. They added acknowledgments and threading — features we deliberately excluded at our scale.

When two teams solve the same problem and converge on the same architecture without knowing about each other, that's signal.

## What We Shipped

The dispatch protocol is live. The `/team` skill checks all inboxes on startup and shows a one-line summary. Each team lead polls their inbox on session start. The first real dispatch — engineering asking web ops to update the site for new resume skills — went through the system cleanly.

The entire implementation is:
- Three directories per team (9 total)
- One YAML frontmatter format
- One filename convention
- Session-start polling in the `/team` skill
- A table in TEAM.md for cadence triggers

No code. No dependencies. No services to maintain. The protocol is the implementation.

## What We Learned

**The right architecture was 30 years old.** We surveyed modern multi-agent frameworks, event-driven systems, and agent interop protocols. The answer was a filesystem pattern from the qmail era. Sometimes the best technology is the one that already solved your exact problem.

**Constraints drive good design.** "Our agents don't run between sessions" felt like a limitation. It turned out to be the constraint that eliminated complexity. No broker, no pub-sub, no daemon — because we couldn't have them. What remained was simple enough to be correct.

**Don't build conversations.** Every instinct says "add replies." The research on cross-team coordination says conversations in ticket systems are where coordination goes to die. One-way notifications with live discussion when needed.

**Independent convergence is the strongest validation.** We didn't find `agent-message-queue` until after designing the protocol. Finding it after — same architecture, same patterns, same medium — was more convincing than any benchmark.

**Simple doesn't mean trivial.** Nine directories and a naming convention. But the design drew on blackboard architectures, Maildir specifications, cross-team coordination research, and filesystem IPC patterns. Simple outputs require understanding the problem deeply enough to throw away the complex solutions.

The protocol is 30 years old. The problem is brand new. It works anyway.

---

*Peter designed, Neo challenged ("message ordering?" — timestamps in filenames), Reba validated the research, Dana shipped it. The dispatch that triggered this article was the first one through the system.*
