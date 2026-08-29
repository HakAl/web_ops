# Devpost description draft

Status: editable draft for architect review. Do not publish.

## Project name

Landfall

## Tagline

One bounded approval starts a governed defect-triage fleet, but only a deterministic verifier can finish the work.

## Category

Fortified Enterprise Fleet

## Concise project summary

Landfall is a governed defect-triage agent fleet for a support lead, operations manager, or solo founder who can authorize bounded repair work without reviewing code. The operator approves one FleetRun envelope, then Gemini triage, supervision, worker execution, succession, and deterministic verification proceed without further human input. Workers can submit checkpoints and evidence references, but they cannot write terminal state.

The current evidence is deliberately split. A bounded real-cloud probe ran on Cloud Run with Gemini 3.7 Flash through ADK and produced the committed account-proof packet. The kill, lease-expiry, succession, stale-closeout, and verifier-completion sequence is a deterministic local governance demonstration, not a Cloud Run kill claim.

## The problem

Our disclosed prior fleet recorded [N: harness/baseline/local-baseline-2026-08-23.json v2_epoch.dispatch_count] dispatches during its frozen measurement window, and its focus-day closes clustered into [N: harness/baseline/local-baseline-2026-08-23.json focus_day.close_histogram_by_hour]. These are prior measurements of a disclosed pre-existing system, not Landfall performance.

The friction was not that a human wrote each dispatch. Every measured initiation was produced by an agent-kind actor, while the ledger recorded producers rather than session origins [N: harness/baseline/local-baseline-2026-08-23.json followup_figures.producer_kind]. The source offered no path for a seat to start itself, and the operator attests that architect sessions in that deployment were human-started except for one proxy-started seat. The practical duty cycle still followed the person at the keyboard.

For the Unlikely Hero, that means an experienced support lead can know the incident and the allowed repair boundary, yet still become the availability bottleneck because they are not a code reviewer and should not have to approve every intermediate agent decision.

## Value proposition

Landfall reduces the operator surface to one bounded authorization. The support lead chooses allowed paths, model-call and token ceilings, attempt limits, and pre-registered completion predicates before any agent acts. After that approval, the system structures incoming failures, delegates work by role, preserves authority across retries, and asks a deterministic verifier to reproduce or retrieve completion evidence.

The value is not unattended model output. It is unattended execution inside a pre-authorized envelope, with explicit refusal records when a step lacks authority or evidence.

## What Landfall does

1. A support lead approves one FleetRun envelope in plain language over pre-registered structured fields.
2. A Gemini 3.7 Flash triage seat, invoked through ADK, converts a redacted failure payload into a closed-shape directive.
3. A supervisor admits and routes work only when the envelope and reserved budget permit it.
4. Workers checkpoint and nominate artifact references within fenced attempt authority.
5. Lease expiry can fence an attempt and create a successor with parent-attempt lineage when the envelope permits another attempt.
6. A revived predecessor's authentic closeout is refused as `stale_attempt` because it no longer owns the active generation.
7. A deterministic verifier, not a model, retrieves or reproduces the evidence and alone may write an admitted or refused terminal state.
8. Missing, stale, malformed, or unresolvable evidence becomes `unknown`, which authorizes no terminal write.
9. A read-only console projects role-level progress and decisions without becoming workflow authority.

## Architectural discipline

### Fenced attempts and succession

Each work item has one active attempt and a monotonic generation. Succession requires lease expiry and a generation bump in one state transaction. Every worker effect carries its generation, so a predecessor can be refused on authority even if its closeout is genuine.

Lease expiry proves expiry, not death. A Cloud Run request timeout can return a 504 while the container continues processing, so Landfall never presents a timeout as process termination (https://cloud.google.com/run/docs/configuring/request-timeout).

### Separate worker and verifier authority

The worker holds a run token that permits checkpoint and evidence submission. The verifier never receives that token. The verifier uses a separate service authority and is the only role that can admit terminal evidence. The worker cannot write terminal state.

### Unknown is a first-class result

Evidence resolves to true, false, or unknown. Unknown enters `verification_blocked`, clears no flag, and authorizes no terminal write. The system does not coerce missing evidence into a conclusive negative.

### Transactional outbox and idempotent decisions

Firestore transaction callbacks can retry, so Landfall writes an outbox record inside the transaction and publishes outside it (https://cloud.google.com/firestore/docs/manage-data/transactions). Pub/Sub delivery is at least once, so consumers deduplicate on the stable application-owned `event_id`, never on a transport message identifier (https://cloud.google.com/pubsub/docs/subscriber).

Every application-owned enforcement point writes one idempotent decision event per logical decision. A redelivery reuses the decision identifier, which keeps refusal counts about decisions rather than transport attempts.

### Bounded spending

Landfall reserves worst-case token and call budget before attempt creation, checks ceilings at the model and tool boundary, and settles actual usage idempotently. A Cloud Billing budget is an operator alert and does not stop spend, so runtime authority depends on the in-process ceilings instead (https://cloud.google.com/billing/docs/how-to/budgets).

## Real cloud proof and local governance proof

### Demonstrated in the real-cloud vertical slice

The committed packet under `harness/evidence/account-proof/` records the bounded probe, its Cloud Run resource binding, Gemini structured output, authoritative state retrieval, an outbox that reached `sent`, consumer deduplication, and one logical effect. The probe reached Gemini 3.7 Flash through ADK on Cloud Run. Firestore held the authoritative application state, while Pub/Sub carried transport events.

This evidence does not establish that the complete worker fleet, the kill sequence, production seat identities, a scale run, or comparative measurements ran on Google Cloud. The wider production gate remains unsatisfied because `harness/evidence/account-proof/account-proof-evidence.json` records four `unknown` checks under `check_results`.

### Demonstrated in the deterministic local governance harness

The local and emulator-backed system demonstrates fenced attempts, lease expiry, atomic successor creation, parent-attempt lineage, stale predecessor closeout refusal, verifier-controlled completion, and a second work item continuing. The video and diagram label this sequence `DETERMINISTIC LOCAL GOVERNANCE DEMONSTRATION` throughout.

## Technologies used

- Gemini 3.7 Flash on Vertex AI for closed-shape triage output; the model reference documents its supported locations (https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-7-flash).
- Google Agent Development Kit for the triage agent runner (https://google.github.io/adk-docs/).
- Cloud Run for the bounded deployed probe; private service-to-service invocation uses the platform authentication path (https://cloud.google.com/run/docs/authenticating/service-to-service).
- Firestore for authoritative FleetRun, work-item, attempt, receipt, decision, and outbox state; transaction callbacks can retry (https://cloud.google.com/firestore/docs/manage-data/transactions).
- Pub/Sub for transport; subscriber delivery is at least once (https://cloud.google.com/pubsub/docs/subscriber).
- Python 3.11, FastAPI, and standard-library `unittest`.
- Cloud Build and Artifact Registry as deployment plumbing, not runtime fleet services (https://cloud.google.com/build/docs/build-push-docker-image, https://cloud.google.com/artifact-registry/docs/docker/store-docker-container-images).

Suggested `Built with` tags: `gemini-3.7-flash`, `vertex-ai`, `google-adk`, `cloud-run`, `firestore`, `pub-sub`, `python`, `fastapi`, `cloud-build`, `artifact-registry`, `google-cloud-iam`, `unittest`.

## Data sources

- Redacted, typed demo failure payloads from `demo_app/fixtures/trace_source.json`. Raw stack traces do not enter the public console, evidence artifacts, README, or video.
- Authoritative Landfall state and decision records stored by the substrate.
- Worker-nominated artifact references that the deterministic verifier retrieves or reproduces. Worker-supplied observed values are not authoritative.
- The prior-fleet manifest at `harness/baseline/local-baseline-2026-08-23.json`, disclosed as prior measurement and never presented as Landfall performance.
- The sanitized account-proof packet under `harness/evidence/account-proof/`, which omits project identifiers, service-account identities, authenticated endpoints, model payloads, and run tokens.
- Repository tests, frozen contracts, metric predicates, and the dated correction trail.

Landfall does not require public end-user data, raw customer failures, or production credentials for local testing.

## Findings and lessons learned

### Correlation is not authority

Identifiers can explain which events are related without deciding which attempt may act. Generation fencing plus a per-attempt run token supplies that missing authority.

### Determinism does not make worker-provided evidence trustworthy

A deterministic verifier over worker-supplied values can deterministically accept fabricated evidence. The verifier must retrieve or reproduce authoritative values itself.

### Managed transport does not remove application idempotency

Pub/Sub delivery is at least once, so stable logical event identifiers and consumer deduplication remain application responsibilities (https://cloud.google.com/pubsub/docs/subscriber).

### A timeout is not a death certificate

A Cloud Run request timeout can return a 504 while work continues, so the honest system fact is `lease_expired_unconfirmed` (https://cloud.google.com/run/docs/configuring/request-timeout).

### Unknown is an operational state

When evidence cannot be resolved, preserving unknown prevents a missing measurement from becoming permission to finish.

### Correction trails are part of production readiness

The design changed after focused reviews found an approval bottleneck, a transport-versus-authority error, an unfenced predecessor, an unsafe evidence boundary, and overclaims about process death and receipt integrity. Landfall keeps those corrections in the repository instead of polishing them out of the story.

## Reproducibility and testing

See the public repository README for zero-network unit checks, the emulator-backed local slice, the deterministic governance harness, and the guarded cloud deployment procedure. The judge-facing quick path is reproduced in `readme-information-architecture.md` in this draft package.

## Links

- Public code repository: `[PUBLIC_GITHUB_REPOSITORY_URL]`
- Optional hosted project: `[OPTIONAL_PUBLIC_HOSTED_PROJECT_URL]` or omit
- Public demonstration video: `[PUBLIC_YOUTUBE_OR_VIMEO_URL]`
- Public build article: `[PUBLIC_BLOG_URL]`
- Optional social post: `[OPTIONAL_SOCIAL_POST_URL]`
