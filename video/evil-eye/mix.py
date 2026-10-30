#!/usr/bin/env python3
"""Mixes the voice (normalised to -15 LUFS) with the sound cues listed in sfx.json into mix.wav."""
import json, subprocess, sys
voice = sys.argv[1]
sfx = json.load(open("sfx.json"))
args = ["ffmpeg", "-y", "-v", "error", "-i", voice]
# loudnorm drops the last ~3 s of a stream that runs to its final sample, so pad first and trim after
fc, mix = "[0:a]aresample=48000,apad=pad_dur=5,loudnorm=I=-15:TP=-1.5:LRA=11,atrim=0:59.8[v];", "[v]"
for k, (t, name, vol) in enumerate(sfx, 1):
    args += ["-i", f"sfx/{name}.wav"]
    fc += f"[{k}:a]volume={vol},adelay={int(t * 1000)}|{int(t * 1000)}[s{k}];"
    mix += f"[s{k}]"
fc += f"{mix}amix=inputs={len(sfx) + 1}:normalize=0:duration=first,apad=pad_dur=0.2,atrim=0:59.8,alimiter=limit=0.84:level=false[out]"
args += ["-filter_complex", fc, "-map", "[out]", "-ar", "48000", "-c:a", "pcm_s16le", "mix.wav"]
subprocess.run(args, check=True)
print("mix.wav", len(sfx), "cues")
