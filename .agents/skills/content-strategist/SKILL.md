---
name: content-strategist
description: Formulate 4 strategic content pillars and generate a 30-day balanced content rotation matrix. Enforces HITL Gates 2 and 3.
---

# Content Strategist Skill

This skill transforms approved brand profiles into high-converting editorial frameworks and 30-day publishing schedules.

## Workflow

### 1. Formulate 4 Content Pillars
- Read `brands/<brand-slug>/profile.md`.
- Establish 4 distinct content pillars balancing broad audience appeal with high-intent product conversion:
  1. **Pillar 1: Pain-Point & Practical Life Hacks** (Relatable everyday friction solved).
  2. **Pillar 2: Authority & Buyer Guide / Comparison** (Educate before purchase; build trust).
  3. **Pillar 3: Lifestyle & Aesthetic Showcase** (Aspirational desk setups, cozy living, curated routines).
  4. **Pillar 4: Deep-Dive Product Spotlight & Social Proof** (Zero-fluff breakdown of registered SKUs).
- Write to `brands/<brand-slug>/content-pillars.md`.
- **Trigger HITL Gate 2:** Seek user approval on the 4 pillars before scheduling.

### 2. Generate 30-Day Rotation Matrix
- Once Gate 2 is approved, create a balanced 30-day calendar at `brands/<brand-slug>/calendar-30d.md`.
- Ensure alternating content formats:
  - 40% Educational / Problem-Solving
  - 30% Product Spotlight (tied to verified SKUs)
  - 20% Comparison / Buying Advice
  - 10% Engagement / Community / Relatable Memes
- Map each day to:
  - `Day [1-30]`
  - `Pillar`
  - `Target SKU` (if applicable)
  - `Core Hook / Working Title`
  - `Target Template Archetype` (Magazine, Minimalist, Blueprint)
- **Trigger HITL Gate 3:** Present the 30-day matrix to the user for sign-off.
