# Landfall demonstration storyboard and voiceover

Status: editable draft for architect review. Do not publish or record from this draft until every capture gate is satisfied.

Target runtime: 3:55, leaving five seconds below the contest limit. English narration. Add burned-in English subtitles for accessibility and muted playback.

## Persistent on-screen conventions

- Top-left status chip: `REAL CLOUD PROBE` or `DETERMINISTIC LOCAL GOVERNANCE DEMONSTRATION`.
- Bottom-left evidence chip: source artifact path, never a private identifier.
- Bottom-right clock during the live sequence: `LIVE, UNEDITED` plus elapsed capture time.
- Mask project identifiers, service-account identities, authenticated endpoints, account details, run tokens, raw failures, stack traces, local filesystem paths, and actor or seat names.
- The local sequence never appears over Cloud Run or Google Cloud Console footage.

## 0:00 to 0:27 | Measured friction in the disclosed prior fleet

### Picture

Open on a prepared hourly histogram using [N: harness/baseline/local-baseline-2026-08-23.json focus_day.close_histogram_by_hour]. The frame carries the caption `PRIOR MEASUREMENT OF A DISCLOSED PRE-EXISTING SYSTEM, NOT LANDFALL PERFORMANCE`. Show the total dispatch caption as [N: harness/baseline/local-baseline-2026-08-23.json v2_epoch.dispatch_count]. Do not show seat identities.

### Voiceover

“We built Landfall after watching a prior agent fleet complete [N: harness/baseline/local-baseline-2026-08-23.json v2_epoch.dispatch_count] dispatches in its frozen measurement window. The agents produced the dispatches, but the substrate could not start an architect session, and this deployment still followed the operator’s time at the keyboard. The close histogram shows the duty-cycle shape. These are disclosed prior measurements, not Landfall results.”

### Evidence footer

`harness/baseline/local-baseline-2026-08-23.json: v2_epoch.dispatch_count, focus_day.close_histogram_by_hour, followup_figures.producer_kind`

## 0:27 to 0:55 | The Unlikely Hero starts the bounded run

### Picture

Show the actual terminal command beside a prepared, source-backed rendering of the pre-registered envelope inputs: allowed paths, call and token ceilings, attempt ceiling, and fixed predicate identifiers. The operator runs the command once, then removes their hands from the keyboard. There is no authorization button or writable console in the current build.

```bash
python3 -m harness.fault_injection \
  --output-root harness/out \
  --fleet-run-id landfall-local-demo
```

### Voiceover

“The operator is a support lead who knows the incident but does not review code. The envelope inputs are pre-registered: where agents may act, what they may spend, how many attempts they may make, and which structural predicates govern this run. The operator starts the command once. That is the final human input.”

### Capture gate

The prepared envelope panel must be traceable to source-controlled inputs. Do not mock an interaction control that does not exist. The console remains GET/HEAD-only and does not authorize, merge, or review code.

## 0:55 to 1:28 | Real Google Cloud beat

### Picture

Cut to the visual system’s teal lane. Show a masked Google Cloud Console Cloud Run service and revision view, then the live probe response and a prepared, sanitized evidence-panel view derived from `harness/evidence/account-proof/`. Show `Gemini structured output: passed`, `outbox: sent`, `consumer record keyed by event_id: passed`, and `one logical effect: passed`. Beside them, show `redelivery/republication: UNKNOWN` and keep every other unresolved production check visible.

### Voiceover

“This highlighted beat is the bounded real-cloud probe. The masked service and revision view, the live probe response, and the committed packet show the bounded deployed slice. The probe invokes Gemini 3.7 Flash through ADK on Cloud Run (https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-7-flash, https://google.github.io/adk-docs/, https://cloud.google.com/run/docs/overview). The packet records application state, an outbox, one observed delivery, and one logical consumer effect (https://cloud.google.com/firestore/docs/overview, https://cloud.google.com/pubsub/docs/overview). It does not establish redelivery, the complete worker fleet, or the kill sequence, and the remaining production checks are still unknown.”

The documentation URLs above appear as readable on-screen footnotes and are omitted from spoken narration.

### Documentation footer

`Cloud Run service view: https://cloud.google.com/run/docs/managing/services`

`Gemini 3.7 Flash: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-7-flash`

`Account proof: harness/evidence/account-proof/manifest.json`

## 1:28 to 2:43 | Deterministic local governance demonstration

### Picture

Hard cut from teal to amber. Put the full-width label `DETERMINISTIC LOCAL GOVERNANCE DEMONSTRATION` on screen. Record one continuous terminal execution of the actual command with a visible clock. The runner emits a sanitized summary only, so do not add simulated intermediate logs or claim that state changes streamed live.

Immediately after the unedited command finishes, cut to two prepared, source-backed evidence views:

1. The emitted `fault_injection.json` artifact, with ordered scenario fields highlighted.
2. The read-only final projection derived from the same in-memory StateStore.

The final observed states are explicit: predecessor `expired`, successor `admitted`, and independent second attempt `in_flight`. The artifact also records checkpoint receipt, a local child-process observation that authorized no transition, no predecessor terminal receipt, `lease_expired_unconfirmed`, generation succession with a parent attempt, the authentic late closeout refused as `stale_attempt`, verifier-only terminal authority, and progress on the independent attempt.

### Voiceover

“Now the evidence boundary changes. This command runs the deterministic local governance harness against an in-memory StateStore, not Firestore. The terminal stays unedited. After it completes, the artifact records the ordered observations. Attempt N checkpointed, and the local process observation authorized nothing. Lease expiry fenced N, succession recorded a higher generation and parent attempt, and N’s authentic late closeout was refused as stale. The final projection shows N expired, the successor admitted, and the independent attempt still in flight.”

### Evidence footer

Kill, lineage, stale-closeout, and continuing-item captions use the exact fields listed in `shot-list.md`, including `[N: harness/out/landfall-local-demo/fault_injection.json scenario.predecessor.late_closeout_refusal]`, `[N: harness/out/landfall-local-demo/fault_injection.json scenario.succession.successor_has_parent_attempt]`, and `[N: harness/out/landfall-local-demo/fault_injection.json scenario.concurrent_work_item.reached_state]`.

### Cut rule

If `harness/out/landfall-local-demo/fault_injection.json` is unavailable at capture time, do not substitute a rehearsed UI animation. Cut every result sentence in this beat and record only after the artifact exists.

## 2:43 to 3:27 | Deterministic verifier decides completion

### Picture

Use the emitted artifact, not a fictional verifier UI. Highlight `scenario.successor_terminal.verifier_controlled`, `scenario.successor_terminal.verdict`, and `scenario.successor_terminal.terminal_receipt_recorded`. Beside it, show the source-controlled Set B predicate definitions and label the run’s results `FIXTURE-PRODUCED STRUCTURAL EVIDENCE`.

Default captions:

- Verifier-only terminal authority: `[N: harness/out/landfall-local-demo/fault_injection.json scenario.successor_terminal.verifier_controlled]`
- Successor verdict: `[N: harness/out/landfall-local-demo/fault_injection.json scenario.successor_terminal.verdict]`
- Terminal receipt recorded: `[N: harness/out/landfall-local-demo/fault_injection.json scenario.successor_terminal.terminal_receipt_recorded]`
- Scope: `STRUCTURAL EVIDENCE ONLY; THIS RUN DOES NOT ESTABLISH THAT THE DEFECT IS FIXED`

### Voiceover

“The worker submits an artifact reference, not a verdict. In this run, fixture-produced Set B structural results enter the verifier-controlled boundary, and only that boundary writes the successor’s admitted state and terminal receipt. The worker cannot write terminal state. This demonstrates verifier-only terminal authority over structural evidence. It does not establish that the defect is fixed.”

### Cut rule

Do not add `repro_fails_at_base`, `repro_passes_at_candidate`, `suite_no_regression`, retrieval, reproduction, or correctness language unless a separately accepted artifact names those observed fields. If that artifact does not land, the structural-evidence wording above is final.

## 3:27 to 3:55 | Counterexamples first

### Picture

End on a prepared ledger with three columns: `SURVIVED`, `CHANGED`, `UNKNOWN`. Put counterexamples first. Show the public correction-trail filename, the cloud proof packet path, and the local harness artifact path. If measured Landfall time, tokens, or retrospective currency are still unavailable, omit those rows entirely.

### Voiceover

“Landfall’s result is a ledger, not a victory lap. Generation fencing, verifier authority, idempotent decisions, and unknown-preserving state survive the move. Process-death proof does not. The cloud probe is real, the kill sequence is local, and the remaining production checks are unknown. The correction trail ships with the project because the architecture is the set of claims that survived evidence.”

## Final edit checklist

- [ ] Runtime is 3:55 or shorter after title card and end card.
- [ ] English subtitles match the final narration.
- [ ] The cloud proof and local governance labels remain present for their entire beats.
- [ ] The live sequence is visibly continuous and unedited.
- [ ] The local live capture shows the actual terminal command and sanitized summary, not simulated intermediate logs.
- [ ] The final projection shows predecessor `expired`, successor `admitted`, and independent attempt `in_flight`.
- [ ] The backend proof includes a masked Google Cloud Console or Cloud Run view.
- [ ] All numeric captions still show exact artifact path and field until architect acceptance.
- [ ] No local kill action is narrated or framed as a Cloud Run event.
- [ ] The remaining unknown production checks stay visible in the real-cloud beat.
- [ ] The final upload is public on YouTube or Vimeo, not unlisted.
