---
name: daily-drafter
description: Read today's scheduled topic and verified SKU specifications to draft 3 distinct creative angles. Enforces HITL Gate 4.
---

# Daily Drafter Skill

This skill acts as the creative copywriter and structural architect for individual daily posts.

## Workflow

### 1. Topic & SKU Context Ingestion
- Retrieve the designated topic and SKU for the target date from `brands/<brand-slug>/calendar-30d.md`.
- Read verified facts from `brands/<brand-slug>/products/<sku-slug>/info.md`.
- Review mobile typography and safe zone limits in `.agents/rules/content-guidelines.md`.

### 2. Generate 3 Distinct Copywriting Angles
Craft 3 distinct draft concepts with complete 7-slide outlines:
- **Option A (Relatable Problem / Emotional Agitation):**
  - Angle: Address a common, frustrating daily nuisance (e.g., "Capek dibikin repot kabel bel rumah putus kena hujan?").
  - Arc: Story -> Agitation -> Practical Solution -> SKU Integration.
- **Option B (Framework / Actionable Checklist):**
  - Angle: Structured step-by-step audit or setup checklist.
  - Arc: "3 Kriteria Wajib Sebelum Beli Bel Rumah" -> Rule 1 -> Rule 2 -> Solution Showcase.
- **Option C (Contrarian Truth / Myth vs Fact):**
  - Angle: Debunking outdated habits or cheap alternatives.
  - Arc: "Kenapa bel rumah kabel jadul bikin boros renovasi?" -> Comparison -> The Modern Standard.

### 3. Draft Presentation & Gate 4 Trigger
- For each option, present:
  - Slide 1 Hook Headline & Visual Vibe
  - Slides 2–5 Core Takeaway Bullets
  - Slide 6 Product Showcase Integration
  - Slide 7 Call-to-Action (CTA) & Recommended Caption
- **Trigger HITL Gate 4:** Present the 3 options to the user and await selection of the winning draft (and destination format: Carousel or Video).
