# رقية اليد على موضع الألم — SPEC

Vertical 1080×1920, 30 fps, 52.7 s (voice 50.05 s + 2.65 s hold on the channel name).
Narrated: the voice is the clock. Timing: the voice's 18 pauses (silencedetect −35 dB, 0.25 s) cut
the audio into 18 spoken chunks; each was transcribed with Whisper small (Arabic) and the
doubtful words checked against wider windows. Words inside a chunk are spread by letter count.

Text on screen is the transcript, nothing added from memory except two references the voice
does not say (hadith number on the seal, Persian meaning under the dua): both listed in REVIEW.md.

## Idea

The film is one colour arc. **Pain is warm** (amber orb, rose-amber wash over the night). The hand
lands, the name of God is said, the warmth turns **gold**, then **emerald calm**. Gold stays the one
accent and means "what heals": the dua, the cracks the light gets through, the answer.

## Look

- Night `#05121a → #0b2e27`; emerald drifting blobs; sparse warm stars (registry `starfield`);
  gold dust rising slowly; grain 0.06. Pain `#e07a5f`; gold `#d4a94f`; cream `#f4ecd8`; ink `#2a2418`.
- Type: Amiri Bold (hadith, dua, names), Cairo 800/900 (spoken lines, labels), Reem Kufi (counts).
  Nothing under 40 px. Content between 168 and 1130 px; captions at 1200; nothing under the rail.
- No people, faces or animals. Hand is line art; the eye is an outline; the "door" is a rectangle.
- BANNED by name: fade-and-slide-up on every element; floating or breathing loops on titles;
  titles that keep scaling after landing; the same entrance twice running; music; bounce on text.

## Shots

| # | Slot (s) | Anchor words → picture |
|---|---|---|
| 1 | 0–6.95 | frame 0 already shows «تشعر بألم / أو تظن أنك أُصبتَ بعين؟» over a pulsing amber orb · 0.9 «ألم» and 2.6 «بعين» go gold · 2.5 an eye outline draws round the orb (the orb is the pupil) · 3.45 «الخطوة الأولى» · 5.2 arrow from the orb to a door, 5.9 «أحد» the door is crossed out |
| 2 | 6.5–15.2 | whip in · hadith card · 7.0 «النبي ﷺ» plate · 8.7 gold arrow draws down · 9.2 «عثمان بن أبي العاص» plate · 11.5 amber spot «وجع» · 13.9 «صحيح مسلم» seal stamps (thump) |
| 3 | 14.9–19.75 | blur swap · 15.2 hand rises from below-right · 16.4 lands on the orb, chip «موضع الألم» · 17.3 three ticks «ثلاثًا» · 18.3 «بسم الله» big, ticks light 3×, amber → gold |
| 4 | 19.15–26.1 | gold flood (the orb becomes the world) fades to emerald · 19.9 ring of 7 beads fills «سبع» · 21.13 the dua, word by word, +Persian meaning at 22.9 · ring turns slowly · ring grows through the frame into scene 5 |
| 5 | 25.7–35.15 | 25.8 «لماذا؟» · 28.1 mihrab arch draws · 29.5 vessel (amber pulses «متألمًا») · 31.0 «منكسرًا» gold cracks draw, light pours out (crack) · 32.1–34.6 «الافتقار» meter fills |
| 6 | 34.8–45.6 | blur swap · 35.4 curve of «انكسار وافتقار» rises, dot rides it · 39.3 star «الإجابة» · 39.9 beam of light, dot «العبد» · 42.6 «ساجد»: dot descends, beam narrows and brightens (riser) · 43.2 touch: flare + rings · 43.8 «السجود = انكسار» |
| 7 | 45.25–52.2 | flare dissolves · 45.75 lamp ignites «ابدأ من اليوم» · 47.7 share arrow draws, three rings «شارك» · 50.1 «في معيّة الله» + «وأنا معه إذا ذكرني», held 2.2 s |

## Motion

Arrivals `expo.out`/`power4.out` 0.5–0.8 s; stamps `back.out`; exits 40–50 % shorter, `power3.in`.
Per-word blur 8 px → 0 in 0.16 s at the spoken word. Whip 0.3 s with 16 px blur (1→2). Blur swaps
(2→3, 5→6). Colour flood (3→4). Object grows into the world, the bead ring (4→5). Light flare (6→7).
Seven scenes in 52 s, each 6–9 s with a new beat every 1–3 s inside.

## Sound

Voice −15 LUFS. Pain pulses: soft thump at 0.25, 1.15, 2.05. Whoosh on the whip, the flood and the
ring. Stamp thump with the seal, a crack at 31.0, one noise riser into a thump at the sujūd touch
(the one riser in the film). No music, no tones.
