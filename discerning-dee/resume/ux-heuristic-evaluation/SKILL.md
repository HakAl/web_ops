---
name: ux-heuristic-evaluation
description: >
  Structured UX evaluation methodology. Nielsen's heuristics, Gestalt principles,
  cognitive load patterns, and severity rating applied to real design review.
  The codified principles Dee critiques against.
metadata:
  author: discerning-dee
  version: "1.0"
  created: "2026-02-01"
---

# UX Heuristic Evaluation

## Nielsen's 10 Heuristics (Applied)

These are not abstract principles. Each one is a lens for finding real usability problems.

### 1. Visibility of System Status

The system should keep users informed about what's happening through timely, appropriate feedback.

**What to look for:**
- Does the user know where they are? (Active nav state, breadcrumbs, page titles)
- Does the user know what's happening? (Loading indicators, progress bars, success/error states)
- Does the user know what just happened? (Confirmation after action, state change feedback)

**Common violations:**
- Form submits with no feedback — did it work? Did it fail? Is it loading?
- Navigation with no active state — which page am I on?
- Background operations with no indicator — the user clicks again, creating duplicates

### 2. Match Between System and Real World

Use language and concepts familiar to the user, not system-oriented terms.

**What to look for:**
- Does the UI use the user's vocabulary or the developer's? ("Dashboard" is developer language. "My posts" is user language.)
- Do icons match real-world metaphors? (Floppy disk for save is dead metaphor but still understood. Hamburger menu is learned convention, not metaphor.)
- Is information organized in a natural, logical order?

**Common violations:**
- Error messages that expose system internals: "Error 500: null reference exception"
- Labels that use internal terminology: "Entity" instead of "Article," "Instance" instead of "Account"
- Dates in ISO format (2026-02-01) instead of human format (February 1, 2026) for non-technical audiences

### 3. User Control and Freedom

Users often take wrong actions. Provide a clearly marked emergency exit without punishment.

**What to look for:**
- Can the user undo? (Edit, unsend, restore, back)
- Can the user cancel mid-process? (Multi-step forms, uploads, long operations)
- Are destructive actions reversible or at least confirmed?

**Common violations:**
- Delete with no confirmation and no undo
- Multi-step forms with no back button
- "Are you sure?" dialogs that train users to click Yes reflexively (too frequent = ignored)

### 4. Consistency and Standards

Follow platform conventions. Don't make users wonder whether different words, situations, or actions mean the same thing.

**What to look for:**
- Same action, same label everywhere? (Don't call it "Save" here and "Update" there)
- Same visual treatment for same element type? (All buttons look like buttons, all links look like links)
- Platform conventions respected? (Underline = link on web. Blue text = link on web. Breaking either creates confusion.)

**Common violations:**
- Links styled as buttons and buttons styled as links
- Different terms for the same concept across pages
- Custom components that override native behavior (custom selects that break keyboard nav)

### 5. Error Prevention

Better than good error messages is design that prevents errors in the first place.

**What to look for:**
- Are constraints built into the UI? (Date pickers instead of free text, character counters, disabled states for invalid actions)
- Does the UI prevent impossible states? (Can't submit without required fields, can't select end date before start date)
- Are dangerous operations gated? (Confirm before delete, type-to-confirm for irreversible actions)

**Common violations:**
- Free text fields where structured input would prevent errors
- No validation until form submit — user fills 10 fields, submits, then discovers field 2 was wrong
- Allowing the user to start an action that will inevitably fail (publish button enabled when required fields are empty)

### 6. Recognition Over Recall

Minimize memory load. Make options, actions, and information visible or easily retrievable.

**What to look for:**
- Are choices visible or do users have to remember them? (Dropdowns with options visible vs. empty text fields requiring exact input)
- Is context preserved? (When returning to a form, are previous entries still there?)
- Are recently used items surfaced? (Recent files, recent searches, last viewed)

**Common violations:**
- Search that requires exact syntax with no suggestions
- Settings pages where you have to remember what you changed
- Navigation that hides behind hover states — invisible until you already know it's there

### 7. Flexibility and Efficiency of Use

Accelerators for experts that don't burden novices. The system should cater to both.

**What to look for:**
- Are there shortcuts for frequent actions? (Keyboard shortcuts, quick actions, bulk operations)
- Can experts skip steps? (Direct URL access, skippable tutorials, collapsed advanced options)
- Do defaults serve the common case? (Pre-filled forms, smart defaults, sensible presets)

**Common violations:**
- Forced walkthroughs that can't be skipped
- No keyboard shortcuts for frequent actions
- Removing power-user features to "simplify" — punishes the users who need the product most

### 8. Aesthetic and Minimalist Design

Every extra unit of information competes with the relevant information and diminishes its visibility.

**What to look for:**
- Is there visual noise? (Decorative elements that don't communicate, excessive borders and dividers)
- Does the visual hierarchy match the importance hierarchy? (Most important thing = most visually prominent)
- Could anything be removed without loss of function? If yes, remove it.

**Common violations:**
- Equal visual weight on everything — no hierarchy, everything looks the same importance
- Decorative images that add no information
- Dashboard with 20 metrics when the user needs 3

### 9. Help Users Recognize, Diagnose, and Recover from Errors

Error messages should be in plain language, precisely indicate the problem, and constructively suggest a solution.

**What to look for:**
- Do error messages say what went wrong? (Not just "Error" or "Something went wrong")
- Do they say how to fix it? ("Email must include @" not just "Invalid email")
- Are they near the problem? (Inline validation next to the field, not a banner at the top)

**Common violations:**
- Generic error messages: "An error occurred. Please try again."
- Errors displayed far from their source (top-of-page banners for field-level problems)
- Technical error codes shown to non-technical users

### 10. Help and Documentation

Even systems that can be used without documentation should provide help. It should be searchable, focused on the user's task, list concrete steps, and not be too large.

**What to look for:**
- Is help contextual? (Tooltips, inline hints, help text near the action it describes)
- Is it findable? (Searchable, linked from relevant places, not buried in a sitemap)
- Is it task-oriented? ("How to publish a post" not "The Publishing Module API Reference")

**Common violations:**
- No help at all — "it should be intuitive" (nothing is intuitive to everyone)
- Help documentation that describes the system, not the user's task
- Outdated documentation that describes a previous version

## Gestalt Principles (Applied to Layout)

How the brain groups visual elements. Violating these creates layouts that feel "off" even when users can't articulate why.

### Proximity

Elements that are close together are perceived as related. Elements far apart are perceived as separate.

**Application:** Form labels must be closer to their field than to the neighboring field. Sections need enough whitespace between them to read as distinct groups. A card's title must be visually bound to its content, not floating between two cards.

**The test:** squint at the layout. The groupings you see at a glance should match the logical groupings.

### Similarity

Elements that look alike are perceived as functionally alike.

**Application:** All clickable elements should share visual traits (color, underline, cursor change). All section headings should look the same. If two buttons look identical but do different things, one of them is lying.

### Continuity

The eye follows smooth paths. Lines, curves, and alignment create visual flow.

**Application:** Align elements to a grid. When elements break alignment, the eye stumbles. Intentional grid-breaking can create emphasis, but unintentional misalignment creates distrust.

### Closure

The brain completes incomplete shapes. You don't need borders on all four sides of a card if three sides and a shadow are enough.

**Application:** Reduce visual noise by using implied boundaries (whitespace, alignment, background color) instead of explicit ones (borders, dividers, outlines).

### Figure-Ground

The brain separates foreground from background. Modals, dropdowns, and tooltips must have clear visual separation from the layer behind them.

**Application:** Overlays need shadow, dimmed background, or both. If a dropdown appears and blends into the page behind it, figure-ground has failed.

## Cognitive Load Patterns

### Hick's Law

Decision time increases logarithmically with the number of choices. More options = slower decisions.

**Application:** Don't present 15 navigation items. Group them. Progressive disclosure: show 5 categories, expand to show sub-items. Every visible choice is a cognitive cost.

### Fitts's Law

Time to reach a target depends on distance and size. Farther and smaller = harder to click.

**Application:** Primary actions should be large and near the user's current focus. Destructive actions should be small and far from primary actions (but not hidden). Mobile touch targets: minimum 44x44px.

### Miller's Law

Working memory holds roughly 7 (plus or minus 2) items. Exceeding this overloads the user.

**Application:** Chunk information into groups of 3-5 items. Phone numbers are chunked (555-123-4567). Navigation should chunk into sections. If a form has 20 fields, group them into 4-5 logical sections.

## Severity Rating

Every finding gets a severity so the team can prioritize.

| Severity | Definition | Action |
|----------|-----------|--------|
| **Critical** | Users cannot complete their primary task. | Fix before ship. Blocker. |
| **Major** | Users can complete the task but with significant difficulty or confusion. | Fix in current cycle. |
| **Minor** | Users notice the issue but it doesn't impede their task. | Fix when touching the area. |
| **Cosmetic** | Does not affect usability. Visual inconsistency or polish issue. | Backlog. |

### Severity Calibration

- A finding that affects every user on every visit is more severe than one affecting a rare flow.
- A finding on the primary task (what the user came to do) is more severe than one on a secondary task.
- A finding that causes data loss or irreversible action is always Critical regardless of frequency.

## The Evaluation Process

### Before Starting

1. Define the scope — which pages, which flows, which user tasks
2. Identify the primary user task — what is the user trying to accomplish?
3. Walk the flow as the user — don't jump to individual pages. Start where the user starts.

### During Evaluation

For each screen or state:
1. Walk through all 10 heuristics systematically. Don't freelance.
2. Note the finding, the heuristic it violates, and the severity.
3. Include a specific recommendation — "this is broken" without "here's how to fix it" is unhelpful.

### After Evaluation

1. Group findings by severity, not by heuristic.
2. Present Critical and Major findings first. Don't bury them in a list of 30 Cosmetic issues.
3. Include positive findings — what's working well. Critique without acknowledgment destroys morale.
