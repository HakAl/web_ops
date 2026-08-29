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

## 0:27 to 0:55 | The Unlikely Hero authorizes the envelope

### Picture

Show the support-lead view of one pending FleetRun. Reveal plain-language renderings of allowed paths, call and token ceilings, attempt ceiling, deadline, and the fixed predicate set. The operator activates `Authorize FleetRun`, then removes their hands from the keyboard. Do not show another human control in the video.

### Voiceover

“The operator is a support lead who knows the incident but does not review code. They authorize one bounded envelope: where agents may act, what they may spend, how many attempts they may make, and what evidence counts as done. That is the final human input in this run.”

### Capture gate

The authorization screen must expose structured values only and must contain no free-form predicate editor, merge control, or code-review control.

## 0:55 to 1:28 | Real Google Cloud beat

### Picture

Cut to the visual system’s teal lane. Show a masked Google Cloud Console Cloud Run service and revision view, then the running probe response and a prepared, sanitized evidence-panel view derived from `harness/evidence/account-proof/`. Show `Gemini structured output: passed`, `outbox: sent`, `consumer event_id dedup: passed`, and `single logical effect: passed`. Keep the remaining production checks visible as `UNKNOWN`, not hidden below the fold.

### Voiceover

“This highlighted beat is the bounded real-cloud probe. The masked Cloud Run view proves the deployed backend. The probe invokes Gemini 3.7 Flash through ADK, writes the authoritative application state and outbox, relays the event, and records one logical consumer effect. The committed evidence packet supports this slice. It does not say the complete worker fleet or the kill sequence ran here, and the remaining production checks are still unknown.”

### Documentation footer

`Cloud Run service view: https://cloud.google.com/run/docs/managing/services`

`Gemini 3.7 Flash: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-7-flash`

`Account proof: harness/evidence/account-proof/manifest.json`

## 1:28 to 2:43 | Deterministic local governance demonstration

### Picture

Hard cut from teal to amber. Put the full-width label `DETERMINISTIC LOCAL GOVERNANCE DEMONSTRATION` on screen. Begin one continuous capture with a visible clock. Do not cut until the second work item’s progress is shown.

Live sequence:

1. The console shows two admitted work items without identities.
2. Attempt N commits a checkpoint.
3. The harness terminates its local process and observes the local exit.
4. No terminal receipt appears.
5. The short demo lease expires with `lease_expired_unconfirmed`.
6. The supervisor atomically creates N+1 with `parent_attempt_id = N` and a higher generation.
7. The harness replays N’s authentic closeout after N+1 becomes active.
8. Landfall records `stale_attempt`; terminal state remains unchanged.
9. The other work item advances during the sequence.

### Voiceover

“Now the evidence boundary changes. This is the deterministic local governance harness. Attempt N checkpoints, then its local process exits. Landfall does not use that observation as authority. The record says `lease_expired_unconfirmed`, because lease expiry proves expiry, not death. After expiry, one transaction fences N and creates N plus one with its parent recorded. We replay N’s genuine, correctly authenticated closeout. It is refused because N no longer owns the active generation. The second item continues while succession happens.”

### Evidence footer

Kill, lineage, stale-closeout, and continuing-item captions: `[N: <harness kill output path> <field>]`.

### Cut rule

If the named kill artifact is unavailable at capture time, do not substitute a rehearsed UI animation. Cut every result sentence in this beat and record only after the artifact exists.

## 2:43 to 3:27 | Deterministic verifier decides completion

### Picture

Continue the same live capture if practical. Follow N+1’s artifact reference into the verifier panel. Show that the verifier is a process role, not a model seat. Display each predicate as `TRUE`, `FALSE`, or `UNKNOWN`, with evidence source and freshness. Show one earlier unknown example landing in `verification_blocked`, then the current successor’s verifier-controlled terminal transition.

Candidate captions:

- Reproduction fails at base: [N: <harness verifier output path> <repro_fails_at_base field>]
- Reproduction passes at candidate: [N: <harness verifier output path> <repro_passes_at_candidate field>]
- Regression suite result: [N: <harness verifier output path> <suite_no_regression field>]

### Voiceover

“The worker submits an artifact reference, not a verdict. The verifier is deterministic, not a model, and it retrieves or reproduces every authoritative value. Missing, stale, malformed, or unresolvable evidence becomes unknown. Unknown moves the attempt to `verification_blocked` and authorizes no terminal write. Here, only the verifier’s measurements permit completion. The worker cannot write terminal state.”

### Cut rule

If Set A verifier evidence is unavailable, remove all correctness language and use: “The verifier admits structural evidence: the artifact applies at base, its paths remain inside the envelope, and the directive is well formed. This does not prove the defect is fixed.”

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
- [ ] The backend proof includes a masked Google Cloud Console or Cloud Run view.
- [ ] All numeric captions still show exact artifact path and field until architect acceptance.
- [ ] No local kill action is narrated or framed as a Cloud Run event.
- [ ] The remaining unknown production checks stay visible in the real-cloud beat.
- [ ] The final upload is public on YouTube or Vimeo, not unlisted.
