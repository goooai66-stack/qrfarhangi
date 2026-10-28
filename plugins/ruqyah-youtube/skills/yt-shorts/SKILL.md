---
name: yt-shorts
description: >-
  Find the Shorts hiding inside a long video and write them, using the
  transcript to pick self-contained moments. Use for "cut this into shorts",
  "clip this", "repurpose this video", "what should I clip".
---

# yt-shorts

A Short cut out of a long video is not a clip of the best moment. It is a moment that **survives
without the video around it**, which is a much smaller set.

## Picking

Read the transcript and find spans of 20-55 seconds where all three are true:

1. It opens on a complete thought. If the first sentence needs the previous minute, it is not a Short.
2. There is a turn in it - a claim, then something that complicates or proves it.
3. It ends on a line, not a trail-off.

Rank the candidates and show the user the top five with their timecodes and first line, so they can
reject one without reading the whole transcript.

## Writing each one

- **A NEW first line.** The long video's line assumes context this viewer does not have. Write the
  replacement and run it through `../yt-script/hookscore.py`.
- **On-screen text for the first two seconds**, different words from the spoken line.
- **A loop point**: what the last line sets up so the first line answers it.
- Vertical framing note - what gets cropped out of a 16:9 frame and whether that matters.

## The niche

This channel is a Persian-language channel about **ruqyah shar'iyyah** (رقیه شرعیه). Before writing,
read `.claude/youtube/niche.md` in the current project (or `../../youtube/niche.md` from this skill's folder, the plugin's copy). Write every output in Persian. The red lines in that
file are hard limits: no promised or guaranteed cures, nothing that presents ruqyah as a replacement
for a doctor, no diagnosing anyone remotely, no fear-based packaging, and no Quranic text or hadith
written from memory. Leave a marked placeholder for the user to paste the verified text instead.
If a request crosses one of these lines, say which one and offer the version that stays inside it.

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user
copies, and the last line of every run is the question: **ship it, or change it?**
