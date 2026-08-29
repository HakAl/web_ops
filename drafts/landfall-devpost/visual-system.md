# Landfall submission visual system

Status: editable draft. Do not publish.

## Creative direction

The visual idea is a controlled shoreline: work crosses one authorization boundary, then moves through explicit channels while authority remains visible. The system should look governed, not militarized and not magical.

## Palette

| Token | Hex | Use |
| --- | --- | --- |
| Ink | `#152536` | Body text, arrows, primary outlines |
| Cloud teal | `#087E8B` | Real-cloud vertical slice, solid highlight |
| Cloud tint | `#D9F1F2` | Real-cloud node fills |
| Local amber | `#B56A00` | Local governance demonstration outlines |
| Local tint | `#FFF4DB` | Local explanatory panels |
| Evidence green | `#18794E` | Passed evidence labels only |
| Unknown violet | `#6F5AA8` | Unknown or blocked evidence labels |
| Refusal red | `#B42318` | Refused transitions and stale predecessor beat |
| Paper | `#FCFBF7` | Canvas |
| Muted | `#526476` | Secondary copy |

All body text on Paper or either tint uses Ink. Never rely on color alone: every cloud element is labeled `REAL CLOUD`, every local element is labeled `LOCAL GOVERNANCE`, and every unknown carries the word `UNKNOWN`.

## Type and hierarchy

- Display: `Inter Tight`, `Arial Narrow`, or system sans, weight 700.
- Body: `Inter`, `Arial`, or system sans, weight 400 to 600.
- Evidence and identifiers: `IBM Plex Mono`, `Consolas`, or monospace.
- Use sentence case. Avoid all-caps except short status chips.
- Minimum video text size: 42 px on a 1920 by 1080 canvas.
- Minimum diagram text size: 15 px in the source SVG viewBox.

## Shape grammar

- Solid Cloud teal border and Cloud tint fill: demonstrated in the real-cloud vertical slice.
- Dashed Local amber border and Paper fill: implemented and demonstrated locally.
- Double Ink border: authoritative state.
- Rounded rectangle: runtime role or interface.
- Cylinder: persisted state.
- Hexagon: deterministic enforcement or verification.
- Thin arrow: event or evidence flow.
- Red barred arrow: refused transition.

## Repeated labels

Use these exact chips across the diagram, video, and gallery stills:

- `REAL CLOUD PROBE`
- `DETERMINISTIC LOCAL GOVERNANCE DEMONSTRATION`
- `AUTHORITATIVE STATE`
- `READ-ONLY, NON-AUTHORITATIVE`
- `LEASE EXPIRY PROVES EXPIRY, NOT DEATH`
- `UNKNOWN AUTHORIZES NO TERMINAL WRITE`
- `WORKER CANNOT WRITE TERMINAL STATE`

## Motion and editing

- Use direct cuts for evidence changes.
- Keep the unedited live-execution segment visibly continuous with a small `LIVE, UNEDITED` chip and running clock.
- Do not animate a local node into a cloud node. The two evidence beats remain separate on screen.
- Hold any proof frame long enough to read its status and source label.
- Mask at capture time when possible, then perform a second masking pass before export.
