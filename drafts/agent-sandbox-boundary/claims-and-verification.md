# Claims and verification: agent sandbox boundary post

Every factual claim in `post.md`, where it came from, and whether this session verified it. Status values:

- **verified**: reproduced or read directly in this session on Claude Code 2.1.259, macOS 26.6.2, 2026-09-03
- **notes**: taken from `blog-notes-stay-in-project-2026-09-03.md`, observed in the original session, not re-run here
- **other session**: reported by the operator from a different session, partly re-checked here
- **unverified**: stated with hedging in the post; needs a check before publish

| # | Claim | Source | Status | Evidence |
|---|---|---|---|---|
| 1 | Claude Code version 2.1.259, macOS 26.6.2 | `claude --version`, `sw_vers` | verified | Output in session |
| 2 | Apple M4 Pro | operator | unverified | Hostname is a MacBook Pro; chip not checked. Operator to confirm or drop |
| 3 | Sandbox default write set is cwd, added dirs, session temp dir; `$TMPDIR` set to session temp for sandboxed commands | code.claude.com/docs/en/sandboxing | verified | "Temporary directories" section and "Default write behavior" bullet |
| 4 | macOS sandbox uses Seatbelt | same docs | verified | "On macOS ... Seatbelt framework" |
| 5 | Hook behavior (four rules, script suffix list, regex for temp paths and mktemp) | `~/.claude/hooks/stay-in-project.py` | verified | Read the file |
| 6 | Hook registration matcher and 5s timeout | `~/.claude/settings.json` | verified | Read the file |
| 7 | Final global sandbox block: enabled, failIfUnavailable, autoAllowBashIfSandboxed false, allowUnsandboxedCommands false, network has only allowLocalBinding. No denyWrite, no allowMachLookup, no allowAllUnixSockets, no excludedCommands | `~/.claude/settings.json` | verified | Re-read after the operator removed allowAllUnixSockets on 2026-09-03 |
| 8 | Suite passes 26 of 26 | this session | verified | Ran `bash ~/.claude/hooks/stay-in-project.test.sh` from the repo: `pass=26 fail=0` |
| 9 | Round 1 probe table (10 rows) | notes | notes | Not re-run. Rerunning the Write and Edit probes needs a fresh session |
| 10 | Failure 1: assistant copied suite to `$TMPDIR`, operator quote | notes | notes | Quote is verbatim from notes |
| 11 | Round 2 script bypass output, four DENIED lines | notes | notes | Path `claude-501` is this machine's session prefix, replace before publish |
| 12 | Failure 2: bare `true` returned 1 with `zsh:1: operation not permitted: /tmp/claude-501/cwd-50da` | notes | notes | Cannot reproduce without adding `denyWrite` for temp, which cannot be done mid-session. Flag as version-specific in post |
| 13 | `mktemp -d` without template ignores `$TMPDIR` and tries `/var/folders` | notes | notes | Consistent with macOS mktemp behavior; not re-run |
| 14 | Round 3 table, including `tempfile` write to `/tmp/claude-501/tmp21_kcc64` | notes | notes | Not re-run |
| 15 | Pytest `tmp_path` lands in session temp; `--basetemp=.tmp/pytest` and `TMPDIR` fix it; parent `.tmp` must exist | notes | notes | Not re-run |
| 16 | Hook blocked the assistant's `cd "$TMPDIR"` while drafting this post | this session | verified | PreToolUse denial message received on a Bash call |
| 17 | Chrome fails with `Failed to create socket directory` (process_singleton_posix.cc:1043) under the sandbox | other session | verified | Reproduced with Chrome for Testing 152.0.7977.54, `--headless=new`, user-data-dir inside project |
| 18 | Chromium `base::GetTempDir` on macOS checks `MAC_CHROMIUM_TMPDIR` before `NSTemporaryDirectory()`; source comment quoted | chromium.googlesource.com, base/files/file_util_apple.mm | verified | Fetched and decoded source at main. File was renamed from file_util_mac.mm at some point; link the apple.mm path |
| 19 | With `MAC_CHROMIUM_TMPDIR` set, `SingletonSocket` lands inside the project | this session | verified | `find` showed `.ct-probe/ct/com.google.chrome.for.testing.*/SingletonSocket` and the profile symlink pointing at it |
| 20 | The `MAC_CHROMIUM_TMPDIR="$PWD/.ct" npm run a11y` command passes the hook | notes | notes | Regex reasoning is sound (no `$` before TMPDIR, `$PWD` not matched). Re-run the printf pipe before publish |
| 21 | `allowMachLookup: ["*"]` did not fix the socket directory error | other session | other session | Not re-testable mid-session. Docs confirm `"*"` matches every service and the key is about lookup |
| 22 | `allowUnixSockets` is documented in terms of connecting; `allowAllUnixSockets` "connect to every Unix socket"; default blocks every socket on macOS | settings-reference docs | verified | Quoted from the per-key sections |
| 23 | No path-scoped permission for socket creation exists | docs plus issues | verified with a caveat | Docs do not offer one. Issue #61149 (closed) reports `allowWrite` plus `allowUnixSockets` on `/var/folders` made a JVM attach socket work, which may mean directory entries cover bind. Post says "the documentation describes it in terms of connecting" and does not claim bind is impossible. Test before publish if possible |
| 24 | Issue #52471 requested path-scoped connect+bind+listen, closed 2026-05-29, state_reason not_planned, by stale bot | api.github.com | verified | Body and comments fetched |
| 25 | Issue #70762 requested wildcard for allowUnixSockets, closed 2026-08-09 by stale bot | api.github.com | verified | Body and comments fetched |
| 26 | Docs recommend `excludedCommands` for docker and Go-based CLIs that fail TLS under Seatbelt | sandboxing docs, troubleshooting | verified | Also hit live: `gh` failed with `x509: OSStatus -26276` in this session |
| 27 | Round 6: with `allowAllUnixSockets: true` and the override, the socket binds and Chrome 152 then dies at `mac_util.mm:379 Check failed: . : Operation not permitted` | this session | verified | Reproduced twice while the global switch was still on. This is the error the notes said was missing: why the socket switch did not get Chrome running |
| 28 | That check is a `sysctl` | chromium source at main | plausible | Line 379 at main is `PCHECK(sysctlbyname("kern.hv_vmm_present", ...))` in `IsVirtualMachine`. Line numbers for the 152 branch not checked. Post says "a sysctl the sandbox refuses"; soften to "appears to be" or check the 152 tag |
| 29 | headless-shell 152 and Chrome 148 die at `mach_port_rendezvous_mac.cc:159 bootstrap_check_in ... Permission denied (1100)` | this session | verified | Reproduced |
| 30 | `bootstrap_check_in` is service registration, not lookup, so `allowMachLookup` would not obviously help | reasoning from Mach API semantics | unverified | Post hedges with "would not obviously have helped". Cannot test without changing settings |
| 31 | Crashpad failed bootstrap check-in and failed to open `~/Library/Application Support/Google/Chrome for Testing/Crashpad/settings.dat` | this session | verified | In stderr of every full-Chrome run |
| 32 | The other project's AGENTS.md tells workers to report the accessibility step as unverified if it cannot launch a browser | verificationdesign AGENTS.md line 29 | verified | Read the line. The commit message for 8645fc2 says workers "do not run" it; the file itself is softer, and the post uses the file's wording |
| 33 | Sandbox settings cannot be changed mid-session; settings.json is on the protected list | this session | verified | Session sandbox description lists `~/.claude/settings.json` under denyWithinAllow |
| 34 | Operator quote "i think i have to accept and hope the agents don't jump through hoops to defy the rules" | notes | notes | Verbatim from notes |
| 35 | `allowAllUnixSockets` was removed from the global config the same day and was never the working configuration | notes, settings.json | verified | Settings re-read shows it gone; notes Round 5 says removed same day |
| 36 | Three npm scripts (`a11y`, `measure:cards`, `verify`) are in `sandbox.excludedCommands` in a local settings file, not globally | `~/dev/ai-research/.claude/settings.local.json` | verified | Found at the ai-research workspace root, one level above the verificationdesign repo. The post says "the local settings file of the workspace that runs them" for that reason. `verificationdesign/.claude/` has no settings file |
| 37 | `excludedCommands` is honored from any settings file and works with `allowUnsandboxedCommands: false` | sandboxing docs, settings reference | verified | Reference table lists scope "Any file". Sandboxing page: when the escape hatch is disabled, "all commands must run sandboxed or be explicitly listed in excludedCommands" |
| 38 | Operator quote "yeah, that's fine they are your tools that's what they're there for" | notes | notes | Verbatim from notes |
| 39 | The docs recommend `excludedCommands` for docker and for Go CLIs that fail TLS under Seatbelt | sandboxing troubleshooting | verified | Same as claim 26, now cited in Round 5 |
| 40 | That settings.local.json also contains a permissions allow list naming other repos and an MCP server | the file | verified | Not quoted in the post. Do not paste the file; the post shows only the excludedCommands block |

## Before publishing

- [ ] Replace `/Users/home` and `claude-501` with placeholders everywhere, including the four DENIED lines and the cwd file error
- [ ] Confirm or drop "Apple M4 Pro" (claim 2)
- [ ] Decide on claim 23: either test `allowUnixSockets` with a directory entry in a fresh session, or keep the hedged wording. Lower stakes now, since the socket layer was not the last wall
- [ ] Optional, would sharpen Round 6: in a fresh session with `allowMachLookup: ["*"]`, confirm Chrome still fails at `bootstrap_check_in`. That would turn "would not obviously have helped" into a verified statement (claim 30)
- [ ] Consider the notes' suggestion of a dedicated `verify:browser` script so the unsandboxed exception covers one command instead of three. Mention as a next step, not a done thing
- [ ] Check the Chromium 152 tag for the `mac_util.mm:379` line, or soften claim 28
- [ ] Re-run the printf hook check (claim 20)
- [ ] Read the verificationdesign AGENTS.md line before quoting it (claim 32)
- [ ] Add links: sandboxing docs, settings reference, Chromium `file_util_apple.mm`, issues #52471 and #70762
- [ ] State the threat model once, plainly: sound against accidental agent behavior, not against a hostile dependency or prompt injection. The post has it in Round 3; Dana to decide whether it also belongs near the top
- [ ] Hero image: 1600x800 dark, `.jpg`. Suggested subject: a fence around a directory icon with socket, port, and browser lines passing through it
- [ ] Blurb for index and home
- [ ] Nora: reread endings of the last five posts; this one ends on a plain declarative, no bolded takeaway list, matching protocol
