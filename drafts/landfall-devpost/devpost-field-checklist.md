# Devpost field checklist

Status: editable submission shell. Do not publish.

## Public project page

| Devpost field | Draft value or source | Gate before entry |
| --- | --- | --- |
| Project name | `Landfall` | Ready |
| Tagline | `One bounded approval starts a governed defect-triage fleet, but only a deterministic verifier can finish the work.` | Architect wording review |
| About the project | Paste from `devpost-description.md`, starting at `The problem` | Claims-risk review and final placeholder cuts |
| Built with | Gemini 3.7 Flash, Vertex AI, Google ADK, Cloud Run, Firestore, Pub/Sub, Python, FastAPI, Cloud Build, Artifact Registry, Google Cloud IAM, unittest | Confirm final public README uses the same pins |
| Try it out: source | `[PUBLIC_GITHUB_REPOSITORY_URL]` | Public repository planned for Sunday |
| Try it out: hosted app | `[OPTIONAL_PUBLIC_HOSTED_PROJECT_URL]` or omit | Must be public and judge-accessible; never use the private authenticated probe endpoint |
| Gallery image: architecture | `architecture-diagram.svg`, with PNG export if Devpost rejects SVG | Export PNG at 3:2 or upload under the dedicated architecture field |
| Gallery still: one approval | Prepared envelope screen | Mask all forbidden values |
| Gallery still: real cloud | Cloud Run proof frame | Mask project, identity, endpoint, billing, and account details |
| Gallery still: local succession | Prepared local harness frame labeled `DETERMINISTIC LOCAL GOVERNANCE DEMONSTRATION` | Numeric caption requires its named artifact |
| Video demo link | `[PUBLIC_YOUTUBE_OR_VIMEO_URL]` | Public, not unlisted; four minutes or shorter; English narration or subtitles |

## Judge and organizer fields

| Devpost field | Draft value or source | Gate before entry |
| --- | --- | --- |
| Sponsor or special prizes | `[SELECT_APPLICABLE_PRIZE_OPTIONS]` | Entrant decision |
| Submitter type | `[INDIVIDUAL_TEAM_OR_ORGANIZATION]` | Entrant decision |
| Country of residence | `[SUBMITTER_COUNTRY]` | Entrant supplies privately in Devpost |
| Category | `Fortified Enterprise Fleet` | Select exactly this one category |
| Organization name | `[ORGANIZATION_NAME_IF_APPLICABLE]` | Omit unless submitting for an organization |
| Project start date | `[PROJECT_START_DATE_WITHIN_SUBMISSION_PERIOD]` | Verify against repository history and contest rule |
| Code repository URL | `[PUBLIC_GITHUB_REPOSITORY_URL]` | Public repository planned for Sunday |
| Reproducible README instructions | `Yes` after the local and cloud sections from `readme-information-architecture.md` land | Run all copied commands before selecting Yes |
| Hosted project URL | `[OPTIONAL_PUBLIC_HOSTED_PROJECT_URL]` or blank | Do not expose an authenticated endpoint |
| Testing instructions | Paste `Judge testing instructions` below | Final command rehearsal on clean clone |
| Google SDK | `Google Agent Development Kit 2.7.1` | Confirm public dependency pin |
| Google Cloud services | `Cloud Run; Firestore; Pub/Sub; Vertex AI` | Runtime list; label Cloud Build, Artifact Registry, IAM, and Billing as deployment or evidence plumbing if mentioned |
| Architecture diagram | Upload PNG, JPG, JPEG, PDF, PPT, or PPTX export from `architecture-diagram.svg` | Devpost field does not list SVG; export and inspect a supported format |
| Google AI model | `Gemini 3.7 Flash` | Confirm final deployment evidence and public model pin |
| Optional public content URL | `[PUBLIC_BLOG_URL]` | Publish later; article must state it was created for this hackathon |
| Optional social URL | `[OPTIONAL_SOCIAL_POST_URL]` | Publish later; post must contain `#AllThingsAgenticHackathon` |

## Judge testing instructions

Landfall has three testing levels with different evidence meanings:

1. **Zero-network checks:** clone `[PUBLIC_GITHUB_REPOSITORY_URL]`, create a Python 3.11 virtual environment, install the local package, run `python3 -m unittest discover -s tests -t . -v`, then run `python3 scripts/verify.py`. These checks require no cloud credentials and make no model call.
2. **Local emulator slice:** install the `emulator` extra, start the official Firestore and Pub/Sub emulators, export only the documented local fake-project variables, and run `python3 -m substrate.run_slice`. This demonstrates the state, outbox, transport, deduplication, and verifier path locally. It is not cloud acceptance.
3. **Evidence review:** inspect `harness/evidence/account-proof/manifest.json` and its hash-bound packet for the bounded real-cloud probe. Inspect the local harness artifact named in the final README for the kill and succession result. Do not use a private endpoint or credentials.

The complete command blocks and prerequisite links are in `readme-information-architecture.md`. If a hosted public judge path is not available, omit the hosted URL and rely on the public repository, reproducible tests, evidence packet, and video.

## Publication and privacy gate

- [ ] No project identifier or project number is visible.
- [ ] No service-account identity is visible.
- [ ] No private or authenticated endpoint is visible or linked.
- [ ] No run token, access token, cookie, header, environment value, or credential file is visible.
- [ ] No raw failure, stack trace, actor name, seat name, or local filesystem path is visible.
- [ ] No per-actor measurement is present.
- [ ] Every prior-fleet number is labeled as prior measurement of a disclosed pre-existing system.
- [ ] Every numeric result retains `[N: <artifact path> <field>]` until provenance acceptance.
- [ ] Every Google service behavior sentence contains an official Google documentation URL.
- [ ] The cloud and local demonstration beats are visibly separate.
- [ ] The local kill beat never uses Cloud Run footage as its background.
- [ ] The video is public on YouTube or Vimeo, English-accessible, and no longer than four minutes.
- [ ] The repository is public and its README commands were rerun from a clean clone.
- [ ] Architect has reviewed `claims-risk-table.md` and resolved every `CUT` or `BLOCK` row.
