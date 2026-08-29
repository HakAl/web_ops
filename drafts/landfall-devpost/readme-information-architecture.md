# README information architecture and reproducibility draft

Status: editable recommendation for the future public `README.md`. Do not publish from this repository.

## Recommended visual hierarchy

The first screen should answer four questions without scrolling:

1. What is Landfall?
2. Who is the operator?
3. Which evidence ran on Google Cloud and which ran locally?
4. How can a judge reproduce the safe path?

Recommended opening stack:

1. `# Landfall`
2. One-sentence tagline.
3. Status chips: `FORTIFIED ENTERPRISE FLEET`, `REAL CLOUD PROBE`, `LOCAL GOVERNANCE HARNESS`, `DRAFT CLAIMS REVIEWED ON [DATE]`.
4. A two-column evidence boundary callout:
   - Real cloud: bounded Cloud Run probe, Gemini 3.7 Flash through ADK, account-proof packet.
   - Local: in-memory StateStore, kill, lease expiry, succession, stale closeout refusal, structural verifier evidence, and final read-only projection.
5. Architecture diagram with descriptive alt text.
6. A three-command zero-network quick start.

Avoid leading with the repository tree or a full theory section. Judges should reach the architecture and executable path before the first long prose block.

## Recommended section order

1. `What Landfall is`
2. `Evidence boundary: real cloud vs local governance`
3. `Measured problem`, with prior-system disclosure in the heading
4. `Architecture`
5. `Authority model`
6. `Discovery, lifecycle, and persisted context`
7. `Quick start: zero network`
8. `Run the emulator-backed local slice`
9. `Run the deterministic governance harness`
10. `Guarded Google Cloud deployment`
11. `Testing instructions for judges`
12. `Measured results`, with unavailable rows omitted
13. `Evidence and provenance`
14. `Privacy and security boundaries`
15. `Repository map`
16. `Hackathon disclosure and license`

## Copy-ready quick start

### Prerequisites

- Python 3.11 or newer.
- Git.
- For the optional local integration slice: a Java runtime plus the Google Cloud CLI components required by the official Firestore emulator and Pub/Sub emulator guides (https://cloud.google.com/firestore/docs/emulator, https://cloud.google.com/pubsub/docs/emulator).
- For deployment only: a Google Cloud account, an explicitly selected project with billing, and the Google Cloud CLI. Deployment can incur charges (https://cloud.google.com/billing/docs/how-to/modify-project).

### Zero-network unit and invariant checks

```bash
git clone [PUBLIC_GITHUB_REPOSITORY_URL]
cd landfall
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --editable .
python3 -m unittest discover -s tests -t . -v
python3 scripts/verify.py
```

The core package has no runtime dependency outside the Python standard library. These commands make no Google Cloud API call and no model call.

Expected acceptance language: both commands exit successfully. Do not publish suite, test, or check counts unless a named harness artifact records them.

### Emulator-backed local slice

Install the optional clients:

```bash
python3 -m pip install --editable '.[emulator]'
```

Start the official emulators in separate shells. Firestore emulator setup is documented at https://cloud.google.com/firestore/docs/emulator, and Pub/Sub emulator setup is documented at https://cloud.google.com/pubsub/docs/emulator.

```bash
gcloud beta emulators firestore start --host-port=127.0.0.1:8080
```

```bash
gcloud beta emulators pubsub start --host-port=127.0.0.1:8085
```

In the test shell, remove any production credential or project variables before selecting the explicit fake local profile:

```bash
unset GOOGLE_APPLICATION_CREDENTIALS GOOGLE_CLOUD_PROJECT GCLOUD_PROJECT CLOUDSDK_CORE_PROJECT
export FIRESTORE_EMULATOR_HOST=127.0.0.1:8080
export PUBSUB_EMULATOR_HOST=127.0.0.1:8085
export LANDFALL_LOCAL_PROJECT=landfall-local
python3 -m substrate.run_slice
```

This slice exercises the state transaction, outbox relay, Pub/Sub emulator delivery, logical-event deduplication, and verifier admission (https://cloud.google.com/pubsub/docs/emulator). It is a local emulator result and does not satisfy real-cloud acceptance.

### Deterministic governance harness

Run the accepted local fault-injection entrypoint:

```bash
python3 -m harness.fault_injection \
  --output-root harness/out \
  --fleet-run-id landfall-local-demo
```

Expected artifact: `harness/out/landfall-local-demo/fault_injection.json`.

The runner uses an in-memory StateStore, not Firestore. Its emitted artifact records the predecessor ending `expired`, the recovered successor ending `admitted`, and an independent second attempt ending `in_flight`. It also records lease expiry, atomic succession, parent-attempt lineage, stale predecessor closeout refusal, and verifier-only terminal authority over fixture-produced structural results. This run demonstrates governance over structural evidence; it does not establish that the defect is fixed.

Use these source-bound captions until the architect accepts the artifact:

- Predecessor final observation: `[N: harness/out/landfall-local-demo/fault_injection.json scenario.console_projection.expired_predecessor_observed]`.
- Successor final observation: `[N: harness/out/landfall-local-demo/fault_injection.json scenario.console_projection.admitted_successor_observed]`.
- Independent attempt final observation: `[N: harness/out/landfall-local-demo/fault_injection.json scenario.console_projection.in_flight_second_item_observed]`.
- Verifier-controlled terminal authority: `[N: harness/out/landfall-local-demo/fault_injection.json scenario.successor_terminal.verifier_controlled]`.

Do not add correctness predicates such as `repro_fails_at_base`, `repro_passes_at_candidate`, or `suite_no_regression` unless a separate accepted artifact records them.

### Discovery, lifecycle, and persisted context

- `seat_registry` is a closed catalog of approved role, lifecycle state, and deployed revision.
- Its console representation is aggregate, read-only, and non-authoritative.
- Recent activity is derived from attempts and decisions. It is not proof of continuous liveness.
- FleetRun, work-item, attempt, lease, generation, receipt, decision, and outbox records carry governed context across process lifetimes.
- Production per-seat IAM enforcement remains unknown. Do not infer it from the local registry or application authority tests.
- Public demonstrations use redacted typed fixture payloads, not customer production data.

## Guarded Google Cloud deployment

### What the public instructions should promise

The deployment path is project-specific, mutating, and potentially billable. The README should make the inspection path easy, then require an explicit handoff before each mutating phase. It must not publish project identifiers, service-account identities, the private probe endpoint, or operator environment values.

Cloud Build builds the container image (https://cloud.google.com/build/docs/build-push-docker-image), Artifact Registry stores it (https://cloud.google.com/artifact-registry/docs/docker/store-docker-container-images), and these remain deployment plumbing rather than runtime fleet services.

### Cloud prerequisites

- Google Cloud CLI installed and authenticated with an operator identity authorized to create the declared resources.
- A dedicated project selected explicitly in the active CLI configuration.
- Billing enabled and spend authorization reviewed.
- The exact required environment-variable set filled from a private operator worksheet, never committed.
- No service-account key file and no plaintext run token in the environment.
- Exact deployment pins retained from `deploy/requirements.txt`.

The public README may list variable names, but never values:

```text
LANDFALL_PROJECT_ID
LANDFALL_PROJECT_NUMBER
LANDFALL_BILLING_ACCOUNT
LANDFALL_REGION
LANDFALL_VERTEX_LOCATION
LANDFALL_TRIAGE_MODEL_ID
LANDFALL_WORKER_MODEL_ID
LANDFALL_ARTIFACT_REPOSITORY
LANDFALL_PROBE_IMAGE
LANDFALL_WORK_TOPIC
LANDFALL_WORK_SUBSCRIPTION
LANDFALL_DEAD_LETTER_TOPIC
LANDFALL_DEAD_LETTER_SUBSCRIPTION
LANDFALL_MAX_MODEL_CALLS
LANDFALL_MAX_MODEL_TOKENS
LANDFALL_WORST_CASE_TOKENS_PER_CALL
LANDFALL_TRIAGE_SA_ID / LANDFALL_TRIAGE_SA_EMAIL
LANDFALL_SUPERVISOR_SA_ID / LANDFALL_SUPERVISOR_SA_EMAIL
LANDFALL_WORKER_SA_ID / LANDFALL_WORKER_SA_EMAIL
LANDFALL_VERIFIER_SA_ID / LANDFALL_VERIFIER_SA_EMAIL
LANDFALL_RELAY_SA_ID / LANDFALL_RELAY_SA_EMAIL
LANDFALL_CONSOLE_READER_SA_ID / LANDFALL_CONSOLE_READER_SA_EMAIL
```

### Inspect before mutation

```bash
python3 -m deploy.live_ports inspect
```

The default inspection path executes no deployment subprocess. Review the rendered plan, resource scope, service shape, spend ceilings, and IAM assignments before continuing.

### Execute the reviewed phases

Only an authorized operator should run these commands, and only after the dry-run plan matches the reviewed environment:

```bash
python3 -m deploy.live_ports bootstrap --apply --credit-authorized
```

After the deployed private service is observed, set `LANDFALL_PROBE_PUSH_ENDPOINT` in the private operator environment. Never paste its value into documentation, screenshots, logs, or Devpost.

```bash
python3 -m deploy.live_ports push --apply --credit-authorized --bootstrap-complete
```

Run the bounded account proof only after both handoffs are true:

```bash
python3 -m deploy.account_proof run --apply --credit-authorized --bootstrap-complete --push-complete
```

Recovery commands are state-specific and must not be used as generic retries. Link to `deploy/README.md` for the reviewed recovery actions and their required handoffs.

### Cloud evidence boundary

The committed `harness/evidence/account-proof/` packet supports the bounded Cloud Run, Gemini through ADK, Firestore, and Pub/Sub account proof (https://cloud.google.com/run/docs/overview, https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-7-flash, https://google.github.io/adk-docs/, https://cloud.google.com/firestore/docs/overview, https://cloud.google.com/pubsub/docs/overview). It does not support a complete production-fleet, scale, cloud kill-sequence, cloud unit-economics, or production seat-identity claim. The broader gate remains false while any preregistered check is unknown.

## Copy-ready judge testing section

### Fast path

```bash
python3 -m unittest discover -s tests -t . -v
python3 scripts/verify.py
```

### Architecture path

1. Read `docs/contracts-landfall-2026-08-23.md` for fencing, state transitions, evidence authority, and budget rules.
2. Inspect `harness/evidence/account-proof/manifest.json` for the sanitized real-cloud packet and file hashes.
3. Run the emulator-backed slice above.
4. Run `python3 -m harness.fault_injection --output-root harness/out --fleet-run-id landfall-local-demo` and inspect `harness/out/landfall-local-demo/fault_injection.json`.
5. Compare its result only with the local governance claims in the README and video.

No judge needs a private endpoint, service-account credential, raw failure, or run token.

## Diagram placement and alt text

Place the architecture diagram immediately after the evidence-boundary callout. Link the image to the full-resolution SVG.

Suggested alt text:

> A support lead authorizes one FleetRun. The highlighted real-cloud lane connects Cloud Run, ADK and Gemini, authoritative cloud state in Firestore, an outbox relay, and Pub/Sub. A separate outlined local lane connects the supervisor, fenced workers, successor lineage, stale closeout refusal, a deterministic verifier, a seat registry, and a read-only console to an in-memory StateStore. The two runtime lanes share an abstract state contract, not a datastore. The local final projection shows the predecessor expired, successor admitted, and independent attempt in flight.

## Result-table discipline

- Put `Unknown or not measured` before `Passed`.
- Use one row per predicate, not a combined success score.
- Include artifact path and field in the same row as every number.
- Label local worker-attested evidence and Landfall verifier-controlled evidence as different tiers.
- Label prior-fleet units per dispatch attempt and Landfall units per work item; never subtract or compare them as the same unit.
- Remove any unresolved placeholder row at finalization rather than filling it with an estimate.
