#!/usr/bin/env python3
"""Generate a Star Trek themed wallpaper - deep space with nebula and grid."""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import random

W, H = 1920, 1080
random.seed(42)

# Base: very dark space
img = Image.new('RGBA', (W, H), (6, 11, 21, 255))

# Nebula layer
nebula = Image.new('RGBA', (W, H), (0, 0, 0, 0))
nebula_draw = ImageDraw.Draw(nebula)
for _ in range(60):
    x = random.randint(0, W)
    y = random.randint(0, H)
    r = random.randint(80, 350)
    if random.random() < 0.7:
        color = (random.randint(0, 20), random.randint(30, 80), random.randint(60, 140), random.randint(15, 40))
    else:
        color = (random.randint(20, 50), random.randint(40, 80), random.randint(80, 140), random.randint(10, 30))
    nebula_draw.ellipse([x-r, y-r, x+r, y+r], fill=color)
nebula = nebula.filter(ImageFilter.GaussianBlur(radius=80))
img = Image.alpha_composite(img, nebula)

# Stars
stars = Image.new('RGBA', (W, H), (0, 0, 0, 0))
stars_draw = ImageDraw.Draw(stars)
for _ in range(500):
    x = random.randint(0, W)
    y = random.randint(0, H)
    b = random.randint(80, 255)
    s = random.choice([1, 1, 1, 2, 2, 3])
    stars_draw.ellipse([x, y, x+s, y+s], fill=(b, b, min(255, b+20), 255))
img = Image.alpha_composite(img, stars)

# Subtle grid (holodeck)
grid = Image.new('RGBA', (W, H), (0, 0, 0, 0))
grid_draw = ImageDraw.Draw(grid)
for x in range(0, W, 100):
    grid_draw.line([(x, 0), (x, H)], fill=(0, 180, 255, 10), width=1)
for y in range(0, H, 100):
    grid_draw.line([(0, y), (W, y)], fill=(0, 180, 255, 10), width=1)
img = Image.alpha_composite(img, grid)

# Vignette with numpy (fast)
img_rgb = np.array(img.convert('RGB'), dtype=np.float64)
y_coords = np.arange(H)[:, np.newaxis]
x_coords = np.arange(W)[np.newaxis, :]
cy, cx = H/2, W/2
dist = np.sqrt(((y_coords - cy)/cy)**2 + ((x_coords - cx)/cx)**2)
vignette = 1.0 - np.clip(dist - 0.5, 0, 1) * 0.5
vignette = np.stack([vignette]*3, axis=-1)
img_rgb = (img_rgb * vignette).astype(np.uint8)

img = Image.fromarray(img_rgb)
img.save('wallpapers/starpac/wallpaper.png', quality=95)
print("Wallpaper saved: wallpapers/starpac/wallpaper.png")

preview = img.resize((960, 540), Image.LANCZOS)
preview.save('wallpapers/starpac/preview.png', quality=90)
print("Preview saved: wallpapers/starpac/preview.png")
