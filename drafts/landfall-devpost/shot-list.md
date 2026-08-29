# Landfall demonstration shot list

Status: editable draft for architect review. Do not publish.

Legend: `LIVE` must be recorded as execution occurs; `PREP` may be composed in advance from accepted evidence; `MASK` lists material that must never survive into the export.

| Time | Shot | Mode | What must happen | Mask before export | Evidence for numeric caption |
| --- | --- | --- | --- | --- | --- |
| 0:00 | Focus-day close histogram | PREP | Animate no values; use the frozen histogram exactly and label it prior measurement | Actor names, raw source paths outside the repository, per-actor detail | `harness/baseline/local-baseline-2026-08-23.json` → `focus_day.close_histogram_by_hour` |
| 0:10 | Prior dispatch total | PREP | Add the frozen dispatch total and disclosure label | Per-actor detail | `harness/baseline/local-baseline-2026-08-23.json` → `v2_epoch.dispatch_count` |
| 0:18 | Three-layer initiation explanation | PREP | Use records, source structure, and deployment-bounded attestation as separate labels | Seat and actor names | `harness/baseline/local-baseline-2026-08-23.json` → `followup_figures.producer_kind` |
| 0:27 | Actual operator command and envelope | PREP plus LIVE command | Show the real `python3 -m harness.fault_injection` command beside source-backed pre-registered envelope field names; do not stage an authorization button | Repository-private paths, commit if not public, run token, identity, endpoint, terminal prompt path | No numeric result; envelope values are scenario inputs, not measured captions |
| 0:50 | Hands leave keyboard | LIVE | Preserve a brief wide frame proving no further operator input | Desktop notifications, username, local paths | None |
| 0:55 | Google Cloud Console service view | LIVE | Show the deployed Cloud Run probe service and revision with the `REAL CLOUD PROBE` chip | Project id and number, account, region if deemed identifying, URL, service-account identity, billing, neighboring resources | No numeric caption; resource presence is supported by `harness/evidence/account-proof/cloud-binding-evidence.json` → `findings` |
| 1:04 | Probe action and closed response | LIVE | Trigger or show the bounded probe action and its sanitized response shape | Authenticated endpoint, authorization header, cookie, token, raw payload, identifiers | `harness/evidence/account-proof/account-proof-evidence.json` → `findings` |
| 1:12 | Sanitized account-proof panel | PREP | Show `consumer record keyed by event_id: passed` and `one logical effect: passed`; keep redelivery/republication and all other unresolved production checks visibly unknown | Causal FleetRun id, hashes if architect elects not to display them, local source path | `harness/evidence/account-proof/account-proof-evidence.json` → `check_results`, `findings`; `harness/evidence/account-proof/manifest.json` → `files` |
| 1:28 | Evidence-boundary hard cut | PREP | Replace teal lane with amber label `DETERMINISTIC LOCAL GOVERNANCE DEMONSTRATION` | Nothing additional | None |
| 1:32 | Local runner command | LIVE, unedited segment starts | Run `python3 -m harness.fault_injection --output-root harness/out --fleet-run-id landfall-local-demo` once in a clean terminal; do not simulate intermediate output | Username, prompt path, environment, notifications | No result caption during execution |
| 1:40 | Sanitized command summary | LIVE, unedited segment ends after process returns | Hold the runner's real sanitized summary; it names the file, hash, byte count, and write result but does not stream intermediate states | Output root if rendered by surrounding shell, local prompt path | `[N: harness/out/landfall-local-demo/fault_injection.json schema_version]` |
| 1:49 | Artifact overview | PREP from emitted artifact | State plainly that the artifact records ordered final observations after the run; do not imply those observations streamed live | FleetRun id if the final public capture policy cuts it, hash if cut, raw source path outside repository | `[N: harness/out/landfall-local-demo/fault_injection.json kind]` |
| 1:58 | Local process and lease evidence | PREP from emitted artifact | Show that the child observation authorized no transition, predecessor terminal receipt is absent, and the lease reason is `lease_expired_unconfirmed` | Any raw process value; use the closed artifact fields only | `[N: harness/out/landfall-local-demo/fault_injection.json scenario.child_process.authorized_a_transition]`; `[N: harness/out/landfall-local-demo/fault_injection.json scenario.predecessor.terminal_receipt_from_attempt]`; `[N: harness/out/landfall-local-demo/fault_injection.json scenario.predecessor.lease_expiry_reason]` |
| 2:09 | Succession evidence | PREP from emitted artifact | Show generation change and parent-attempt presence as artifact fields, not as a live console animation | Raw attempt identifiers | `[N: harness/out/landfall-local-demo/fault_injection.json scenario.succession.atomic_generation_bump]`; `[N: harness/out/landfall-local-demo/fault_injection.json scenario.succession.successor_has_parent_attempt]` |
| 2:20 | Stale predecessor refusal | PREP from emitted artifact | Show `late_closeout_refusal: stale_attempt` and the corresponding invariant | Raw decision record and token | `[N: harness/out/landfall-local-demo/fault_injection.json scenario.predecessor.late_closeout_refusal]`; `[N: harness/out/landfall-local-demo/fault_injection.json invariants_observed.predecessor_closeout_fenced]` |
| 2:29 | Final read-only projection | PREP from emitted artifact and projection | Show exact final states: predecessor `expired`, successor `admitted`, independent second attempt `in_flight`; label projection aggregate and non-authoritative | Record identifiers, identities, raw counts if not required | `[N: harness/out/landfall-local-demo/fault_injection.json scenario.console_projection.expired_predecessor_observed]`; `[N: harness/out/landfall-local-demo/fault_injection.json scenario.console_projection.admitted_successor_observed]`; `[N: harness/out/landfall-local-demo/fault_injection.json scenario.console_projection.in_flight_second_item_observed]` |
| 2:43 | Structural verifier authority | PREP from emitted artifact | Show fixture-produced Set B structural scope and verifier-only terminal authority; state that this run does not establish the defect is fixed | Identity string; retain only role label | `[N: harness/out/landfall-local-demo/fault_injection.json scenario.successor_terminal.verifier_controlled]`; `[N: harness/out/landfall-local-demo/fault_injection.json scenario.successor_terminal.verdict]`; `[N: harness/out/landfall-local-demo/fault_injection.json scenario.successor_terminal.terminal_receipt_recorded]` |
| 3:05 | Registry and cross-process context | PREP | Show the local aggregate `seat_registry` catalog and the state objects that survive one process lifetime; recent activity is not labeled liveness | Seat identities, per-seat detail, production IAM inference | No numeric caption; mechanism and limitation only |
| 3:16 | Evidence scope card | PREP | Put `STRUCTURAL EVIDENCE ONLY` and `NO CUSTOMER PRODUCTION DATA` beside the cloud/local boundary | Raw fixture failure and local paths | None |
| 3:27 | Ledger | PREP | Put `UNKNOWN` rows first, then changed and survived mechanisms | Any private link or unpublished repository URL | Each numeric row requires its own `[N: <artifact path> <field>]`; omit unavailable rows |
| 3:47 | End card | PREP | Landfall, category, public repository placeholder until release | Nothing private | None |

## Capture order

1. Rehearse masking with fake values before any cloud recording.
2. Record the cloud console and probe beat in a dedicated browser profile with notifications disabled.
3. Record the actual local runner command and sanitized summary in one take with a clean terminal prompt and the persistent local label.
4. Build the local evidence panels from the emitted artifact and final read-only projection; do not recreate intermediate UI states.
5. Build prior-measurement and final-ledger cards only from accepted artifacts.
6. Perform a frame-by-frame privacy review before upload.

## Recording artifacts to retain privately

- Original untouched screen recording.
- Redacted edit project.
- Final caption file.
- Final export checksum.
- A capture manifest mapping each published numeric caption to its repository artifact path and field.

Do not commit raw screen recordings if they contain any masked value.
