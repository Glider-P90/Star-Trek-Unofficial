# Star Trek — KDE Plasma Theme

> *Unofficial* theme for KDE Plasma 5/6, inspired by the bridge of the USS Enterprise.

![Preview](wallpapers/starpac/preview.png)

## Palette

| Role | Color | Hex |
|------|-------|-----|
| Background | Deep space | `#060b15` |
| Panel | Bridge console | `#0d1b2a` |
| Text | Holo display | `#c8e6ff` |
| Accent | Cyan glow | `#00d4ff` |
| Highlight | Enterprise gold | `#ffb700` |
| Alert | Red alert | `#ff3333` |
| Success | Green channel | `#00e676` |

## Structure

```
Star-Trek-Unofficial/
├── theme.yaml              # Theme descriptor
├── colors/
│   └── StarTrek.colors     # Color scheme (KDE format)
├── wallpapers/
│   └── starpac/
│       ├── wallpaper.png   # 1920x1080 deep space
│       ├── preview.png     # 960x540 preview
│       └── metadata.json   # Wallpaper metadata
├── gen_wallpaper.py        # Wallpaper generator (Pillow + NumPy)
└── LICENSE                 # GPL-3
```

## Installation

### Method 1: Plasma Theme Manager (recommended)

```bash
# Install as a full Plasma theme
mkdir -p ~/.local/share/plasma-themes/StarTrek
cp -r theme.yaml colors wallpapers ~/.local/share/plasma-themes/StarTrek/

# Or install just the color scheme
mkdir -p ~/.local/share/color-schemes
cp colors/StarTrek.colors ~/.local/share/color-schemes/
```

Then in **System Settings → Appearance → Colors**, select **"StarTrek"**.

### Method 2: Wallpaper only

```bash
mkdir -p ~/.local/share/wallpapers
cp -r wallpapers/starpac ~/.local/share/wallpapers/
```

Then right-click desktop → Change Wallpaper → select **"starpac"**.

## Regenerating the Wallpaper

```bash
pip install Pillow numpy
python3 gen_wallpaper.py
```

The wallpaper is procedurally generated — no copyrighted assets.

## Notes

- This is an **unofficial** fan theme. Not affiliated with CBS, Paramount, or the Star Trek franchise.
- Icon theme defaults to **Breeze** (KDE default). For a full Star Trek icon set, create a custom icon theme and update `iconTheme` in `theme.yaml`.
- Window decoration defaults to **Default**. A custom KWin decoration can be added later.

## License

GPL-3.0 — see [LICENSE](LICENSE).
