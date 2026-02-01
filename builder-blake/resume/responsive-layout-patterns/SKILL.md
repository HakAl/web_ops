---
name: responsive-layout-patterns
description: >
  CSS architecture and responsive layout patterns for building pages that work
  everywhere. Custom properties, fluid typography, modern layout systems, breakpoint
  strategy, and progressive enhancement. Complements Engineering's
  accessible-component-patterns (Gary) — Blake owns layout, Gary owns components.
metadata:
  author: builder-blake
  version: "1.0"
  created: "2026-02-01"
---

# Responsive Layout Patterns

## CSS Custom Property Architecture

Custom properties (CSS variables) are the foundation of a maintainable design system. Define them once, reference everywhere, override contextually.

### The Token Layer

Define design tokens at the root. These are the source of truth for the entire site.

```css
:root {
  /* Spacing scale — consistent rhythm */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 2rem;
  --space-xl: 4rem;

  /* Typography scale */
  --font-sm: clamp(0.8rem, 0.17vw + 0.76rem, 0.89rem);
  --font-base: clamp(1rem, 0.34vw + 0.91rem, 1.19rem);
  --font-lg: clamp(1.25rem, 0.61vw + 1.1rem, 1.58rem);
  --font-xl: clamp(1.56rem, 1.03vw + 1.31rem, 2.11rem);
  --font-2xl: clamp(1.95rem, 1.68vw + 1.53rem, 2.81rem);

  /* Colors — semantic, not literal */
  --color-text: #1a1a1a;
  --color-text-muted: #666;
  --color-bg: #fff;
  --color-bg-subtle: #f5f5f5;
  --color-accent: #2563eb;
  --color-border: #e5e5e5;

  /* Layout */
  --content-width: 65ch;
  --page-width: 1200px;
  --page-gutter: clamp(1rem, 5vw, 3rem);
}
```

### Rules for Custom Properties

- **Semantic names**: `--color-text` not `--dark-gray`. The value can change; the purpose doesn't.
- **Token layer is global**: defined on `:root`, read everywhere.
- **Component overrides are local**: `--button-bg` defined on `.button`, not on `:root`.
- **Never hardcode values that have tokens**: if `--space-md` exists, don't write `margin: 1rem`.
- **Dark mode is a token swap**, not a rewrite. Override `--color-text` and `--color-bg` in a media query or class, and the entire site adapts.

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-text: #e5e5e5;
    --color-bg: #1a1a1a;
    --color-bg-subtle: #2a2a2a;
    --color-border: #333;
  }
}
```

## Fluid Typography

Fixed font sizes break at viewport extremes. Fluid typography scales smoothly between a minimum and maximum using `clamp()`.

### The Formula

```
clamp(minimum, preferred, maximum)
```

- **Minimum**: the smallest the text should ever be (mobile floor)
- **Preferred**: a viewport-relative calculation that scales smoothly
- **Maximum**: the largest the text should ever be (desktop ceiling)

### Practical Scale

Use a modular scale with a ratio (1.2 for subtle, 1.25 for moderate, 1.333 for dramatic). Generate with `clamp()` so the scale itself is fluid:

| Token | Mobile min | Desktop max | Use |
|-------|-----------|-------------|-----|
| `--font-sm` | 0.8rem | 0.89rem | Captions, metadata |
| `--font-base` | 1rem | 1.19rem | Body text |
| `--font-lg` | 1.25rem | 1.58rem | H3, subheadings |
| `--font-xl` | 1.56rem | 2.11rem | H2 |
| `--font-2xl` | 1.95rem | 2.81rem | H1, hero text |

### Rules

- **Body text minimum**: never below 1rem (16px). Below this, readability drops on mobile.
- **Line length**: `max-width: 65ch` on body text containers. Beyond 75 characters per line, readers lose their place.
- **Line height scales inversely with size**: body text needs 1.5-1.6. Headings need 1.1-1.2. Large headings at 1.5 line height waste vertical space.

## Layout Systems

### The Content Grid

A single responsive grid that handles 90% of page layouts:

```css
.page {
  display: grid;
  grid-template-columns:
    [full-start] minmax(var(--page-gutter), 1fr)
    [content-start] min(var(--content-width), 100%)
    [content-end] minmax(var(--page-gutter), 1fr)
    [full-end];
}

.page > * {
  grid-column: content;
}

.page > .full-width {
  grid-column: full;
}
```

This gives you a centered content column with gutters that grow on large screens, and a `.full-width` escape hatch for elements (images, code blocks, tables) that need more room.

### Flexbox vs Grid Decision

| Use case | Choose | Why |
|----------|--------|-----|
| One-dimensional flow (nav items, tags, buttons) | Flexbox | Content drives the layout |
| Two-dimensional layout (page structure, card grids) | Grid | Layout drives the content |
| Unknown number of items, equal sizing | Grid with `auto-fill`/`auto-fit` | Intrinsic responsiveness |
| Items that need to wrap dynamically | Flexbox with `flex-wrap` | Content-aware wrapping |

### Intrinsic Responsiveness

Let the content and container determine the layout, not arbitrary breakpoints:

```css
/* Cards that reflow without media queries */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(300px, 100%), 1fr));
  gap: var(--space-lg);
}
```

`auto-fill` + `minmax()` creates a grid that goes from 1 column on small screens to 2, 3, or 4 columns as space allows — with zero media queries.

### Container Queries

Respond to the container's size, not the viewport's. Use for components that live in different contexts (sidebar vs main content vs full-width):

```css
.card-container {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
  }
}
```

**When to use container queries vs media queries:**
- **Container queries**: component adapts to its container. Use when the same component appears in different layout contexts.
- **Media queries**: page layout adapts to the viewport. Use for structural layout shifts.

## Breakpoint Strategy

### The Wrong Way

Designing for specific device widths (320px, 768px, 1024px) targets devices that exist today but not tomorrow.

### The Right Way

Set breakpoints where the content breaks, not where devices happen to be.

**Process:**
1. Start at the narrowest viewport
2. Widen slowly until the layout looks wrong
3. That's where the breakpoint goes
4. Repeat until the widest viewport

### Practical Breakpoints

Most sites need 2-3 breakpoints, not 6:

```css
/* Small: single column, full-width elements */
/* No media query needed — this is the default */

/* Medium: enough room for side-by-side layouts */
@media (min-width: 40em) { /* ~640px */ }

/* Large: full desktop layout */
@media (min-width: 64em) { /* ~1024px */ }
```

**Use `em` for breakpoints, not `px`.** `em`-based breakpoints respect the user's font size preference. A user who sets their browser to 20px base font triggers the breakpoint at a wider pixel width, giving them more room — which is exactly what they need.

### Mobile-First

Always write mobile styles as the default, then add complexity with `min-width` queries. Reasons:

- Mobile is the constrained case. Start with constraints, add flexibility.
- `min-width` queries add features. `max-width` queries remove them. Adding is simpler than subtracting.
- If the CSS fails to load media queries (old browser, broken parse), the user gets the mobile layout — which works. The reverse gives them a broken desktop layout on a small screen.

## Progressive Enhancement

### The Principle

Build the core experience with the most resilient technology (HTML), enhance with style (CSS), enhance further with behavior (JavaScript). Each layer is optional for the one below it.

### In Practice

- **HTML works without CSS**: content is readable, forms submit, links navigate. Semantic markup is the baseline.
- **CSS works without JavaScript**: layouts render, animations play (via CSS transitions/animations), responsive behavior works. No layout that requires JS to function.
- **JavaScript enhances**: infinite scroll, dynamic filtering, real-time updates, smooth transitions. If JS fails, the user gets a functional (if less polished) experience.

### Feature Detection

Use `@supports` for CSS features, not browser sniffing:

```css
/* Fallback: regular grid */
.layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

/* Enhancement: subgrid when available */
@supports (grid-template-columns: subgrid) {
  .layout > .item {
    display: grid;
    grid-template-columns: subgrid;
  }
}
```

## Performance Patterns

### Critical CSS

The styles needed for above-the-fold content should be inlined in `<head>`. Everything else loads asynchronously. For a blog, this means: layout grid, typography, header, hero — not the footer, not the code block syntax highlighting.

### Image Optimization

- **`loading="lazy"`** on every image below the fold. Free performance.
- **`width` and `height` attributes** on every `<img>`. Prevents layout shift (CLS).
- **`srcset` and `sizes`** for responsive images. Don't serve a 2000px image to a 320px viewport.
- **Modern formats**: WebP or AVIF with `<picture>` fallback to JPEG.

### Reduce Layout Shift

Layout shift (CLS) is the most visible performance problem — content jumping as the page loads.

- **Set dimensions on media**: images, videos, embeds all need explicit width/height or aspect-ratio.
- **Reserve space for dynamic content**: ads, lazy-loaded components, fonts. Use `min-height` or `aspect-ratio` to hold the space.
- **Font loading**: `font-display: swap` prevents invisible text. Accept the flash of unstyled text — it's better than a blank page.

## The Build Checklist

Before considering a page done:

1. **Resize test**: drag the viewport from 320px to 2560px. Nothing breaks, nothing overflows, nothing disappears.
2. **Content test**: does the layout work with real content? Short titles AND long titles? One paragraph AND ten?
3. **Zoom test**: 200% zoom, no horizontal scroll, no overlapping text.
4. **Token test**: are all spacing, color, and font values using custom properties? No hardcoded values.
5. **Progressive test**: disable JavaScript. Does the page still work?
6. **Performance test**: no images without dimensions, no render-blocking resources, no layout shift.
