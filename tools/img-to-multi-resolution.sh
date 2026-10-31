#!/usr/bin/env bash
SRC="/home/glider/Pictures/Background/star-trek/12245-3840x2160-desktop-4k-star-trek-wallpaper-photo.jpg"

resolutions=(
  1024x768
  1280x800
  1600x1200
  1920x1200
  3200x1800
  3840x2160
  720x1440
  1080x1920
  1366x768
  1680x1050
  2560x1440
  3200x2000
  440x247
  7680x2160
  1280x1024
  1440x900
  1920x1080
  2560x1600
  360x720
  5120x2880
)

for res in "${resolutions[@]}"; do
  out="${res}.png"
  sudo magick "$SRC" -resize "${res}^" -gravity center -extent "${res}" -quality 95 "$out"
  echo "✓ $out"
done
