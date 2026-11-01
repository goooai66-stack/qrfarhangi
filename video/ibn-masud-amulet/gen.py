#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.30, 4.02, "دخل ابن مسعود على زوجته فرأى شيئًا في رقبتها", "Ibn Mas‘ud entered upon his wife and saw something around her neck.", "伊本·麦斯欧德走进妻子的房间,看到她脖子上挂着什么东西。"),
    (4.35, 5.14, "ماذا فعل؟", "What did he do?", "他做了什么?"),
    (5.98, 11.20, "كانت زينب امرأةُ عبد الله بن مسعود رضي الله عنهما قد علّقت في رقبتها خيطًا",
     "Zaynab, the wife of ‘Abdullah ibn Mas‘ud (may Allah be pleased with them both), had hung a thread around her neck", "宰奈卜是阿卜杜拉·本·麦斯欧德(愿真主喜悦他们俩)的妻子,她在脖子上挂了一根线,"),
    (11.51, 13.24, "لأن عينها كانت تؤلمها", "because her eye was hurting her,", "因为她的眼睛疼,"),
    (13.57, 15.27, "وكانت تظن أنه ينفعها", "and she thought it would help her.", "她以为这样会有帮助。"),
    (15.89, 18.48, "فلما رآه عبد الله قطعه وقال", "When ‘Abdullah saw it, he cut it off and said:", "阿卜杜拉看到后把它扯断,并说:"),
    (18.94, 21.58, "«إنّ آل عبد الله لأغنياء عن الشرك", "“The family of ‘Abdullah have no need of shirk.", "“阿卜杜拉的家人不需要多神崇拜。"),
    (22.25, 25.09, "سمعت رسول الله صلى الله عليه وسلم يقول", "I heard the Messenger of Allah (peace be upon him) say:", "我听到真主的使者(愿主福安之)说:"),
    (25.48, 28.21, "إنّ الرُّقى والتمائم والتِّوَلة شرك»", "‘Indeed, spells, amulets and love charms are shirk.’”", "‘咒语、护身符和爱情符咒都是多神崇拜。’”"),
    (28.73, 29.81, "رواه أبو داود", "(Narrated by Abu Dawud)", "(艾布·达伍德传述)"),
    (30.25, 30.92, "والمقصود", "What is meant", "这里指的是"),
    (31.35, 35.18, "الرُّقى التي فيها شرك، أما الرقية بالقرآن فهي مشروعة", "is ruqyah that contains shirk. As for ruqyah with the Qur’an, it is permitted.", "含有多神崇拜内容的咒语。至于用《古兰经》诵经祛病,则是合法的。"),
    (35.82, 39.39, "فلا تعلّق خرزاتٍ ولا خيوطًا ولا أشياء لدفع العين", "So do not hang beads, threads, or anything else to ward off the evil eye.", "所以,不要为了防邪眼而佩戴珠子、线绳或任何东西。"),
    (39.80, 43.51, "فالحماية تكون بالذكر والتوكل على الله وحده", "Protection comes through dhikr and reliance on Allah alone.", "护佑来自赞念,以及只依靠真主。"),
    (44.07, 47.80, "شارك هذا المقطع مع من تحب، وتابع القناة", "Share this clip with someone you love, and follow the channel.", "把这段视频分享给你爱的人,并关注本频道。"),
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
