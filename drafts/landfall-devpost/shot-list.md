# Landfall demonstration shot list

Status: editable draft for architect review. Do not publish.

Legend: `LIVE` must be recorded as execution occurs; `PREP` may be composed in advance from accepted evidence; `MASK` lists material that must never survive into the export.

| Time | Shot | Mode | What must happen | Mask before export | Evidence for numeric caption |
| --- | --- | --- | --- | --- | --- |
| 0:00 | Focus-day close histogram | PREP | Animate no values; use the frozen histogram exactly and label it prior measurement | Actor names, raw source paths outside the repository, per-actor detail | `harness/baseline/local-baseline-2026-08-23.json` → `focus_day.close_histogram_by_hour` |
| 0:10 | Prior dispatch total | PREP | Add the frozen dispatch total and disclosure label | Per-actor detail | `harness/baseline/local-baseline-2026-08-23.json` → `v2_epoch.dispatch_count` |
| 0:18 | Three-layer initiation explanation | PREP | Use records, source structure, and deployment-bounded attestation as separate labels | Seat and actor names | `harness/baseline/local-baseline-2026-08-23.json` → `followup_figures.producer_kind` |
| 0:27 | Support-lead envelope | LIVE or staged UI over real state | Show allowed paths, ceilings, attempts, deadline, and predicate identifiers; activate FleetRun once | Repository-private paths, commit if not public, run token, identity, endpoint | No numeric result; envelope values are scenario inputs, not measured captions |
| 0:50 | Hands leave keyboard | LIVE | Preserve a brief wide frame proving no further operator input | Desktop notifications, username, local paths | None |
| 0:55 | Google Cloud Console service view | LIVE | Show the deployed Cloud Run probe service and revision with the `REAL CLOUD PROBE` chip | Project id and number, account, region if deemed identifying, URL, service-account identity, billing, neighboring resources | No numeric caption; resource presence is supported by `harness/evidence/account-proof/cloud-binding-evidence.json` → `findings` |
| 1:04 | Probe action and closed response | LIVE | Trigger or show the bounded probe action and its sanitized response shape | Authenticated endpoint, authorization header, cookie, token, raw payload, identifiers | `harness/evidence/account-proof/account-proof-evidence.json` → `findings` |
| 1:12 | Sanitized account-proof panel | PREP | Show passed slice findings and keep the four production checks visibly unknown | Causal FleetRun id, hashes if architect elects not to display them, local source path | `harness/evidence/account-proof/account-proof-evidence.json` → `check_results`, `findings`; `harness/evidence/account-proof/manifest.json` → `files` |
| 1:28 | Evidence-boundary hard cut | PREP | Replace teal lane with amber label `DETERMINISTIC LOCAL GOVERNANCE DEMONSTRATION` | Nothing additional | None |
| 1:32 | Two admitted work items | LIVE, unedited segment starts | Show role-level items and states without identities | Actor and seat names, local paths, raw failure text | `[N: <harness kill output path> <initial work-item fields>]` |
| 1:40 | Attempt N checkpoint | LIVE | Show checkpoint commit before fault injection | Run token, branch if private, local paths | `[N: <harness kill output path> <checkpoint field>]` |
| 1:49 | Local process exit | LIVE | Harness injects the local process fault and records its observation | PID if considered identifying, terminal prompt path, username | `[N: <harness kill output path> <local process-exit observation field>]` |
| 1:58 | Lease expiry | LIVE | Show `lease_expired_unconfirmed` and no terminal receipt | Attempt id unless replaced by N in the overlay | `[N: <harness kill output path> <lease and terminal-receipt fields>]` |
| 2:09 | Atomic successor creation | LIVE | Show generation bump and `parent_attempt_id` lineage in one state change | Raw attempt identifiers; overlay N and N+1 | `[N: <harness kill output path> <successor and lineage fields>]` |
| 2:20 | Authentic stale closeout replay | LIVE | Replay predecessor closeout after successor is active | Run token and request authentication material | `[N: <harness kill output path> <replay-authenticity field>]` |
| 2:29 | Refusal | LIVE | Show `stale_attempt` and terminal state unchanged | Decision prose, raw identifiers | `[N: <harness kill output path> <stale refusal and terminal-state fields>]` |
| 2:37 | Other item continues | LIVE, unedited segment ends after proof | Show an independent progress event whose timing overlaps succession | Work-item ids, actor or seat name | `[N: <harness kill output path> <continuing-item field>]` |
| 2:43 | Verifier evidence panel | LIVE if possible | Show artifact reference intake, verifier retrieval or reproduction, and tri-state resolution | Repository-private artifact URL, local path, raw test failure | `[N: <harness verifier output path> <repro_fails_at_base, repro_passes_at_candidate, suite_no_regression fields>]` |
| 3:05 | Unknown counterexample | PREP from real artifact | Show `verification_blocked`, not terminal, with `evidence_unknown` | Attempt id, raw operator prose | `[N: <harness verifier output path> <unknown and state fields>]` |
| 3:16 | Verifier terminal transition | LIVE or PREP from accepted artifact | Show that verifier authority writes terminal state | Identity string; retain only role label | `[N: <harness verifier output path> <terminal authority and verdict fields>]` |
| 3:27 | Ledger | PREP | Put `UNKNOWN` rows first, then changed and survived mechanisms | Any private link or unpublished repository URL | Each numeric row requires its own `[N: <artifact path> <field>]`; omit unavailable rows |
| 3:47 | End card | PREP | Landfall, category, public repository placeholder until release | Nothing private | None |

## Capture order

1. Rehearse masking with fake values before any cloud recording.
2. Record the cloud console and probe beat in a dedicated browser profile with notifications disabled.
3. Record the local governance beat in one take with a clean terminal prompt and the persistent local label.
4. Record the verifier continuation immediately after the live governance take if the UI can preserve continuity.
5. Build prior-measurement and final-ledger cards only from accepted artifacts.
6. Perform a frame-by-frame privacy review before upload.

## Recording artifacts to retain privately

- Original untouched screen recording.
- Redacted edit project.
- Final caption file.
- Final export checksum.
- A capture manifest mapping each published numeric caption to its repository artifact path and field.

Do not commit raw screen recordings if they contain any masked value.
