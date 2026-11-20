#!/usr/bin/env bash
# Builds the horizontal trilingual long-form video (vox torn-paper style) from the Arabic voice.
# Usage: ./build.sh /path/to/voice.wav [output-name]     Needs node + playwright (Chromium), ffmpeg, python3.  One file out: the MP4.
set -euo pipefail
cd "$(dirname "$0")"
VOICE="$1"; OUT="${2:-evil-eye-kids-vox-ar-en-zh}"; FPS=30; export DUR=498.04; N=14942
python3 -I gen.py --no-font
rm -rf seg && mkdir seg
for i in 0 1 2 3; do node render.js "$PWD/comp.html" "$PWD/seg/p$i.mp4" $((i*N/4)) $(((i+1)*N/4)) $FPS & done; wait
python3 -I mix.py "$VOICE"
printf "file 'p%s.mp4'\n" 0 1 2 3 > seg/list.txt
ffmpeg -y -v error -f concat -safe 0 -i seg/list.txt -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -movflags +faststart -shortest "../$OUT.mp4"
echo done
