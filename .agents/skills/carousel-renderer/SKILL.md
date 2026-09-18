---
name: carousel-renderer
description: Render approved 7-slide drafts into ultra-crisp 2x Retina PNGs (2160x2700 px) using Playwright headless browser snapshotting.
---

# Carousel Renderer Skill

This skill automates the production rendering of validated 7-slide carousels into high-resolution social assets ready for upload.

## Workflow

### 1. Template Selection & Population
- Based on the brand's aesthetic or post archetype, select the HTML template:
  - `templates/carousels/magazine.html` (Dark / High-Impact Luxury)
  - `templates/carousels/minimalist.html` (Light / Editorial Authority)
  - `templates/carousels/blueprint.html` (Tech / Cyber Framework)
- Inject the approved copy into the 7 `.slide-canvas` elements.
- Slot the transparent product image from `brands/<brand-slug>/products/<sku-slug>/mockup.png` into Slide 6.

### 2. Execution via Playwright Engine
Run the headless snapshot script with scale factor 2:
```bash
./.venv/bin/python engine/render.py \
  --template templates/carousels/<template>.html \
  --output output/<brand-slug>_<YYYY-MM-DD>/ \
  --scale 2
```

### 3. Output Validation
- Confirm all 7 PNG files are generated:
  - `slide_01.png` through `slide_07.png`
  - Exact dimensions: `2160 x 2700 px` (rendered from 1080x1350 canvas at 2x DPR).
- Generate `output/<brand-slug>_<YYYY-MM-DD>/caption.txt` containing the finalized caption, hook, hashtags, and CTA.
- Report completion and provide direct file paths to the user.
