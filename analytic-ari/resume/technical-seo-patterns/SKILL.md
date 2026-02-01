---
name: technical-seo-patterns
description: >
  Technical SEO reference for web practitioners. On-page optimization, structured
  data, crawl management, Core Web Vitals, indexing strategy, and canonical URL
  patterns. Complete gap in the Agent Skills ecosystem — first skill covering
  this domain.
metadata:
  author: analytic-ari
  version: "1.0"
  created: "2026-02-01"
---

# Technical SEO Patterns

## On-Page Fundamentals

### Title Tags

The single most impactful on-page element.

- **Length**: 50-60 characters. Google truncates at ~60 characters in search results.
- **Structure**: Primary keyword near the front. Brand at the end, separated by a dash or pipe.
- **Uniqueness**: every page gets a unique title. Duplicate titles signal duplicate content.
- **Format**: `Page Topic - Brand Name` or `Page Topic | Brand Name`

**Bad**: "Home" / "Blog" / "Page 1"
**Good**: "Why I Make Claude Argue With Itself Before Writing Code - The Skills Team"

### Meta Descriptions

Not a ranking factor, but controls the search result snippet. A good description increases click-through rate.

- **Length**: 150-160 characters. Longer gets truncated.
- **Content**: summarize the page's value proposition. What will the reader get?
- **Call to action**: not a sales pitch, but a reason to click. "Learn how we..." / "See the results of..."
- **Uniqueness**: every page gets a unique description. Missing descriptions let Google auto-generate (often poorly).

### Heading Structure

- **One H1 per page**: the page's primary topic. Must match the title tag's intent.
- **H2-H6 hierarchy**: logical nesting. H2 sections contain H3 subsections. Never skip levels (H1 -> H3).
- **Keywords in headings**: natural inclusion, not stuffing. The heading should make sense to a human first.
- **Heading as outline**: if you extracted only the headings, they should form a coherent table of contents.

### URL Structure

- **Readable**: `/blog/plan-before-code` not `/blog/post?id=47`
- **Lowercase**: URLs are case-sensitive on most servers. Standardize to lowercase.
- **Hyphens not underscores**: Google treats hyphens as word separators, underscores as joiners.
- **Flat where possible**: `/blog/article-name` not `/blog/2026/01/31/category/article-name`
- **Permanent**: changing a URL without a redirect kills its accumulated search equity. Plan URLs before publishing.

## Canonical URLs

### Why Canonicals Matter

When the same content is accessible at multiple URLs, search engines must guess which is authoritative. Canonical tags remove the guessing.

### When to Use

- **Always**: every page should have a self-referencing canonical tag, even if no duplicates exist. It's defensive.
- **Cross-posting**: when content exists on your site AND dev.to/Medium/etc, the canonical points to your site.
- **URL variations**: `http` vs `https`, `www` vs non-www, trailing slash vs no trailing slash — canonical resolves all of these.
- **Pagination**: page 2, page 3 of a list should canonical to themselves (not page 1) unless they're truly duplicate content.

### Implementation

```html
<link rel="canonical" href="https://example.com/blog/article-name">
```

**Rules:**
- Canonical URL must be absolute (full URL with protocol and domain), not relative.
- Canonical must point to a 200-status page. Canonical to a 404 is a signal conflict.
- Canonical must match the page's actual URL (self-referencing) unless deliberately pointing elsewhere.
- One canonical per page. Multiple canonical tags are ignored by crawlers.

## Structured Data

### What It Does

Structured data (JSON-LD) tells search engines what your content IS, not just what it says. An article, a person, an organization, a FAQ, a breadcrumb trail.

### JSON-LD Over Microdata

Always use JSON-LD (script tag in `<head>`), not microdata (HTML attributes). Reasons:
- Decoupled from markup — changing your HTML doesn't break structured data
- Easier to validate and debug
- Google explicitly recommends JSON-LD

### Essential Schemas

**Article** (for blog posts):
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "datePublished": "2026-02-01",
  "dateModified": "2026-02-01",
  "author": {
    "@type": "Organization",
    "name": "The Skills Team"
  },
  "publisher": {
    "@type": "Organization",
    "name": "The Skills Team"
  },
  "description": "Article description for search results"
}
```

**BreadcrumbList** (for navigation context):
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com/" },
    { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://example.com/blog/" },
    { "@type": "ListItem", "position": 3, "name": "Article Title" }
  ]
}
```

**WebSite** (for sitewide identity):
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "The Skills Team",
  "url": "https://example.com/"
}
```

### Validation

Always validate structured data with Google's Rich Results Test or Schema.org validator before publishing. Invalid JSON-LD is silently ignored — no errors, just no benefit.

## Crawl Management

### robots.txt

Controls what crawlers are allowed to access. Lives at the site root (`/robots.txt`).

```
User-agent: *
Allow: /
Sitemap: https://example.com/sitemap.xml
```

**Rules:**
- `robots.txt` is a suggestion, not enforcement. Well-behaved crawlers respect it. Malicious ones don't.
- Don't block CSS or JS files — Google needs them to render the page for indexing.
- Don't use `robots.txt` to hide pages from Google. Use `noindex` meta tag instead. `robots.txt` blocks crawling but the page can still appear in search results (with no snippet) if other sites link to it.

### Sitemap

An XML file listing all pages you want indexed. Helps crawlers discover content, especially on smaller sites without many inbound links.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2026-02-01</lastmod>
  </url>
  <url>
    <loc>https://example.com/blog/</loc>
    <lastmod>2026-02-01</lastmod>
  </url>
</urlset>
```

**Rules:**
- Only include pages that return 200 and are canonical. No 404s, no redirects, no noindex pages.
- Keep `lastmod` accurate. If it's always today's date, crawlers learn to ignore it.
- Reference the sitemap in `robots.txt`.
- Maximum 50,000 URLs per sitemap. Use sitemap index files for larger sites.

### Internal Linking

Internal links are how crawlers discover pages and how search equity flows through a site.

- **Every page reachable within 3 clicks from the homepage**: deeper pages get crawled less frequently.
- **Descriptive anchor text**: "read the full article" is wasted anchor text. "Our plan-before-code workflow" tells crawlers what the target page is about.
- **Link from high-authority pages**: the homepage and popular articles pass the most equity. Use them to boost important content.
- **Fix broken internal links immediately**: 404s waste crawl budget and break equity flow.

## Core Web Vitals

Google's page experience signals. Not the only ranking factor, but a tiebreaker between otherwise equal pages.

### Largest Contentful Paint (LCP)

How long until the largest visible element renders. Target: **under 2.5 seconds**.

**Common causes of slow LCP:**
- Unoptimized hero images (no responsive sizing, no modern format)
- Render-blocking CSS or JS in `<head>`
- Web fonts that delay text rendering
- Slow server response (TTFB > 600ms)

**Fixes:**
- Preload the LCP image: `<link rel="preload" as="image" href="hero.webp">`
- Inline critical CSS, defer the rest
- `font-display: swap` on web fonts
- Server-side caching for static content

### Interaction to Next Paint (INP)

How long until the page responds to user interaction. Target: **under 200ms**. Replaced FID in 2024.

**Common causes of slow INP:**
- Heavy JavaScript blocking the main thread
- Event handlers that trigger layout recalculation
- Third-party scripts (analytics, chat widgets, ad scripts)

**Fixes:**
- Defer non-critical JavaScript: `<script defer>`
- Break long tasks into smaller chunks (yield to the main thread)
- Load third-party scripts after the page is interactive

### Cumulative Layout Shift (CLS)

How much the page layout shifts during loading. Target: **under 0.1**.

**Common causes of high CLS:**
- Images without explicit dimensions
- Ads or embeds that load and push content down
- Web fonts causing text reflow
- Dynamically injected content above the fold

**Fixes:**
- Width and height attributes on all images and videos
- `aspect-ratio` CSS for responsive embeds
- `font-display: swap` with matched fallback font metrics
- Reserve space for late-loading elements with `min-height`

## Open Graph and Social Meta

Not SEO directly, but affects how links appear when shared — which affects click-through, which affects traffic.

### Essential Tags

```html
<meta property="og:title" content="Article Title">
<meta property="og:description" content="Compelling description for social shares">
<meta property="og:url" content="https://example.com/blog/article">
<meta property="og:type" content="article">
<meta property="og:image" content="https://example.com/images/social-preview.png">
<meta property="og:site_name" content="The Skills Team">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Article Title">
<meta name="twitter:description" content="Compelling description">
<meta name="twitter:image" content="https://example.com/images/social-preview.png">
```

### og:image Rules

- **Minimum size**: 1200x630px for `summary_large_image` (Twitter/X), same works for Facebook/LinkedIn.
- **File size**: under 1MB. Large images slow down social previews.
- **Text on image**: keep text large and centered — platforms crop differently.
- **Fallback**: if no og:image, the link preview shows no image. This dramatically reduces engagement.

## Indexing Diagnostics

### Is the Page Indexed?

Search `site:example.com/page-url` in Google. If it appears, it's indexed. If not:

1. **Check robots.txt** — is the page blocked?
2. **Check canonical** — does it point somewhere else?
3. **Check noindex** — is there a `<meta name="robots" content="noindex">`?
4. **Check Google Search Console** — the URL Inspection tool shows exactly what Google sees.
5. **Check page age** — new pages take days to weeks for initial indexing. Patience.

### Forcing Index

Submit the URL through Google Search Console's URL Inspection tool. This requests (not guarantees) a crawl. For new sites, submitting the sitemap through Search Console is the fastest path to initial indexing.

## The SEO Audit Checklist

For every page:

1. **Title tag**: unique, under 60 characters, keyword near front
2. **Meta description**: unique, under 160 characters, compelling
3. **H1**: one per page, matches title intent
4. **Canonical**: present, self-referencing or correctly pointing to canonical source
5. **URL**: readable, lowercase, hyphens, permanent
6. **Structured data**: valid JSON-LD, no errors in validator
7. **Images**: dimensions set, alt text present, lazy loading on below-fold images
8. **Internal links**: page reachable in 3 clicks, descriptive anchor text
9. **Performance**: LCP < 2.5s, INP < 200ms, CLS < 0.1
10. **Social meta**: og:title, og:description, og:image present
