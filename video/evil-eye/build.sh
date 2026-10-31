#!/usr/bin/env bash
# Builds the trilingual short from the Arabic voice. Usage: ./build.sh /path/to/voice.wav
# Needs: node + playwright (Chromium), ffmpeg, python3.  No HyperFrames.
set -euo pipefail
cd "$(dirname "$0")"
VOICE="$1"; OUT="${2:-evil-eye-ar-en-zh}"; FPS=30; DUR=59.8; N=1794
python3 -I gen.py --no-font
rm -rf frames && mkdir frames
for i in 0 1 2 3; do node render.js "$PWD/comp.html" "$PWD/frames" $((i*N/4)) $(((i+1)*N/4)) $FPS & done; wait
node -e "
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ args: ['--allow-file-access-from-files'] }); const p = await b.newPage();
  await p.goto('file://$PWD/comp.html'); await p.evaluate(() => window.ready);
  console.log(JSON.stringify(await p.evaluate(() => window.SFX))); await b.close(); })();" > sfx.json
python3 -I mix.py "$VOICE"
ffmpeg -y -v error -framerate $FPS -i frames/f%05d.jpg -i mix.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -profile:v high -movflags +faststart -c:a aac -b:a 192k -shortest "../$OUT.mp4"
echo done
