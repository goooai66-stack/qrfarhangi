# Vox-style motion: الرُّقية الشرعية vs كتابة الحُجُب

`comp.html` is the whole animation, driven by `render(t)` (seconds) and timed to the
ElevenLabs voice track (Mohammed Almansari, 46.3 s). Rendered videos are not committed.

```bash
# frames (4 parallel workers, 1410 frames at 30 fps)
mkdir -p frames && for i in 0 1 2 3; do node render.js $PWD/comp.html $PWD/frames $((i*1410/4)) $(((i+1)*1410/4)) 30 & done; wait
# stills for review
node stills.js $PWD/comp.html /tmp 0.6 8.1 19.5
# encode with the mixed audio (voice + whoosh/thud SFX, loudnorm -14 LUFS)
ffmpeg -framerate 30 -i frames/f%05d.jpg -i mix.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 18 \
  -pix_fmt yuv420p -movflags +faststart -c:a aac -b:a 192k -shortest ../ruqyah-vs-hujub-vox.mp4
```

Fonts: Cairo, Reem Kufi, Amiri (SIL Open Font License).
