---
name: accessibility-testing-methodology
description: >
  Systematic accessibility testing procedures. WCAG success criteria verification,
  screen reader testing flows, keyboard navigation audit, automated tooling,
  and common failure modes. Complements Engineering's accessible-component-patterns
  (Gary) — Gary builds accessible components, Grace verifies they are accessible.
metadata:
  author: guardian-grace
  version: "1.0"
  created: "2026-02-01"
---

# Accessibility Testing Methodology

## The Testing Layers

Accessibility testing is not one activity. It's four distinct layers, each catching problems the others miss.

| Layer | What it catches | Coverage |
|-------|----------------|----------|
| **Automated scanning** | Obvious violations: missing alt text, low contrast, missing labels | ~30-40% of WCAG issues |
| **Keyboard testing** | Focus traps, unreachable elements, missing focus indicators | Critical interactions |
| **Screen reader testing** | Announcement order, missing context, confusing navigation | User experience |
| **Manual review** | Content clarity, cognitive load, logical flow | Everything automation misses |

Never rely on a single layer. Automated tools catch less than half of real accessibility problems. The rest require a human.

## Layer 1: Automated Scanning

### Tools

- **axe-core** (browser extension or CLI): the most reliable automated scanner. Low false-positive rate.
- **Lighthouse** (Chrome DevTools): includes accessibility audit. Good for quick checks, less thorough than axe.
- **pa11y** (CLI): good for CI integration. Run on every build to catch regressions.
- **WAVE** (browser extension): visual overlay showing errors in context. Good for learning, less good for systematic audits.

### What Automation Catches

- Missing `alt` attributes on images
- Color contrast below WCAG thresholds (4.5:1 for text, 3:1 for UI elements)
- Missing form labels
- Missing document language (`<html lang="en">`)
- Duplicate IDs
- Empty headings or links
- Missing ARIA attributes on interactive elements

### What Automation Misses

- Alt text that exists but is meaningless ("image1.jpg", "photo", "click here")
- Logical reading order (automation sees DOM order, not visual order)
- Whether focus management makes sense to a user
- Whether ARIA usage is correct (automation checks presence, not correctness)
- Cognitive accessibility (is the content understandable?)
- Keyboard traps that only occur in specific interaction sequences

### Running an Automated Audit

1. Run axe on every page — not just the homepage
2. Group results by impact: Critical > Serious > Moderate > Minor
3. Fix Critical and Serious before anything else
4. Re-run after fixes to verify resolution (some fixes break other things)
5. Don't chase a perfect score — a page with zero axe violations can still be unusable for screen reader users

## Layer 2: Keyboard Testing

### The Core Test

Put the mouse in a drawer. Navigate the entire page using only the keyboard.

### Key Commands

| Key | Action |
|-----|--------|
| `Tab` | Move to next focusable element |
| `Shift + Tab` | Move to previous focusable element |
| `Enter` | Activate links and buttons |
| `Space` | Activate buttons, toggle checkboxes, scroll |
| `Arrow keys` | Navigate within widgets (tabs, menus, radio groups) |
| `Escape` | Close modals, dropdowns, dialogs |

### What to Test

**Focus order:**
- Does Tab move through elements in a logical order? (Usually visual left-to-right, top-to-bottom)
- Are any interactive elements skipped? (Clickable elements without tabindex)
- Are any non-interactive elements focused? (Decorative elements with errant tabindex)

**Focus visibility:**
- Can you always tell which element has focus? A visible focus indicator is mandatory.
- Does the focus indicator have sufficient contrast? (WCAG 2.2 requires 3:1 contrast for focus indicators)
- Does focus ever disappear? (Focus moves to an invisible or off-screen element)

**Focus traps:**
- Can you Tab into AND out of every component? (Modals should trap focus intentionally. Nothing else should.)
- After closing a modal/dropdown/dialog, does focus return to the element that opened it?

**Functionality:**
- Can every action performed with a mouse also be performed with a keyboard?
- Do custom components (dropdowns, sliders, tabs) support expected keyboard patterns?
- Can forms be completed and submitted entirely by keyboard?

### Common Keyboard Failures

- `<div onclick>` instead of `<button>` — not focusable, not keyboard-activatable
- Custom dropdowns that only open on mouse hover
- Modals that don't trap focus — Tab escapes into the background
- Focus indicators removed with `outline: none` and nothing replacing them
- Skip-to-content link missing — keyboard users Tab through entire navigation on every page

## Layer 3: Screen Reader Testing

### Which Screen Readers

| Screen reader | Platform | Browser | Priority |
|---------------|----------|---------|----------|
| **NVDA** | Windows | Firefox or Chrome | High — most used free screen reader |
| **VoiceOver** | macOS/iOS | Safari | High — default on Apple devices |
| **JAWS** | Windows | Chrome or Edge | Medium — most used paid screen reader |
| **TalkBack** | Android | Chrome | Medium — Android default |

Test with at least NVDA + VoiceOver to cover the two dominant platforms.

### Screen Reader Navigation Patterns

Screen reader users do not read pages linearly. They navigate by:

- **Headings** (`H` key in NVDA): jump between headings to scan page structure. This is why heading hierarchy matters.
- **Landmarks** (D key in NVDA): jump between `<header>`, `<nav>`, `<main>`, `<footer>`. This is why semantic HTML matters.
- **Links** (K key in NVDA): list all links on the page. This is why "click here" link text is useless out of context.
- **Form controls** (F key in NVDA): jump between form fields. This is why label association matters.

### What to Test

**Page load announcement:**
- Does the screen reader announce the page title?
- Is the first meaningful content reachable quickly? (Skip link, landmark navigation)

**Heading navigation:**
- Do headings form a logical outline when navigated in sequence?
- Is there a single H1 that identifies the page?
- Are there heading level skips? (H1 -> H3 with no H2)

**Link and button announcements:**
- Does every link announce where it goes? ("Read more" fails. "Read more about accessibility testing" passes.)
- Does every button announce what it does? ("Submit" is better than "Button 1")
- Do icon-only buttons have accessible names? (`aria-label` or visually hidden text)

**Image descriptions:**
- Do informative images have meaningful alt text? (Not just "image" or the filename)
- Do decorative images have empty alt text (`alt=""`)? (Prevents the screen reader from announcing "image" with no context)
- Do complex images (charts, diagrams) have extended descriptions?

**Form interaction:**
- Does each field announce its label when focused?
- Do required fields announce "required"?
- Do error messages announce when they appear? (Live region or focus management)
- Are field descriptions (help text, format hints) announced via `aria-describedby`?

**Dynamic content:**
- Are status messages announced without focus change? (`role="status"`, `aria-live="polite"`)
- Are error alerts announced immediately? (`role="alert"`, `aria-live="assertive"`)
- When content updates dynamically (search results, loaded content), is the change communicated?

### Common Screen Reader Failures

- Missing alt text — screen reader announces the image filename instead
- Missing form labels — screen reader announces "edit text" with no context
- Missing landmark regions — no way to jump to main content
- `aria-hidden="true"` on visible content — hides it from screen reader users
- Live regions that fire on page load — bombardment of announcements before the user can navigate
- CSS `content` used for meaningful text — may not be announced by all screen readers

## Layer 4: Manual Review

### Content Accessibility

- **Reading level**: is the content understandable by the target audience? Jargon explained or avoided?
- **Consistent terminology**: same concept uses the same word throughout. Don't alternate between "post," "article," and "entry."
- **Instruction clarity**: do instructions make sense without visual reference? "Click the green button" fails for colorblind and screen reader users. "Click Submit" passes.

### Visual Accessibility

- **Color alone**: is any information conveyed only by color? (Red/green for error/success needs an icon or text too)
- **Text resize**: does the page work at 200% zoom without horizontal scroll or content clipping?
- **Reduced motion**: does `prefers-reduced-motion: reduce` suppress animations? Vestibular disorders are triggered by motion.
- **High contrast**: does `prefers-contrast: more` (or Windows High Contrast Mode) produce a usable result?
- **Spacing**: does `prefers-reduced-data` or text spacing override (WCAG 1.4.12: 1.5x line height, 2x paragraph spacing) break the layout?

### Cognitive Accessibility

- **Predictability**: does the interface behave consistently? Same action = same result across pages.
- **Error recovery**: can users undo mistakes? Are destructive actions confirmed?
- **Timeout handling**: if there's a session timeout, is the user warned? Can they extend it?
- **Distraction**: are there auto-playing videos, carousels, or animations that can't be paused?

## WCAG Quick Reference

### Level A (Minimum)

Must-pass criteria. Failure means some users are completely blocked.

- 1.1.1 Non-text content has text alternatives
- 1.3.1 Information and relationships are programmatically determinable (semantic HTML)
- 2.1.1 All functionality available from keyboard
- 2.4.1 Mechanism to skip repetitive blocks (skip link)
- 3.1.1 Default language of the page is programmatically set
- 4.1.2 Name, role, value determinable for UI components

### Level AA (Standard Target)

The standard compliance target. Most organizations and legal requirements aim here.

- 1.4.3 Contrast ratio: 4.5:1 for text, 3:1 for large text
- 1.4.4 Text resizable to 200% without loss of content
- 1.4.10 Content reflows at 320px width without horizontal scroll
- 2.4.6 Headings and labels describe topic or purpose
- 2.4.7 Focus indicator is visible
- 2.5.8 Target size minimum 24x24px (WCAG 2.2)

### Level AAA (Aspirational)

Rarely required, but valuable for specific use cases.

- 1.4.6 Contrast ratio: 7:1 for text
- 2.4.9 Link purpose clear from link text alone (not surrounding context)
- 3.1.5 Reading level: lower secondary education level where possible

## The Accessibility Audit Report

### Structure

1. **Executive summary**: pass/fail/partial for each WCAG level tested. Total issues by severity.
2. **Critical findings**: issues that block users. Fix first.
3. **Major findings**: issues that significantly impair the experience.
4. **Minor findings**: issues that are noticeable but not blocking.
5. **Positive findings**: what's working well. Reinforces good patterns.

### For Each Finding

- **What**: the specific problem
- **Where**: page URL and element (screenshot or code snippet)
- **Who's affected**: which users or assistive technologies
- **WCAG criterion**: specific success criterion violated
- **Severity**: Critical / Major / Minor
- **How to fix**: specific, actionable remediation steps

### The Sign-Off

Grace does not sign off on "it passes axe." Grace signs off on "a real user with a screen reader can accomplish the primary task on this page." Those are different bars.
