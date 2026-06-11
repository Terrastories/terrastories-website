#!/usr/bin/env python3
"""Resize all images in public/media/images/ to max 1200px wide.
Originals are backed up to _originals/ outside public/.
Preserves animated GIFs and transparent PNGs."""

import os
import shutil
from pathlib import Path
from PIL import Image

PUBLIC = Path("/home/coder/projects/terrastories-website/public/media/images")
ORIGINALS = Path("/home/coder/projects/terrastories-website/_originals/media/images")
MAX_WIDTH = 1200
MAX_HEIGHT = 1200  # Also cap height for square images

def is_transparent(img):
    if img.mode == "RGBA":
        return any(pixel[3] < 255 for pixel in img.getdata())
    return False

def main():
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    
    stats = {"resized": 0, "skipped": 0, "error": 0, "saved": 0}
    
    files = sorted(f for f in PUBLIC.iterdir() if f.suffix.lower() in {'.jpg', '.jpeg', '.png', '.gif', '.webp'})
    print(f"Found {len(files)} images to check\n")
    
    for path in files:
        try:
            img = Image.open(path)
            w, h = img.size
            
            # Skip animated GIFs
            if path.suffix.lower() == '.gif' and getattr(img, 'n_frames', 1) > 1:
                print(f"  SKIP (animated GIF): {path.name}")
                stats["skipped"] += 1
                continue
            
            # Skip if already within limits
            if w <= MAX_WIDTH and h <= MAX_HEIGHT:
                print(f"  SKIP (within limits {w}x{h}): {path.name}")
                stats["skipped"] += 1
                continue
            
            # Backup original
            backup = ORIGINALS / path.name
            if not backup.exists():
                shutil.copy2(path, backup)
            
            orig_size = path.stat().st_size
            
            # Resize
            if path.suffix.lower() == '.png':
                img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.LANCZOS)
                img.save(str(path), "PNG", optimize=True)
            elif path.suffix.lower() in ('.jpg', '.jpeg'):
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.LANCZOS)
                img.save(str(path), "JPEG", quality=82, optimize=True, subsampling=0)
            elif path.suffix.lower() == '.gif':
                # Single-frame GIF, convert to JPEG for efficiency
                img_rgb = img.convert("RGB")
                img_rgb.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.LANCZOS)
                new_path = path.with_suffix('.jpg')
                img_rgb.save(str(new_path), "JPEG", quality=82, optimize=True, subsampling=0)
                # Keep the old GIF reference for now (content update needed separately)
                print(f"  NOTE: Single-frame GIF -> JPEG (need to update references): {path.name}")
                stats["resized"] += 1
                continue
            elif path.suffix.lower() == '.webp':
                img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.LANCZOS)
                if img.mode == "RGBA":
                    img.save(str(path), "WEBP", quality=80, method=6)
                else:
                    img.convert("RGB").save(str(path), "WEBP", quality=80, method=6)
            
            new_size = path.stat().st_size
            new_w, new_h = img.size
            saved = orig_size - new_size
            stats["saved"] += saved
            stats["resized"] += 1
            pct = (1 - new_size / orig_size) * 100 if orig_size > 0 else 0
            print(f"  RESIZED {w}x{h} -> {new_w}x{new_h} ({pct:.0f}% saved, {orig_size/1024:.0f}KB -> {new_size/1024:.0f}KB): {path.name}")
            
        except Exception as e:
            print(f"  ERROR: {path.name}: {e}")
            stats["error"] += 1
    
    print(f"\n{'='*60}")
    print(f"Resized: {stats['resized']}")
    print(f"Skipped: {stats['skipped']}")
    print(f"Errors:  {stats['error']}")
    print(f"Total saved: {stats['saved']/1024/1024:.1f} MB")
    print(f"Originals backed up to: {ORIGINALS}")
    
    # Final size
    total = sum(f.stat().st_size for f in PUBLIC.rglob("*") if f.is_file())
    print(f"Final public/media/images/ size: {total/1024/1024:.1f} MB")

if __name__ == "__main__":
    main()
