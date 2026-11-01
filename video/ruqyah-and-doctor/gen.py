#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.35, 1.88, "هل تغني الرقية عن الطبيب؟", "Does ruqyah replace the doctor?", "诵经祛病能代替医生吗?"),
    (2.15, 4.08, "الجواب يخطئ فيه كثير", "Many people get the answer wrong.", "很多人对这个问题的回答是错的。"),
    (4.61, 6.33, "قال النبي صلى الله عليه وسلم", "The Prophet (peace be upon him) said:", "先知(愿主福安之)说:"),
    (6.57, 7.96, "«ما أنزل الله داءً", "“Allah has not sent down a disease", "“真主降下任何一种疾病,"),
    (8.07, 9.59, "إلا أنزل له شفاءً»", "except that He sent down a cure for it.”", "必同时降下它的治疗。”"),
    (9.84, 10.97, "كما في صحيح البخاري", "(As in Sahih al-Bukhari)", "(见于《布哈里圣训集》)"),
    (11.39, 11.81, "وقال", "And he said:", "他还说:"),
    (12.10, 13.22, "«تداوَوْا عباد الله»", "“Seek treatment, servants of Allah.”", "“真主的仆人们啊,你们要求医治疗。”"),
    (14.13, 17.13, "فالنبي صلى الله عليه وسلم رَقى ورُقي به", "The Prophet (peace be upon him) performed ruqyah and had ruqyah performed for him,", "先知(愿主福安之)既为人诵经,也曾被人诵经,"),
    (17.48, 18.22, "وفي الوقت نفسه", "and at the same time", "同时"),
    (18.51, 20.05, "تداوى وأمر بالتداوي", "he sought treatment and commanded treatment,", "他也求医治疗,并吩咐人们治疗,"),
    (20.45, 21.86, "فلم يتعارض عنده الأمران", "so the two never conflicted for him.", "在他那里,这两者从不冲突。"),
    (22.56, 25.02, "فالرقية دعاء وتوكّل على الله", "Ruqyah is supplication and reliance on Allah,", "诵经祛病是祈祷,是依靠真主;"),
    (25.33, 27.23, "والطبيب سبب من أسباب الشفاء", "and the doctor is one of the means of healing,", "医生是治愈的途径之一,"),
    (27.76, 29.41, "وكلاهما بإذن الله وحده", "and both are by Allah’s permission alone.", "二者都唯有凭真主的许可。"),
    (29.96, 31.77, "فلا تترك الطبيب بحجة الرقية", "So do not abandon the doctor on the pretext of ruqyah,", "所以,不要以诵经为借口而放弃医生,"),
    (31.99, 34.15, "ولا تترك الرقية بحجة الطبيب", "and do not abandon ruqyah on the pretext of the doctor.", "也不要以医生为借口而放弃诵经。"),
    (34.76, 37.66, "اجمع بينهما كما فعل النبي صلى الله عليه وسلم", "Combine the two, as the Prophet (peace be upon him) did.", "要像先知(愿主福安之)那样,把二者结合起来。"),
    (38.76, 41.56, "أرسل هذا المقطع لمن تحب، وتابع القناة", "Send this clip to someone you love, and follow the channel.", "把这段视频发给你爱的人,并关注本频道。"),
]


def srt_time(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def write_srt():
    for code, k in {"ar": 2, "en": 3, "zh": 4}.items():
        with open(os.path.join(HERE, f"subtitles.{code}.srt"), "w", encoding="utf-8") as f:
            for i, c in enumerate(CAPS, 1):
                f.write(f"{i}\n{srt_time(c[0])} --> {srt_time(c[1])}\n{c[k]}\n\n")
        print("wrote", f"subtitles.{code}.srt", len(CAPS), "cues")


def fetch_font():
    chars = "".join(sorted({ch for c in CAPS for ch in c[4]}))
    css = subprocess.run(["curl", "-sS", "-m", "40", "-A", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
                          f"https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@500;700&text={quote(chars)}"],
                         capture_output=True, text=True, check=True).stdout
    url = re.search(r"url\((https://[^)]+)\)", css).group(1)
    subprocess.run(["curl", "-sS", "-m", "60", "-o", os.path.join(HERE, "fonts", "NotoSansSC-subset.woff2"), url], check=True)
    print("font subset:", len(chars), "characters")


def build_html():
    tpl = open(os.path.join(HERE, "comp.tpl.html"), encoding="utf-8").read()
    caps = [{"a": c[0], "b": c[1], "ar": c[2], "en": c[3], "zh": c[4]} for c in CAPS]
    open(os.path.join(HERE, "comp.html"), "w", encoding="utf-8").write(tpl.replace("__CAPS__", json.dumps(caps, ensure_ascii=False)))
    print("wrote comp.html")


if __name__ == "__main__":
    write_srt()
    if "--no-font" not in sys.argv:
        fetch_font()
    build_html()
