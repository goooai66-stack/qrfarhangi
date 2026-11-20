#!/usr/bin/env python3
"""Builds comp.html, the three .srt files, sfx.json and the Chinese font subset.  Usage: python3 -I gen.py [--no-font]  (inside this folder)"""
import importlib.util, json, os, re, subprocess, sys
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name):
    s = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py")); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
caps, secs = load("caps"), load("secs")
asr = json.load(open(os.path.join(HERE, "asr.json")))["segs"]
DUR = 498.04
CUES = [{"a": round(asr[a]["start"] + 0.03, 2), "b": round(asr[b]["end"] - 0.06, 2), "ar": ar, "en": en, "zh": zh} for a, b, ar, en, zh in caps.CAPS]
def tm(t):
    ms = int(round(t * 1000)); return f"{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}"
def write_srt():
    for code in ("ar", "en", "zh"):
        with open(os.path.join(HERE, f"subtitles.{code}.srt"), "w", encoding="utf-8") as f:
            for i, c in enumerate(CUES, 1): f.write(f"{i}\n{tm(c['a'])} --> {tm(c['b'])}\n{c[code]}\n\n")
    print("srt", len(CUES), "cues")
def fetch_font():
    chars = "".join(sorted({ch for c in CUES for ch in c["zh"]}))
    css = subprocess.run(["curl", "-sS", "-m", "60", "-A", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
        f"https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@500&text={quote(chars)}"], capture_output=True, text=True, check=True).stdout
    url = re.search(r"url\((https://[^)]+)\)", css).group(1)
    subprocess.run(["curl", "-sS", "-m", "90", "-o", os.path.join(HERE, "fonts", "NotoSansSC-subset.woff2"), url], check=True)
    print("font subset:", len(chars), "chars")
def build():
    tpl = open(os.path.join(HERE, "comp.tpl.html"), encoding="utf-8").read()
    out = tpl.replace("__DUR__", str(DUR)).replace("__CAPS__", json.dumps(CUES, ensure_ascii=False)).replace("__SECS__", json.dumps(secs.SECS, ensure_ascii=False))
    open(os.path.join(HERE, "comp.html"), "w", encoding="utf-8").write(out)
    sfx = []; k = 0
    for i, S in enumerate(secs.SECS):
        sfx.append([S["a"] + 0.02, "whoosh-a" if i % 2 else "whoosh-b", 0.34]);
        if S.get("num"): sfx.append([S["a"] + 0.3, "thump", 0.3])
        for it in S["items"]:
            k += 1; sfx.append([it[0], "pop-a" if k % 2 else "pop-b", 0.26 if it[1] == "c" else 0.3])
    sfx.sort(); json.dump(sfx, open(os.path.join(HERE, "sfx.json"), "w")); print("sfx", len(sfx), "cues; comp.html written")
if __name__ == "__main__":
    write_srt()
    if "--no-font" not in sys.argv: fetch_font()
    build()
