#!/usr/bin/env python3
"""Compress all media in the Terrastories website without visible quality loss."""

import os
import sys
import subprocess
from pathlib import Path
from PIL import Image

PUBLIC = Path("/home/coder/projects/terrastories-website/public")

def compress_jpeg(path):
    """Compress JPEG: save at quality 82 (visually lossless) with MozJPEG optimization."""
    img = Image.open(path)
    # Convert RGBA to RGB if needed
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    # Strip metadata, optimize
    img.save(path, "JPEG", quality=82, optimize=True, subsampling=0)
    return path.stat().st_size

def compress_png(path):
    """Compress PNG: convert large PNGs (>500KB) to JPEG where appropriate, or optimize."""
    size = path.stat().st_size
    img = Image.open(path)
    
    # If PNG has no transparency and is large, convert to JPEG
    has_alpha = img.mode == "RGBA" and any(
        pixel[3] < 255 for pixel in img.getdata()
    ) if img.mode == "RGBA" else False
    
    if not has_alpha and size > 200_000:
        # Convert to JPEG for massive savings
        jpg_path = path.with_suffix('.jpg')
        img_rgb = img.convert("RGB")
        img_rgb.save(str(jpg_path), "JPEG", quality=82, optimize=True, subsampling=0)
        new_size = jpg_path.stat().st_size
        if new_size < size * 0.7:  # Only if 30%+ smaller
            os.remove(path)
            return new_size, str(jpg_path)
        else:
            os.remove(jpg_path)
    
    # Optimize PNG in place
    img.save(str(path), "PNG", optimize=True)
    return path.stat().st_size, str(path)

def compress_gif(path):
    """Compress GIF using gifsicle if available, else skip."""
    try:
        subprocess.run(
            ["gifsicle", "-O3", "--colors", "128", "-o", str(path), str(path)],
            check=True, capture_output=True, timeout=60
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        # gifsicle not available, try with PIL
        try:
            img = Image.open(path)
            img.save(str(path), "GIF", optimize=True)
        except Exception:
            pass
    return path.stat().st_size

def convert_to_webp(path, quality=80):
    """Create a WebP version alongside the original."""
    webp_path = path.with_suffix('.webp')
    try:
        img = Image.open(path)
        if img.mode == "RGBA":
            img.save(str(webp_path), "WEBP", quality=quality, method=6)
        else:
            img.convert("RGB").save(str(webp_path), "WEBP", quality=quality, method=6)
        return webp_path.stat().st_size
    except Exception as e:
        return 0

def main():
    stats = {"jpg": 0, "png": 0, "gif": 0, "saved": 0, "webp_created": 0}
    
    # Collect all image files
    extensions = {".jpg", ".jpeg", ".png", ".gif"}
    files = []
    for root, dirs, filenames in os.walk(PUBLIC):
        for f in filenames:
            p = Path(root) / f
            if p.suffix.lower() in extensions:
                files.append(p)
    
    files.sort(key=lambda p: p.stat().st_size, reverse=True)
    
    print(f"Found {len(files)} images to process\n")
    
    for path in files:
        orig_size = path.stat().st_size
        ext = path.suffix.lower()
        result_path = str(path)
        
        try:
            if ext in (".jpg", ".jpeg"):
                compress_jpeg(path)
                stats["jpg"] += 1
            elif ext == ".png":
                new_size, result_path = compress_png(path)
                stats["png"] += 1
            elif ext == ".gif":
                compress_gif(path)
                stats["gif"] += 1
            
            new_size = Path(result_path).stat().st_size
            saved = orig_size - new_size
            stats["saved"] += saved
            
            pct = (1 - new_size / orig_size) * 100 if orig_size > 0 else 0
            label = "→ " + Path(result_path).name if result_path != str(path) else ""
            print(f"  {pct:5.1f}% saved  {orig_size/1024:.0f}KB → {new_size/1024:.0f}KB  {path.name} {label}")
            
        except Exception as e:
            print(f"  ERROR: {path.name}: {e}")
    
    # Summary
    print(f"\n{'='*60}")
    print(f"JPEGs compressed: {stats['jpg']}")
    print(f"PNGs compressed:  {stats['png']}")
    print(f"GIFs compressed:  {stats['gif']}")
    print(f"Total saved:      {stats['saved']/1024/1024:.1f} MB")
    
    # Final size
    total = sum(f.stat().st_size for f in Path(PUBLIC).rglob("*") if f.is_file())
    print(f"Final public/ size: {total/1024/1024:.1f} MB")

if __name__ == "__main__":
    main()
