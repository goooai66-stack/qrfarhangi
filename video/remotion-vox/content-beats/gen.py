#!/usr/bin/env python3
"""Writes src/data.json for the Remotion composition, the three .srt files, the Chinese font subset and the loudness-normalised voice.
Usage (inside content/): python3 -I gen.py /path/to/voice.wav [--no-font]"""
import importlib.util, json, os, re, subprocess, sys
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
def load(name):
    s = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py")); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
caps, secs = load("caps"), load("secs")
asr = json.load(open(os.path.join(HERE, "asr.json")))["segs"]
voice = sys.argv[1]
OUT_JSON = next((a.split("=",1)[1] for a in sys.argv if a.startswith("--data=")), "data.json")
FONT_NAME = next((a.split("=",1)[1] for a in sys.argv if a.startswith("--zhfont=")), "NotoSansSC-subset.woff2")
OUT_VOICE = next((a.split("=",1)[1] for a in sys.argv if a.startswith("--voice=")), "voice.wav")
DUR = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", voice], capture_output=True, text=True, check=True).stdout)
def span(a, b):
    if isinstance(a, float): return a, b
    return asr[a]["start"] + 0.03, asr[b]["end"] - 0.06
CUES = []
for a, b, ar, en, zh in caps.CAPS:
    s, e = span(a, b); CUES.append({"a": round(s, 2), "b": round(e, 2), "ar": ar, "en": en, "zh": zh})
def tm(t):
    ms = int(round(t * 1000)); return f"{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}"
for code in ("ar", "en", "zh"):
    with open(os.path.join(HERE, f"subtitles.{code}.srt"), "w", encoding="utf-8") as f:
        for i, c in enumerate(CUES, 1): f.write(f"{i}\n{tm(c['a'])} --> {tm(c['b'])}\n{c[code]}\n\n")
if "--no-font" not in sys.argv:
    import glob
    pool = {ch for c in CUES for ch in c["zh"]}
    for fj in glob.glob(os.path.join(ROOT, "src", "data*.json")):
        if os.path.basename(fj) != OUT_JSON: pool |= {ch for c in json.load(open(fj))["caps"] for ch in c["zh"]}
    chars = "".join(sorted(pool))
    css = subprocess.run(["curl", "-sS", "-m", "60", "-A", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
        f"https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@500&text={quote(chars)}"], capture_output=True, text=True, check=True).stdout
    url = re.search(r"url\((https://[^)]+)\)", css).group(1)
    subprocess.run(["curl", "-sS", "-m", "90", "-o", os.path.join(ROOT, "public", "fonts", FONT_NAME), url], check=True)
    # voice normalised to -15 LUFS (padded first so loudnorm keeps the tail)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", voice, "-af", f"aresample=48000,apad=pad_dur=5,loudnorm=I=-15:TP=-1.5:LRA=11,atrim=0:{DUR}",
        "-ar", "48000", "-c:a", "pcm_s16le", os.path.join(ROOT, "public", OUT_VOICE)], check=True)
sfx = []; k = 0
for i, S in enumerate(secs.SECS):
    sfx.append([round(S["a"] + 0.02, 2), "whoosh-a" if i % 2 else "whoosh-b", 0.34])
    if S.get("num"): sfx.append([round(S["a"] + 0.3, 2), "thump", 0.3])
    for it in S["items"]:
        k += 1; sfx.append([it[0], "pop-a" if k % 2 else "pop-b", 0.26 if it[1] == "c" else 0.3])
sfx.sort()
json.dump({"dur": DUR, "voice": OUT_VOICE, "caps": CUES, "secs": secs.SECS, "sfx": sfx}, open(os.path.join(ROOT, "src", OUT_JSON), "w"), ensure_ascii=False)
print(len(CUES), "cues,", len(secs.SECS), "sections,", len(sfx), "sfx, dur", DUR)
