# Content Guidelines — Carousel Typography, Layout & Anti-Hallucination

## 1. Mobile Typography Hierarchy (4:5 Aspect Ratio — 1080x1350 px Canvas)

When generating or editing HTML carousel templates, strictly adhere to these typographic bounds:

| Element | Ideal Size | Font Weight | Line Height | Purpose & Guidelines |
|---|---|---|---|---|
| **Cover Headline (Slide 1)** | `76px – 88px` | `800 / 900` | `1.05 – 1.10` | High-stopping power; max 8 words; must be readable on a 6-inch phone screen in 1.5s. |
| **Inside Headline (Slides 2–7)** | `52px – 58px` | `700 / 800` | `1.15` | Clear section claim; keep to 1–2 lines. |
| **Body Text / Paragraph** | `28px – 32px` | `400 / 500` | `1.5 – 1.6` | High legibility; maximum 30–45 words per slide. Never drop below `26px`. |
| **Step / Metric Counter** | `64px – 100px` | `800 / Mono` | `1.0` | Sequential anchors (e.g. `01.`, `02.`, `03.`). |
| **Tag / Category Pill** | `18px – 22px` | `600 / Bold` | `1.0` | Uppercase, tracked out (`letter-spacing: 0.15em`). |

---

## 2. Safe Zones & UI Margins

- **Outer Margin:** Minimum `84px` (recommended `96px`) margin on all 4 sides.
- **Top Safe Zone:** Keep `100px` clear from the top edge to prevent interference with Instagram carousel progress dots and author header.
- **Bottom Safe Zone:** Keep `110px` clear from the bottom edge to avoid overlapping with Instagram bookmark, like, and share icons.
- **Swipe Cue:** Place subtle indicator (e.g., `SWIPE ->` or pagination `[01/07]`) strictly in the top-right or bottom-right safe corner.

---

## 3. Anti-Hallucination & Grounding Protocol

1. **Strict SKU Grounding:** Never invent product features, battery life numbers, dimensions, or technical specifications. Every claim must directly trace to `brands/<brand-slug>/products/<sku-slug>/info.md`.
2. **Missing Info Protocol:** If a requested specification is not found in `info.md`, flag it immediately during drafting rather than guessing.
3. **Product Asset Requirement:** Slide 6 (Product Showcase) must always reference a verified local file at `brands/<brand>/products/<sku>/mockup.png`. If missing, notify the user.

---

## 4. Slide-by-Slide Narrative Arc (7-Slide Framework)

- **Slide 1 (Hook):** Relatable pain point, contrarian truth, or high-urgency question.
- **Slide 2 (Agitation / The Problem):** Why typical advice fails; the hidden cost of ignoring the issue.
- **Slide 3 (Insight / Core Principle):** The paradigm shift or fundamental framework.
- **Slide 4 (Actionable Step 1):** Practical, immediate execution tip.
- **Slide 5 (Actionable Step 2):** Pro-level optimization or common pitfall to avoid.
- **Slide 6 (Product Integration / Showcase):** How the specific SKU solves this friction effortlessly. Includes transparent product cutout + key specs badge.
- **Slide 7 (Actionable CTA):** Save prompt, comment trigger word for auto-DM, and marketplace bio link callout.
