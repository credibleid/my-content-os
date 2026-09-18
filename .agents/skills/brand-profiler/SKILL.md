---
name: brand-profiler
description: Intake and configure brand profile, visual design tokens, audience personas, and product SKU specifications. Enforces HITL Gate 1.
---

# Brand Profiler Skill

This skill handles onboarding new brands and configuring product SKU knowledge bases to eliminate creative hallucinations.

## Workflow

### 1. Ingest Brand & Store Information
- Extract store details, niche, and product lineup from user input or marketplace links (e.g. Tokopedia, Shopee).
- Formulate or update `brands/<brand-slug>/profile.md` containing:
  - Brand identity, mission, and unique value proposition (UVP).
  - Target audience demographics and psychographics.
  - Tone of voice guidelines (vocabulary, formality, banned words).
  - Visual design tokens (Primary hex, secondary hex, background accents, font pairings).
  - Store links and marketplace identifiers.

### 2. Configure Product Knowledge Bases
- For each product SKU, create a dedicated folder: `brands/<brand-slug>/products/<sku-slug>/`.
- Author `info.md` detailing:
  - Product title and exact SKU code.
  - Real technical specifications (dimensions, battery, waterproof rating, materials).
  - Primary pain points solved.
  - Features vs benefits breakdown.
  - Verified Tokopedia/marketplace product link and price point.
- **Asset Requirement:** Ensure a transparent product cutout is placed at `brands/<brand-slug>/products/<sku-slug>/mockup.png`.

### 3. Verification & Gate 1 Trigger
- Present a concise summary of `profile.md` and registered SKUs to the user.
- **Trigger HITL Gate 1:** Explicitly ask user approval before progressing to content strategy.
