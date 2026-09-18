#!/usr/bin/env python3
"""
Playwright-based 2x Retina PNG renderer for Instagram Carousels (1080x1350 px, 4:5 ratio).
Snapshots all `.slide-canvas` elements inside an HTML template file.
Supports dynamic Jinja2 template rendering with autoescape and safe concurrent temp files.
"""

import os
import sys
import json
import tempfile
import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from playwright.sync_api import sync_playwright

def render_slides(html_path: str, output_dir: str, data_path: str = None, scale_factor: int = 2):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    template_file = Path(html_path).resolve()

    if not template_file.exists():
        raise FileNotFoundError(f"HTML template not found: {template_file}")

    temp_html_path = None
    if data_path:
        data_file = Path(data_path).resolve()
        if not data_file.exists():
            raise FileNotFoundError(f"Data file not found: {data_file}")
        
        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        env = Environment(
            loader=FileSystemLoader(str(template_file.parent)),
            autoescape=select_autoescape(["html", "xml"])
        )
        template = env.get_template(template_file.name)
        rendered_content = template.render(**data)

        # Use unique temporary file in template directory for safe concurrent execution and relative asset resolution
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=template_file.parent,
            prefix=f".rendered_{template_file.stem}_",
            suffix=".html",
            delete=False
        ) as tmp:
            tmp.write(rendered_content)
            temp_html_path = Path(tmp.name)

        target_html_to_load = temp_html_path
        print(f"[Renderer] Compiled Jinja template with data from: {data_file.name}")
    else:
        target_html_to_load = template_file

    abs_html_path = f"file://{target_html_to_load.resolve()}"
    print(f"[Renderer] Loading target HTML: {abs_html_path}")
    print(f"[Renderer] Target output directory: {output_path.resolve()}")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            try:
                page = browser.new_page(
                    viewport={"width": 1440, "height": 2200},
                    device_scale_factor=scale_factor
                )

                page.goto(abs_html_path, wait_until="networkidle")

                # Locate all slide canvas elements
                slide_elements = page.query_selector_all(".slide-canvas")
                if not slide_elements:
                    print("[Warning] No elements with class '.slide-canvas' found! Looking for body...")
                    target_file = output_path / "page_full.png"
                    page.screenshot(path=str(target_file))
                    print(f"[Renderer] Saved full page snapshot: {target_file}")
                    return

                print(f"[Renderer] Found {len(slide_elements)} slides to export.")

                for idx, element in enumerate(slide_elements, start=1):
                    target_file = output_path / f"slide_{idx:02d}.png"
                    element.screenshot(path=str(target_file))
                    target_w = 1080 * scale_factor
                    target_h = 1350 * scale_factor
                    print(f"  ✓ Exported: {target_file.name} ({target_w}x{target_h} @ {scale_factor}x DPR)")

                print("[Renderer] Export completed successfully!")
            finally:
                browser.close()
    finally:
        if temp_html_path and temp_html_path.exists():
            try:
                temp_html_path.unlink()
            except Exception as e:
                print(f"[Warning] Failed to remove temp HTML {temp_html_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Render HTML carousel slides to crisp PNGs.")
    parser.add_argument("--template", "-t", default="templates/carousels/magazine.html", help="Path to HTML template")
    parser.add_argument("--data", "-d", default=None, help="Optional path to JSON data payload for Jinja rendering")
    parser.add_argument("--output", "-o", default="output/latest-run", help="Output directory")
    parser.add_argument("--scale", "-s", type=int, default=2, help="Device scale factor (default: 2 for 2160x2700)")

    args = parser.parse_args()
    render_slides(args.template, args.output, args.data, args.scale)

if __name__ == "__main__":
    main()
