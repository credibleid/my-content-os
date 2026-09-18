#!/usr/bin/env python3
"""
Playwright-based 2x Retina PNG renderer for Instagram Carousels (1080x1350 px, 4:5 ratio).
Snapshots all `.slide-canvas` elements inside an HTML template file.
"""

import os
import sys
import argparse
from pathlib import Path
from playwright.sync_api import sync_playwright

def render_slides(html_path: str, output_dir: str, scale_factor: int = 2):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    abs_html_path = f"file://{os.path.abspath(html_path)}"
    print(f"[Renderer] Loading template: {abs_html_path}")
    print(f"[Renderer] Target output directory: {output_path.resolve()}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Standard desktop viewport large enough to layout slide cards
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
            browser.close()
            return
            
        print(f"[Renderer] Found {len(slide_elements)} slides to export.")
        
        for idx, element in enumerate(slide_elements, start=1):
            target_file = output_path / f"slide_{idx:02d}.png"
            element.screenshot(path=str(target_file))
            target_w = 1080 * scale_factor
            target_h = 1350 * scale_factor
            print(f"  ✓ Exported: {target_file.name} ({target_w}x{target_h} @ {scale_factor}x DPR)")
            
        browser.close()
        print("[Renderer] Export completed successfully!")

def main():
    parser = argparse.ArgumentParser(description="Render HTML carousel slides to crisp PNGs.")
    parser.add_argument("--template", "-t", default="templates/carousels/magazine.html", help="Path to HTML template")
    parser.add_argument("--output", "-o", default="output/latest-run", help="Output directory")
    parser.add_argument("--scale", "-s", type=int, default=2, help="Device scale factor (default: 2 for 2160x2700)")
    
    args = parser.parse_args()
    render_slides(args.template, args.output, args.scale)

if __name__ == "__main__":
    main()
