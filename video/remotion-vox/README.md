# Ruqyah vox video — Remotion version

Horizontal (1920×1080, 30 fps) torn-paper "vox" explainer, Arabic voice with Arabic / English / Chinese captions.

- `content/caps.py` — caption cues (ASR segment ranges or explicit seconds) with AR / EN / ZH text
- `content/secs.py` — scene plan: sections, chips and Qur'an / hadith cards with their times
- `content/gen.py voice.wav` — writes `src/data.json`, the three `.srt` files, the Chinese font subset and `public/voice.wav` (−15 LUFS)
- `src/Vox.tsx` — the composition (paper background, sections, captions, voice + SFX); `src/icons.ts` sticker icons

Render:

```bash
cd content && python3 -I gen.py /path/to/voice.wav && cd ..
npx remotion render RuqyahVox out.mp4 --browser-executable=/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell --concurrency=4 --crf=18
```
