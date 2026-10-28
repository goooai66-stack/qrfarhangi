---
name: yt-chapters
description: >-
  Write YouTube chapters from a transcript, validated against YouTube's own
  rules so they actually render. Use for "add chapters", "timestamps",
  "break this video into sections".
---

# yt-chapters

```bash
python3 chapters.py transcript.srt --target 8
```

## The rules, which are not optional

A chapter list that breaks any of these silently does not become chapters at all - the block just
sits in the description doing nothing:

- The first entry must be **00:00**.
- There must be **at least three**.
- Each must be **at least 10 seconds** long.

The tool checks all three and tells you when a list is invalid rather than letting you paste it.

## Retitle every line

`chapters.py` finds the BOUNDARIES well - it scores the pauses you actually took by how much the
vocabulary shifts across them. The titles it emits are the topic words, and they are a draft. A
chapter called "Thumbnails Titles Packaging" is a placeholder. Rewrite each one as the promise of
that section, in the user's voice, three to five words.

Chapters are also a retention diagnostic: if a section cannot be named in five words, it is two
sections or it is filler.

## The niche

This channel is a Persian-language channel about **ruqyah shar'iyyah** (رقیه شرعیه). Before writing,
read `.claude/youtube/niche.md` in this repo. Write every output in Persian. The red lines in that
file are hard limits: no promised or guaranteed cures, nothing that presents ruqyah as a replacement
for a doctor, no diagnosing anyone remotely, no fear-based packaging, and no Quranic text or hadith
written from memory. Leave a marked placeholder for the user to paste the verified text instead.
If a request crosses one of these lines, say which one and offer the version that stays inside it.

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user
copies, and the last line of every run is the question: **ship it, or change it?**
