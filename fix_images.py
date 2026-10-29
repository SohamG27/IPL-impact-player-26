"""
Fix existing image filenames + create placeholder.
"""
import os
import shutil

IMG_DIR = os.path.join("static", "images", "players")

# Rename any spaces/mismatched names
renames = [
    ("Hardik Pandya.webp", "hardik_pandya.webp"),
]
for old, new in renames:
    src = os.path.join(IMG_DIR, old)
    dst = os.path.join(IMG_DIR, new)
    if os.path.exists(src) and not os.path.exists(dst):
        shutil.move(src, dst)
        print(f"Renamed: {old} -> {new}")

# Create SVG placeholder
placeholder_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 400 400">
  <rect width="400" height="400" fill="#1a1740"/>
  <circle cx="200" cy="155" r="75" fill="#2a2560"/>
  <ellipse cx="200" cy="330" rx="120" ry="70" fill="#2a2560"/>
  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="18" fill="#555">No Photo</text>
</svg>"""

png_path = os.path.join(IMG_DIR, "placeholder.png")
svg_path = os.path.join(IMG_DIR, "placeholder.svg")

with open(svg_path, "w") as f:
    f.write(placeholder_svg)

# Copy SVG content as placeholder.png fallback
shutil.copy(svg_path, png_path)
print("Placeholder files created.")
print("Fix script complete.")
