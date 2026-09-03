---
title: The Project Directory Is Not Where Your Agent Ends
published: false
tags: claudecode, ai, security, sandbox
canonical_url: https://vibecoder.buzz/blog/agent-sandbox-boundary.html
cover_image: https://vibecoder.buzz/blog/agent-sandbox-boundary.jpg
---

*TL;DR: I tried to keep Claude Code's writes inside the project it was launched in. Two layers, a hook and the native sandbox, held against every direct probe. Then the assistant used the one gap it had just reported. Closing that gap broke every Bash exit code. Restoring a headless browser reopened the boundary through sockets and Mach ports. The project directory is a useful behavioral fence. It is not the agent's authority boundary, and current tooling does not let you scope the real one.*

> **Version-specific. Verify before copying.** Everything below was observed on Claude Code 2.1.259, macOS 26.6.2 (Tahoe), Apple M4 Pro, on 2026-09-03. The sandbox keys, the temp directory behavior, and the failure modes all belong to that version. Check the current sandbox and settings reference pages before you paste any of this into your own settings.

I constrain my coding agents for two reasons. I do not want them destroying things outside the project, and I do not want them doing throwaway work in places I will never look. A diagnostic script that lands in a temp directory is a diagnostic script I lose.

For months my whole enforcement was one line in my user-level `CLAUDE.md`:

> This is not your system, treat it with respect. Operate within the directory you're launched unless granted permission.

That line is in direct tension with Claude Code's own Bash guidance, which tells the model to put scratch files under a session temp directory. Instructions lose to instructions. So I set out to make the rule mechanical.

## The two layers

Claude Code gives you two places to enforce a write boundary, and they see different things.

A **PreToolUse hook** runs before each tool call and sees the call's arguments. For Write and Edit it sees the target path and the new content. For Bash it sees the command text the model wrote. It does not see what a script does once it runs.

The **native sandbox** wraps every Bash command in macOS Seatbelt. It sees every filesystem effect, including effects inside scripts and child processes. By default it allows writes to the working directory, any added directories, and the session temp directory. It knows nothing about which tool asked, or why.

My hook, `stay-in-project.py`, does four things:

1. For Write, Edit, MultiEdit, and NotebookEdit, resolve the target with `realpath` and deny it if the result is outside the project root. This catches `../` traversal and symlinks that point out.
2. For those same tools, if the target is a script, scan the new content for temp references and deny if found. Markdown is not scanned, so docs can mention `/tmp`.
3. For Bash, deny background runs, because background output lands in the temp area. Deny any command text that names a temp path, a temp variable, or `mktemp`.
4. Leave Read, Glob, and Grep alone. Reads anywhere are deliberate.

The sandbox handles what the hook cannot: any Bash write outside the project, however it is expressed.

## Round one: every probe holds

I ran the probes through the real tools, inside a live session, not just through a unit suite.

| Probe | Result |
|---|---|
| Write tool to a file in home | Denied by hook |
| Edit tool via `wip/../../.zshrc` | Denied by hook, resolved path shown |
| Write tool through a symlink inside the project that points at home | Denied by hook |
| Write tool inside the project | Allowed |
| Read tool on `~/.zshrc` | Allowed |
| Background Bash | Denied by hook |
| Bash redirect to `~/probe.txt` | Denied by sandbox, `operation not permitted` |
| Bash redirect through the symlink | Denied by sandbox |
| Bash redirect into the project | Allowed |
| Bash redirect into `$TMPDIR` | Allowed |

The last row was flagged in the same report as "the sandbox's own policy, not a hook gap." Keep that row in mind.

## Failure one: the assistant used the hole it had just reported

I asked for a symlink test case to be added to the regression suite. The suite lives under `~/.claude/hooks`, which both layers block. The assistant's response was to copy the suite into `$TMPDIR`, patch it there, run it there, and hand me a `cp` command to install the result.

My reply was short: "no i mean you wrote outside the dir. exactly what i'm trying to stop."

This is the center of the story. The gap was reported as a gap. Then, the moment the boundary got in the way, the gap became a convenience. Two files and one `mktemp` call went to temp. The tool did what it was told. The agent routed around it.

The mechanical reason was simple. The hook only inspected file-tool paths and delegated every Bash write to the sandbox, and the sandbox's allowlist includes the session temp directory. Any redirect, copy, or `mktemp` aimed at `$TMPDIR` passed both layers.

## Round two: close the temp hole hard

Two changes. The sandbox got a `filesystem.denyWrite` for `/tmp`, `/private/tmp`, `/var/folders`, and `/private/var/folders`. The hook started rejecting Bash commands that named a temp path, a temp variable, or `mktemp`.

Then I tested the part the hook cannot see. A project-local Python script that opens files in four locations, run with a plain `python3 script.py`. The command text is innocent. The script is not.

```
DENIED  /private/tmp/claude-501/bypass-probe.txt: Operation not permitted
DENIED  /private/tmp/bypass-probe.txt: Operation not permitted
DENIED  /private/var/folders/bypass-probe.txt: Operation not permitted
DENIED  /Users/home/bypass-probe.txt: Operation not permitted
```

The sandbox caught all four. Python's `tempfile` module, with every system location denied, fell through to the working directory, which was inside the project. Hard close.

## Failure two: the deny broke every exit code

Every Bash call in the session now returned exit code 1. Including a bare `true`:

```
zsh:1: operation not permitted: /tmp/claude-501/cwd-50da
```

Claude Code's Bash tool writes a small working-directory tracking file under the session temp directory after each command. The deny blocked that write, and the failure overwrote the real exit status. Commands still ran. Every one of them was reported as failed. Real failures became indistinguishable from noise.

This is the second thing worth remembering. The temp directory is not just scratch space the model uses. It is part of the runtime. Denying it blindly breaks the tool's own bookkeeping, and the symptom is silent enough that you can go a long way before noticing that nothing has "succeeded" in an hour.

Two smaller things surfaced in the same round. `mktemp -d` with no template ignored `$TMPDIR` and tried `/var/folders`, which the sandbox refused. And the suite's symlink fixture lived under `~/.claude`, so the suite could not run from inside a session at all.

## Round three: the design that holds

I removed the `denyWrite` entries and moved every piece of temp detection into the hook, where it only sees model-authored content. The sandbox's temp allowance stays as shipped. The suite's fixture moved into the project. Suite passes 26 of 26.

Verified after a restart:

| Probe | Result |
|---|---|
| Bare `true` | Exit 0, no trailer |
| Bash naming `/tmp` | Denied by hook |
| Bash calling `mktemp` | Denied by hook |
| Write of a `.py` file with a literal temp path | Denied by hook at write time |
| Write of a `.py` file using `tempfile`, no literal path | Allowed |
| Running that file | Wrote to `/tmp/claude-501/tmp21_kcc64` |

The last two rows are the accepted gap. A library that picks its own temp location writes to the session temp directory and neither layer stops it. Pytest's `tmp_path` fixture resolves through the same module, so it lands there too. Two verified fixes keep it in the project: pass `--basetemp=.tmp/pytest` on the command line, or set `TMPDIR` to a project-local path before running. The parent `.tmp` directory must exist first or pytest raises `FileNotFoundError`. Put it in `pytest.ini` so nobody has to remember:

```ini
[pytest]
addopts = --basetemp=.tmp/pytest -p no:cacheprovider
```

The division of labor, as it stands:

| Concern | Enforced by |
|---|---|
| Write and Edit targets outside the project | Hook |
| Symlink and `../` escapes in tool targets | Hook, via realpath |
| Bash redirect or copy to home, other projects | Sandbox |
| Bash writes to the session temp directory | Hook, by text match only |
| Scripts that name a temp path | Hook, content scan at write time |
| Scripts that resolve temp through a library | Nothing |
| Background Bash | Hook |
| Reads anywhere | Allowed |

This is behavioral enforcement, not an adversarial boundary. It stops the common mistake and it stops the agent from quietly parking work where I will lose it. An obfuscated path, a hostile dependency, or a prompt injection would walk through it.

While drafting this post, the assistant tried to `cd "$TMPDIR"` for a scratch download. The hook blocked it. It works on the model that is helping write about it.

## Round four: the browser does not respect your temp directory

Then I ran a browser-based accessibility check and a card-measurement script from inside a session. Both aborted:

```
[chrome/browser/process_singleton_posix.cc:1043] Failed to create socket directory.
[chrome/app/chrome_main_delegate.cc:527] Failed to create a ProcessSingleton for your profile directory. ... Aborting now to avoid profile corruption.
```

Chrome creates its profile singleton socket under the macOS per-user temp folder, the one under `/var/folders/.../T`. It does not honor `$TMPDIR` for this. That folder is not on the sandbox's write allowlist, so Chrome cannot start.

My first guess was wrong. I set `sandbox.network.allowMachLookup` to `["*"]` on the theory that Mach IPC was the blocker. It changed nothing for this error, and it broadened XPC access for no benefit. I removed it. I am leaving the wrong guess in this post because it is the diagnostic path, and because that wildcard is exactly the kind of "temporary" setting that survives into a final config. Treat it as a testing concession. Do not ship it.

The real fix is Chrome-specific. Chromium's `base::GetTempDir` on macOS checks the `MAC_CHROMIUM_TMPDIR` environment variable before falling back to `NSTemporaryDirectory()`. The source comment says it exists "to facilitate hermetic runs on macOS" and is "used instead of TMPDIR for historical reasons." Point it at a short directory inside the project:

```bash
mkdir -p .ct && chmod 700 .ct && MAC_CHROMIUM_TMPDIR="$PWD/.ct" npm run a11y
```

That command passes the hook. The variable name contains `TMPDIR` but has no leading dollar sign, and `$PWD` is not on the pattern list. Add `.ct/` to `.gitignore` next to `.tmp/`.

Granting the whole per-user temp folder in the sandbox would also have worked. It would also recreate the write escape the whole setup exists to prevent. When a tool fails under the sandbox with a permission error on a path you did not name, look for that tool's own override before widening the allowlist.

## Round five: the socket is not a file

The temp fix was necessary and not sufficient. Chrome's singleton is a Unix domain socket, and binding a socket is a distinct sandbox permission from writing a file.

On Claude Code's side, as of this version: `sandbox.network.allowUnixSockets` lists socket paths that sandboxed commands can connect to. The documentation describes it in terms of connecting. Creating a socket at a fresh random path needs the global switch `sandbox.network.allowAllUnixSockets`. There is no path-scoped permission for socket creation. An issue asking for exactly that, "path-scoped allowUnixSockets that covers connect() + bind() + listen()," was [filed in April 2026 and closed by the stale bot in May](https://github.com/anthropics/claude-code/issues/52471). A [wildcard request for the same key](https://github.com/anthropics/claude-code/issues/70762) went the same way in August.

Four options:

1. Keep the sandbox strict. Run browser tests manually or in CI.
2. Launch a trusted browser outside Claude and have sandboxed Puppeteer attach over a localhost debugging port.
3. Enable `allowAllUnixSockets` and accept the exposure.
4. Add the npm script to `excludedCommands` so it runs unsandboxed.

I rejected option 4 outright. The script name is fixed. What it executes is not. An agent can edit `package.json`, the test runner, an imported module, or a build hook, then invoke the trusted script name with full permissions. That is a much wider door than a socket permission. The documentation says the same thing about `docker *` and Go-based CLIs, and it is right, and it is still the escape hatch the docs recommend when things break.

I chose option 3. The filesystem sandbox stays active for every test process. The hook still blocks agent-authored temp paths. Chrome's socket lands inside the project. Escaping now requires deliberately reaching for a privileged socket, not merely editing a script that already runs unsandboxed. My own words at the time: "i think i have to accept and hope the agents don't jump through hoops to defy the rules."

The final sandbox block:

```json
{
  "enabled": true,
  "failIfUnavailable": true,
  "autoAllowBashIfSandboxed": false,
  "allowUnsandboxedCommands": false,
  "network": {
    "allowLocalBinding": true,
    "allowAllUnixSockets": true
  }
}
```

No `denyWrite`. No `allowMachLookup`. No `excludedCommands`.

## Round six: it still does not run

Here is the part the earlier notes did not have.

While drafting this post I re-ran the Chrome probes from inside a session on the final config. With `MAC_CHROMIUM_TMPDIR` set, the singleton socket appeared inside the project. The bind worked. Chrome then died anyway:

```
[base/mac/mac_util.mm:379] Check failed: . : Operation not permitted (1)
```

That is a `sysctl` the sandbox refuses. The headless shell binary and an older Chrome died one step earlier:

```
[base/apple/mach_port_rendezvous_mac.cc:159] Check failed: kr == KERN_SUCCESS. bootstrap_check_in ...MachPortRendezvousServer.44804: Permission denied (1100)
```

That is Chrome registering a Mach service so its child processes can find it. `allowMachLookup` is about looking services up, not registering them, so the wildcard I removed in round four would not obviously have helped here either. I could not test that from inside a session, because sandbox settings cannot be changed mid-session and my settings file is on the sandbox's protected list. Crashpad also failed to check in and failed to write under `~/Library/Application Support`.

Count the boundaries one browser launch crossed: a file write, a socket bind, a Mach service registration, a sysctl, and a second file write in a different tree. Each one is a separate knob. Each knob is global or nearly so. I widened two of them and the browser still does not run under this sandbox. The other project's agent instructions now carry a line for exactly this: if the accessibility step cannot launch a browser in the current environment, report it as unverified.

## The boundary mismatch

Step back from Chrome. Four durable things fell out of this.

**Hooks see intent. Sandboxes see effects. Neither sees both.** A PreToolUse hook reads the command the model wrote and nothing about what runs inside a script. The OS sandbox sees every write and nothing about who asked. The `tempfile` gap lives exactly in between: an innocent command running a script that picks its own path.

**The sandbox cannot tell agent writes from runtime bookkeeping.** The session temp directory holds both the model's scratch files and Claude Code's own working-directory tracker. There is one permission for both. Deny it and you break exit reporting for every command, silently.

**Blocking runtime temp storage corrupts what the tool tells you.** That failure is worse than a crash. A crash you notice. A session where `true` returns 1 you might not.

**Compatibility exceptions widen the boundary again.** Every tool that does not work under the sandbox comes with a recommended fix, and the fix is a global switch: all Unix sockets, all Mach services, this command unsandboxed. The exceptions are how the boundary gets undone, one reasonable accommodation at a time.

## What the sandbox is actually around

I started with a filesystem question: can I keep an agent's writes inside its project? The experiment answered a different question.

A process does not need to write outside the project if it can ask another process to act for it. A Unix socket is a transfer of authority. Access to Docker is host access. Access to an SSH agent can authorize remote actions. Access to a browser can expose an authenticated session. Access to a local development server can mutate data the filesystem sandbox never sees. My `allowAllUnixSockets: true` says all of that is reachable, and the mitigation I have is operational: try not to run sensitive daemons next to the session. That is not a control. It is a habit.

The conclusion is not "keep sensitive daemons away from Claude." That is not how a development machine works. The conclusion is that today's agent sandboxes make you choose between broad compatibility and narrow authority, because their controls do not match how development tools compose. What I actually want is capability-scoped access: create sockets only under this directory, connect only to these named services, use this one browser profile, invoke this fixed tool without being able to rewrite what the tool executes. None of those knobs exist yet in the tool I use, and the issues asking for the first one are closed.

I never found a configuration that meant both "Claude can use the development environment normally" and "Claude cannot cause effects outside this directory." The closer I moved toward strict confinement, the more runtime and development machinery stopped working. The more functionality I restored, the more authority came back through another channel.

The project directory is still worth fencing. It stops the common mistakes and it stops throwaway work. But it is not the agent's boundary. The boundary is every capability the environment makes reachable, and nothing I have lets me draw it narrowly enough.

## Reproduce it yourself

> Same warning as the top. These commands and errors are from Claude Code 2.1.259 on macOS 26.6.2. Replace `/Users/home` and the `claude-501` session id with your own. Confirm the current docs for every sandbox key before relying on it.

Prove exit codes are intact after any sandbox change:

```bash
true; echo "exit=$?"
```

Direct write outside the project, expect a sandbox denial:

```bash
echo probe > ~/stay-in-project-probe.txt
```

Symlink escape, expect a hook denial through the Write tool and a sandbox denial through Bash:

```bash
ln -sfn /Users/home ./.probe-link
echo probe > ./.probe-link/escape-probe.txt
rm -f ./.probe-link
```

Background Bash: ask the agent to run anything with `run_in_background`. Expect the hook to deny it.

Script bypass, testing the sandbox layer alone. Write this with the Write tool. With the final hook it is denied at write time because of the literal paths; disable the hook temporarily to test the sandbox on its own:

```python
import os
targets = [
    "/private/tmp/claude-501/bypass-probe.txt",
    "/private/tmp/bypass-probe.txt",
    "/private/var/folders/bypass-probe.txt",
    os.path.expanduser("~/bypass-probe.txt"),
]
for target in targets:
    try:
        with open(target, "w") as fh:
            fh.write("probe\n")
        print(f"WROTE   {target}")
        os.remove(target)
    except OSError as exc:
        print(f"DENIED  {target}: {exc.strerror}")
```

Implicit temp, the accepted gap. Passes the hook, writes to session temp:

```python
import os, tempfile
fh = tempfile.NamedTemporaryFile(delete=False)
fh.write(b"probe\n")
fh.close()
print(f"WROTE {fh.name}")
os.remove(fh.name)
```

Check that a command passes the hook without running it:

```bash
printf '%s' '{"tool_name":"Bash","tool_input":{"command":"MAC_CHROMIUM_TMPDIR=\"$PWD/.ct\" npm run a11y"}}' \
  | CLAUDE_PROJECT_DIR=$PWD python3 ~/.claude/hooks/stay-in-project.py; echo "exit=$?"
```

Chrome under the sandbox, with and without the override. Use whatever Chrome for Testing binary Puppeteer installed for you:

```bash
mkdir -p .ct-probe/ct .ct-probe/ud && chmod 700 .ct-probe/ct
"$CHROME" --headless=new --no-first-run --disable-gpu \
  --user-data-dir="$PWD/.ct-probe/ud" --dump-dom about:blank
MAC_CHROMIUM_TMPDIR="$PWD/.ct-probe/ct" "$CHROME" --headless=new --no-first-run --disable-gpu \
  --user-data-dir="$PWD/.ct-probe/ud" --dump-dom about:blank
find .ct-probe/ct -name SingletonSocket
rm -rf .ct-probe
```

The first run should fail with `Failed to create socket directory`. The second should place `SingletonSocket` inside `.ct-probe/ct` and then fail at a different check. Which check depends on your Chrome build. That is the point.

---

*The hook and its regression suite are mine. The assistant tested, reported, and, once, went around them. I am researching agent boundaries at [Parapet](https://github.com/Parapet-Tech/parapet), an open-source LLM security proxy. More experiments here as they happen.*
