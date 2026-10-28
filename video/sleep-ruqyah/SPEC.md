# رقية قبل النوم — SPEC

Vertical 1080×1920, 30 fps, 39.5 s (voice 37.96 s + 1.5 s hold on the channel name).
Channel: في معيّة الله. Narrated: the voice is the clock; every beat lands on its anchor word.
Timings come from the voice's pauses (silencedetect −35 dB, 0.25 s): 20 spoken chunks matched
1:1 to the script's 20 phrases.

## Look

- Night: sky `#05121a` → `#0b2e27` (top → bottom). Dawn flood `#1d3a3a` → `#7a5a2e` at the horizon.
- Gold `#d4a94f` (one accent, carries meaning: the protected thing, the ordinal, the channel name).
  Cream `#f4ecd8` for running words. Muted `#9fb3ab`.
- Type: Amiri Bold for Quranic names and the channel name; Cairo 800/900 for spoken lines;
  Reem Kufi for the ordinals ١ ٢ ٣. Nothing under 40 px.
- Text only in the band 168–1330 px; captions at 1190 px. Nothing under the right action rail.
- Stars: registry `starfield` (warm, sparse). Grain: registry `grain-overlay` at 0.06.
- No people, faces or animals. Hands are line art. The mushaf carries no real text.

## Banned defaults

Fade-and-slide-up on every element; breathing or floating loops on titles; a slow creep after a
title lands; the same entrance twice in a row; music (Quran-adjacent content: voice and a few
effects only).

## Shots

| # | Slot (s) | Anchor words → picture |
|---|---|---|
| 1 | 0–6.25 | frame 0 already shows «تُريدُ أن تنامَ / في معيّة الله؟» under a hanging lamp · 2.37 «رُقيتُك قبل النوم» per-word blur-in, hook shrinks up · 4.50 chip «٣٠ ثانية» |
| 2 | 5.95–13.70 | whip in · 6.13 «١» spring · 6.93 «آيةُ الكرسيّ» + chip «البقرة ٢٥٥» · 8.25 bed line art · 11.3 gold dome draws over the bed, «حافظٌ من الله» · 12.35 dawn flood, «حتى الصباح» |
| 3 | 13.40–19.75 | blur swap · 13.77 «٢» · 14.54 «آخرُ آيتين» + chip «البقرة ٢٨٥–٢٨٦», mushaf, last two lines glow · 16.85 «في ليلةٍ» · 18.64 «كَفَتاه» in a gold ring; the ring's disc grows into the next scene |
| 4 | 19.25–31.85 | object becomes the world · 19.62 «٣» · 20.47 palms meet, 21.6 breath dots · 22.91 chips الإخلاص 23.93, الفلق 24.95, الناس 25.46 · 26.24 «امسح ما استطعتَ من جسدك», 29.3 الرأس → الوجه → الجسد · 30.64 ×١ ×٢ ×٣ |
| 5 | 31.55–39.5 | blur swap · 31.90 «رُقيةٌ يسيرة» · 33.26 «تقرؤها أنت بنفسك» · 35.16 lamp dims, «نَمِ الليلة» · 36.12 «في معيّة الله» + «وأنا معه إذا ذكرني», held to the end |

## Motion

Arrivals `expo.out`/`power4.out` 0.5–0.7 s; ordinals `back.out(1.4)`; exits 40–50 % shorter,
`power3.in`. Per-word blur 8 px → 0 in 0.16 s, 0.07 s apart. Whip 0.3 s with 16 px horizontal
blur. Transitions: whip (1→2), blur swap (2→3, 4→5), object becomes the world (3→4).

## Sound

Voice normalised to −15 LUFS. Two whoosh takes (the whip, the growing disc) and two pop takes
(ordinals, the three surah chips), each placed one frame after its picture. No music.
