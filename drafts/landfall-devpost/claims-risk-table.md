# Landfall claims-risk table

Status: architect review register. Do not publish this draft as project copy.

Disposition meanings:

- `KEEP`: supported in its bounded wording.
- `PLACEHOLDER`: keep editable but do not publish until the named artifact and field exist.
- `CUT`: remove at finalization if evidence remains unavailable.
- `BLOCK`: do not record or publish the dependent asset until resolved.
- `PROHIBITED`: do not use even if nearby evidence appears suggestive.

| Proposed statement | Current evidence | Risk | Disposition | Required final action |
| --- | --- | --- | --- | --- |
| A bounded Cloud Run probe used Gemini 3.7 Flash through ADK and produced the committed account-proof packet. | `harness/evidence/account-proof/account-proof-evidence.json` → `check_results.prod.gemini_structured_output`; `cloud-binding-evidence.json` → `findings`; `manifest.json` → `files` | Could be broadened into a fleet claim | KEEP | Retain `bounded probe` and never replace it with `complete fleet` |
| The basic real-cloud account proof passed. | Hash-bound proof and binding files exist in `harness/evidence/account-proof/` | Must stay distinct from the production-fleet gate | KEEP | State beside the wider gate status |
| The wider production-fleet gate passed. | `account-proof-evidence.json` → `check_results` has one passed check and four unknown checks | False under current evidence | PROHIBITED | Do not publish unless all preregistered checks later pass from evidence |
| Real Firestore transaction retry and lost-outcome reread passed in production (https://cloud.google.com/firestore/docs/manage-data/transactions). | `check_results.prod.txn_retry_reread = unknown` | Unknown could be mistaken for false or pass | CUT | Remove unless an accepted production artifact resolves the check |
| Pub/Sub republication produced distinct transport identifiers for one logical event in production (https://cloud.google.com/pubsub/docs/subscriber). | `check_results.prod.pubsub_republish = unknown`; current proof observed a single delivery | Local emulator evidence does not prove production behavior for this run | CUT | Remove unless an accepted production artifact resolves the check |
| Authenticated Cloud Run push reused the logical decision identifier in production (https://cloud.google.com/pubsub/docs/authenticate-push-subscriptions). | `check_results.prod.cloud_run_push_auth = unknown` | Resource privacy does not establish decision reuse | CUT | Remove unless an accepted production artifact resolves the check |
| Production per-seat identities enforce the worker and verifier split. | `check_results.prod.per_seat_identity = unknown`; current IAM plan notes application-owned enforcement points | Could imply an IAM guarantee that has not passed | CUT | Keep authority split as an application-owned enforcement mechanism only |
| The console reader holds no write role on the production path shown. | Current per-seat or console IAM acceptance evidence is unresolved | Local capability boundary is not production IAM proof | CUT | Remove production IAM wording; retain `read-only, non-authoritative projection` as implemented-local wording |
| The complete worker fleet ran on Google Cloud. | Not established by the bounded probe | Central overclaim | PROHIBITED | Never use without a new accepted artifact that explicitly establishes it |
| The kill and succession sequence ran on Cloud Run (https://cloud.google.com/run/docs/configuring/request-timeout). | The sequence is local or hybrid only | Central mandatory claim split | PROHIBITED | Label every frame and sentence `DETERMINISTIC LOCAL GOVERNANCE DEMONSTRATION` |
| A Cloud Run worker's process state was known after lease expiry. | Lease state cannot prove process death; Cloud Run timeout behavior is documented at https://cloud.google.com/run/docs/configuring/request-timeout | False causal claim | PROHIBITED | Use `lease expiry proves expiry, not death` |
| Attempt N was killed locally, successor N+1 recorded its parent, stale closeout was refused, and another item continued. | Final kill artifact path and verdict fields not yet named in this packet | Demo could become a rehearsed animation without evidence | BLOCK | Record the live beat only after `[N: <harness kill output path> <verdict fields>]` exists |
| The verifier reproduced a failing base, passing candidate, and non-regressing suite. | Final verifier artifact path and fields not yet named | Would overstate correctness if only structural predicates ran | PLACEHOLDER | Use `[N: <harness verifier output path> <fields>]`; otherwise use the structural-evidence cut language |
| Landfall elapsed time per verified fix is a measured value. | No accepted measured-run output is named | Missing numeric evidence | CUT | Remove the result row and spoken sentence unless an exact artifact field lands |
| Landfall token use per verified fix is a measured value. | No accepted measured-run output is named | Missing numeric evidence | CUT | Remove the result row and spoken sentence unless an exact artifact field lands |
| Landfall retrospective currency per verified fix is a measured value. | No accepted cloud measured-run output is named; broader production gate is not satisfied | Could turn delayed billing evidence into a runtime claim | CUT | Remove unless the full gate passes and an exact billing-normalized artifact field lands |
| Landfall sustained a measured cloud scale run. | Cloud scale run is not established and remains cut-list work | Production-readiness overclaim | PROHIBITED | Do not use |
| The prior fleet recorded a dispatch total in the frozen measurement window. | `harness/baseline/local-baseline-2026-08-23.json` → `v2_epoch.dispatch_count` | Could be read as Landfall performance | KEEP | Keep the source field and the prior-measurement disclosure in the same frame or paragraph |
| The prior focus-day closes had a clustered hourly shape. | Baseline manifest → `focus_day.close_histogram_by_hour` and `histogram_note` | The histogram supports timing shape, not session origin by itself | KEEP | Present with the three labeled initiation layers, not as standalone causal proof |
| Every prior-fleet initiation was human-authored. | Baseline producer split says agent-produced | False mechanism | PROHIBITED | Say every measured initiation was agent-produced; separate source structure and operator attestation |
| Prior-fleet terminal coverage and Landfall verifier coverage are the same evidence tier. | Baseline manifest distinguishes worker-attested from verifier-controlled | Invalid comparison | PROHIBITED | Show tiers side by side and compare only terminal-reached level where applicable |
| Prior-fleet and Landfall unit economics use the same unit. | Prior system is per dispatch attempt; Landfall design is per work item spanning attempts | Invalid denominator | PROHIBITED | Label units separately and never subtract them |
| The receipt chain is protected against alteration by an independent anchor. | Current design has a shared mutable writer and no external anchor | Would overclaim integrity | PROHIBITED | Use `hash-linked and internally consistency-checked` only |
| Cloud transport guarantees one delivery. | Pub/Sub subscriber delivery is at least once (https://cloud.google.com/pubsub/docs/subscriber) | Forbidden transport claim | PROHIBITED | Use `at least once` and name application-owned deduplication |
| The console proves truth. | Console is a projection and can misrender | Overstates a read surface | PROHIBITED | Use `read-only and non-authoritative` |
| Unknown evidence means the predicate failed. | Frozen contract maps unknown to non-terminal `verification_blocked` | Would collapse a core state distinction | PROHIBITED | Use `unknown authorizes no terminal write` |
| Public hosted application is available. | No public URL supplied | Could expose a private authenticated endpoint | CUT | Omit the optional field unless a separate public judge-safe URL exists |
| Public GitHub repository is available. | Publication planned for Sunday | Submission blocker | BLOCK | Insert `[PUBLIC_GITHUB_REPOSITORY_URL]` only after public visibility and clean-clone verification |
| Public demonstration video is available. | Not yet recorded or uploaded | Required submission blocker | BLOCK | Insert `[PUBLIC_YOUTUBE_OR_VIMEO_URL]` only after public visibility and runtime check |
| Public build article is available. | Web Ops draft remains unpublished | Optional bonus blocker | PLACEHOLDER | Insert `[PUBLIC_BLOG_URL]` only after architect review and publication |
| Public social post is available. | Draft only | Optional bonus blocker | PLACEHOLDER | Insert `[OPTIONAL_SOCIAL_POST_URL]` only after publication and hashtag verification |

## Final provenance pass

The architect’s final checker should scan every public artifact together: Devpost description, README, architecture export, subtitles, video captions, blog, and social post. A claim removed from prose but left in a diagram label or subtitle is still a published claim.
