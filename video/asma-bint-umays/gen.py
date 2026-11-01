#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.21, 4.37, "أمٌّ جاءت إلى النبي صلى الله عليه وسلم خائفةً على أولادها", "A mother came to the Prophet (peace be upon him), afraid for her children.", "一位母亲来到先知(愿主福安之)面前,为她的孩子们担忧。"),
    (4.64, 5.60, "فماذا قال لها؟", "So what did he say to her?", "他对她说了什么?"),
    (6.29, 10.53, "جاءت أسماء بنت عُميس رضي الله عنها إلى النبي صلى الله عليه وسلم وقالت", "Asma’ bint ‘Umays (may Allah be pleased with her) came to the Prophet (peace be upon him) and said:", "阿斯玛·宾特·欧迈斯(愿真主喜悦她)来见先知(愿主福安之),说:"),
    (10.88, 11.57, "يا رسول الله", "“O Messenger of Allah,", "“真主的使者啊,"),
    (12.02, 14.39, "إنّ بني جعفر تُسرع إليهم العين", "the evil eye afflicts the children of Ja‘far quickly.", "贾法尔的孩子们很容易被邪眼所伤。"),
    (14.73, 15.77, "أفأسترقي لهم؟", "Shall I seek ruqyah for them?”", "我可以为他们诵经祛病吗?”"),
    (16.18, 18.33, "فقال النبي صلى الله عليه وسلم: نعم", "The Prophet (peace be upon him) said: “Yes.", "先知(愿主福安之)说:“可以。"),
    (18.66, 20.37, "لو كان شيءٌ يسبق القدر", "If anything could outrun the decree,", "若有什么能胜过定命,"),
    (20.58, 21.62, "لسبقته العين»", "the evil eye would.”", "那就是邪眼了。”"),
    (21.92, 22.65, "رواه الترمذي", "(Narrated by al-Tirmidhi)", "(提尔密济传述)"),
    (23.24, 25.90, "فالنبي صلى الله عليه وسلم لم يسخر من خوفها", "The Prophet (peace be upon him) did not mock her fear,", "先知(愿主福安之)没有嘲笑她的担心,"),
    (26.14, 27.74, "ولم ينكر أن العين حقيقة", "nor deny that the evil eye is real,", "也没有否认邪眼是真实存在的,"),
    (28.30, 29.96, "بل أذن لها بالرقية لأولادها", "but permitted her to perform ruqyah for her children.", "而是允许她为孩子们诵经祛病。"),
    (30.61, 32.34, "فإن خفت على أولادك من العين", "So if you fear the evil eye for your children,", "所以,如果你担心孩子们受邪眼伤害,"),
    (32.47, 36.92, "فعوّذهم بما كان يعوّذ به النبي صلى الله عليه وسلم الحسن والحسين", "seek protection for them as the Prophet (peace be upon him) did for al-Hasan and al-Husayn:", "就用先知(愿主福安之)为哈桑和侯赛因祈求庇护的话来为他们祈护:"),
    (37.29, 38.95, "«أعيذكما بكلمات الله التامة", "“I seek refuge for you both in the perfect words of Allah", "“我借真主完美的言辞,为你们二人祈求庇护,"),
    (39.57, 41.15, "من كل شيطان وهامّة", "from every devil and every harmful creature,", "免受一切恶魔和一切毒害之物的伤害,"),
    (41.44, 42.85, "ومن كل عين لامّة»", "and from every evil eye.”", "也免受一切邪眼的伤害。”"),
    (43.47, 47.52, "شارك هذه القصة مع كل أم تخاف على أولادها، وتابع القناة", "Share this story with every mother who fears for her children, and follow the channel.", "把这个故事分享给每一位担心孩子的母亲,并关注本频道。"),
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
