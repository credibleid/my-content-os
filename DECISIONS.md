# Architecture Decision Records (ADRs)

This document records architectural decisions for `my-content-os`.

## ADR-001: Dynamic Jinja2 Templating with Tailwind CDN and Hardened Isolation
- **Date:** 2026-09-18
- **Status:** Accepted
- **Context:** The content operating system requires rendering high-fidelity carousel templates (`.html` blueprints) into 2x Retina PNGs (`1080x1350 px` at `2x` device scale factor) via Playwright headless browser automation. Previously static or unrendered HTML files lacked dynamic data binding, and embedding complex CSS build tooling introduced heavy build step friction.
- **Decision:** Adopt Jinja2 templating engine with autoescape enabled (`select_autoescape(["html", "xml"])`) combined with Tailwind CSS via CDN loaded in HTML templates. Implement safe concurrent execution in [`engine/render.py`](file:///srv/agy-workspaces/my-content-os/engine/render.py#L41-L51) using unique temporary HTML files (`.rendered_{template}_...html`) within the template directory to ensure correct relative asset resolution and isolation.
- **Consequences:**
  - **Positive:** Zero heavy build steps (Tailwind CDN styling), robust dynamic data injection via JSON datasets, safe concurrent multi-process rendering without race conditions or asset path breakage, and pristine 2x Retina visual fidelity.
  - **Trade-offs / Drawbacks:** Requires network access during headless rendering for Tailwind CDN script execution, and template validation relies on runtime execution rather than compile-time bundlers.
