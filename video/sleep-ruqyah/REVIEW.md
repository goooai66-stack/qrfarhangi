# REVIEW — رقية قبل النوم

Render: `../ruqyah-qabl-alnawm.mp4`, 1080×1920, 30 fps, 39.5 s, delivery quality (51 MB).
`hyperframes check`: passes.

## Creative calls

- One storyline, built without a pick: the person asked for the motion on their voice, so the
  three-storyline step was skipped. The voice is the clock; each beat lands on its word.
- Night look (sky, registry `starfield`, a hanging lamp) instead of the paper "Vox" look of the
  first short: this one is watched at bedtime. Gold carries meaning only (the ordinal, the
  protected thing, the channel name).
- No music, by intent: Quran-adjacent ruqyah content. Voice plus two whoosh and two pop takes.
- Transitions: whip (1→2), blur swap (2→3, 4→5, sequential), the كَفَتاه ring growing into the
  next scene (3→4).
- No people or faces; the hands are line art; the mushaf shows no real text.

## Measured vs. looked at

- Timing: from the voice's pauses (20 chunks ↔ 20 phrases), not a transcript. Words inside the
  three long chunks (8.25–12.04, 22.91–25.97, 26.24–30.29) are placed by word share.
- Looked at: the review sheets, every beat, the seams, and frames from the rendered file at the
  transitions.
- Sound measured, not heard: −14.1 LUFS integrated, −1.5 dBFS peak.

## Fixed in review

- 3.1 s: the hook shrank up into the lamp → it now lifts away and the title takes its place.
- 12.9 s: «حتى الصباح» sat on «حافظٌ من الله» → both lines moved up.
- 31.4 s: «×٣» landed on the dimmed hands → hands leave; a ×٣ with three ticking dots replaces
  the ×١ ×٢ ×٣ flashes (each was on screen 0.27 s, under the read floor).
- 37.6 s: «نَمِ الليلة» rose into the lamp → shorter move, the name sits lower.
- 13.5 s and 31.7 s: two scenes on screen at once → the incoming scene waits for the outgoing one.

## Weakest shot, and what next

- Scene 4 (19.25–31.85 s) carries the most: palms, three chips, the head → face → body path and
  the count. With more time: give "امسح" its own frame with an arrow sweeping down the palms.
- The breath dots at 21.6 s are small on a phone; a soft glow trail would read better.
- The hook says «في ثلاثين ثانية» and the film runs 38 s.

## Warnings kept

- `nested_structure_needs_subcomposition` on `#prog`: it only changes how the progress dots show
  in the editor's timeline, not the render.

## Editing note

The scene files were generated once and are now the source: edit `compositions/*.html` directly
(or in the HyperFrames desktop app). GSAP is vendored in `assets/vendor/` because the CDN is
blocked in the build environment.
