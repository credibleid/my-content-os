# My Content OS (`my-content-os`)

Autonomous Multi-Format Content Operating System (Instagram Carousels, Short-Form Video).

Designed as a self-contained Antigravity workspace with local project configuration in `.agents/`.

---

## 📁 Repository Layout

```text
my-content-os/
├── .agents/                                     # Antigravity project configuration
│   ├── rules/
│   │   ├── content-guidelines.md                # Mobile typography, safe margins, copy rules
│   │   └── video-guidelines.md                  # Vertical video 9:16 guidelines
│   └── skills/
│       ├── brand-profiler/SKILL.md              # Gate 1: Brand intake & SKU setup
│       ├── content-strategist/SKILL.md          # Gate 2 & 3: Pillars & 30-day calendar
│       ├── daily-drafter/SKILL.md               # Gate 4: 3 distinct angle drafts
│       ├── carousel-renderer/                   # Playwright rendering engine
│       └── video-reels-engine/SKILL.md          # (Phase 2) Vertical video generator
│
├── AGENTS.md                                    # Master project protocol & HITL gates
├── brands/                                      # Brand & product single source of truth
│   └── mgt-indonesia/                           # Golden Reference Tokopedia store
│       ├── profile.md
│       ├── content-pillars.md
│       ├── calendar-30d.md
│       └── products/
│           └── bel-wireless-waterproof/
│               ├── info.md
│               └── mockup.png
│
├── templates/
│   ├── carousels/                               # 4:5 HTML Carousel Templates
│   │   ├── magazine.html                        # High-Impact Magazine (Dark/Gold)
│   │   ├── minimalist.html                      # Minimalist Authority (Cream/Editorial)
│   │   ├── blueprint.html                       # Tech Framework Breakdown (Cyan)
│   │   └── assets/                              # Backgrounds, mockups, textures
│   └── video-templates/                         # Storyboard presets
│
├── engine/
│   └── render.py                                # Playwright snapshot runner CLI
│
└── output/                                      # Production PNG exports
```

---

## 🚀 Quick Start & Environment

This workspace uses an isolated Python virtual environment:

```bash
# Create venv and install dependencies
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt

# Install Playwright browser dependencies (if not already cached)
./.venv/bin/playwright install chromium
```

---

## 🎨 Rendering a Carousel

To render an HTML template into 7 crisp 2x Retina PNGs (2160x2700 px):

```bash
./.venv/bin/python engine/render.py \
  --template templates/carousels/magazine.html \
  --output output/demo-magazine/ \
  --scale 2
```

The exported slides will appear in `output/demo-magazine/slide_01.png` through `slide_07.png`.

---

## 🚦 Human-in-the-Loop (HITL) Workflow

When operating autonomously with an AI agent in this workspace:
1. **[HITL Gate 1] Brand & Product Setup:** Agent invokes `brand-profiler` -> User reviews and approves `profile.md` and SKU specs in `info.md`.
2. **[HITL Gate 2] Content Pillars:** Agent invokes `content-strategist` -> User reviews and approves the 4 content pillars in `content-pillars.md`.
3. **[HITL Gate 3] 30-Day Calendar:** Agent compiles calendar matrix -> User reviews and signs off on `calendar-30d.md`.
4. **[HITL Gate 4] Daily Draft Selection:** Agent invokes `daily-drafter` -> Presents 3 distinct creative angles -> User chooses the winning draft -> Agent invokes `carousel-renderer`.
