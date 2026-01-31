---
name: team
description: >
  Web Ops team orchestration. Invoke with "/team genesis" to bootstrap the improvement cycle,
  "/team iterate" for ongoing evolution, or "/team" for status. Thin wrapper that summons Dana to lead.
---

# Team - Orchestration Layer

<!-- IMMUTABLE SECTION - Grace rejects unauthorized changes -->

## Purpose

This skill is the ignition key. It doesn't think - it summons Dana to lead the team.

## Invocation

- `/team genesis` - Bootstrap. Dana runs the first Retrospective, defines initial protocols.
- `/team iterate` - Improve. Dana drives one improvement cycle.
- `/team` - Status. Show current TEAM.md state.
- `/team <task>` - Autonomous. Team runs full cycle on task.

## Commands

### genesis

First-time bootstrap. Run this once to start the self-improvement loop.

**What happens:**
1. Read current `TEAM.md` state
2. Invoke Dana with: "The team exists but has no operating protocols. Run the first Retrospective. Consult Dee to challenge your proposals, then get Grace to validate before landing changes. Keep it lightweight - velocity over ceremony."
3. Dana defines initial processes in `TEAM.md`
4. The loop begins

**User's role after genesis:** Step back. The team self-organizes. Check in when you want.

### iterate

Ongoing improvement. Run when you want the team to evolve.

**What happens:**
1. Dana reviews what's working and what isn't
2. Proposes changes to `TEAM.md` or skill MUTABLE sections
3. Dee challenges for UX/design bottlenecks
4. Grace validates before landing
5. Changes merge directly (no branch friction)

### status

Quick check on team state.

**What happens:**
1. Read and display `TEAM.md`
2. Show any pending improvements or blockers

### autonomous (default for `/team <task>`)

Run a full cycle on a task with minimal user intervention.

**What happens:**
1. Dana reads the task and creates a plan
2. Dee critiques the plan, identifies UX/design risks
3. Blake implements (with Nora for content, Ari for SEO)
4. Grace reviews before delivery
5. Team delivers output + summary of decisions

**Escape conditions** (team stops and asks user):
- Requirements are ambiguous
- Multiple valid approaches with significant tradeoffs
- Brand/voice implications unclear
- Changes needed outside `_web_ops/` or `.team/`

## Safety

- This skill only orchestrates - Dana makes decisions
- All changes still require Grace validation
- IMMUTABLE sections remain protected

<!-- END IMMUTABLE SECTION -->

---

<!-- MUTABLE SECTION - Can evolve -->

## Implementation Notes

When invoked, this skill should:

1. **Read context**: Load team protocols from `.team/TEAM.md` in project root, or `~/.team/TEAM.md` for global defaults
2. **Invoke Dana**: Use the director-dana skill with appropriate context
3. **Let Dana lead**: Don't micromanage - Dana decides how to run the team

The goal is minimal orchestration overhead. This is a trigger, not a controller.

<team_knowledge>
Genesis complete. Team operational since 2026-01-31.
Protocols: Ship workflow, review gates, collaboration rules, handoff protocol.
</team_knowledge>

<!-- END MUTABLE SECTION -->
