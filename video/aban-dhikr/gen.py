#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.23, 2.24, "رجلٌ نظر إلى أبان بن عثمان", "A man looked at Aban ibn ‘Uthman", "有个人注视着阿班·本·奥斯曼"),
    (2.43, 4.57, "فسأله سؤالًا غيّر القصة", "and asked him a question that changed the story.", "并问了他一个改变整个故事的问题。"),
    (5.15, 9.38, "كان أبان بن عثمان رحمه الله يحدّث عن أبيه عثمان رضي الله عنه",
     "Aban ibn ‘Uthman (may Allah have mercy on him) used to narrate from his father ‘Uthman (may Allah be pleased with him)", "阿班·本·奥斯曼(愿真主怜悯他)曾转述其父奥斯曼(愿真主喜悦他)的话:"),
    (9.79, 11.96, "أن النبيَّ صلى الله عليه وسلم قال", "that the Prophet (peace be upon him) said:", "先知(愿主福安之)说:"),
    (12.32, 12.84, "من قال", "Whoever says:", "谁若念:"),
    (13.27, 17.09, "«بسم الله الذي لا يضرُّ مع اسمه شيءٌ في الأرض ولا في السماء", "“In the name of Allah, with whose name nothing on earth or in heaven can cause harm,",
     "“奉真主之名,有祂的名字,天地间任何事物都不能伤害,"),
    (17.42, 19.47, "وهو السميع العليم» ثلاث مرات", "and He is the All-Hearing, the All-Knowing” — three times,", "祂是全听的、全知的”——念三遍,"),
    (19.80, 21.86, "لم تصبه فجأةُ بلاءٍ حتى يصبح", "no sudden affliction will strike him until morning.", "直到早晨,突如其来的灾祸都不会降临到他身上。"),
    (22.02, 24.96, "وكان أبان قد أصابه فالج", "Now Aban had been struck by paralysis.", "而阿班自己曾患过中风。"),
    (25.31, 28.08, "فجعل الرجل الذي سمع الحديث ينظر إليه", "The man who heard the hadith kept looking at him.", "那位听到这段圣训的人一直盯着他看。"),
    (28.48, 29.51, "فقال له أبان:", "Aban said to him:", "阿班对他说:"),
    (29.76, 30.51, "ما لك تنظر؟", "“Why are you staring?", "“你为什么盯着我看?"),
    (31.00, 32.81, "أما إن الحديث كما حدّثتك", "The hadith is exactly as I told you,", "这段圣训确如我对你所说,"),
    (33.10, 36.49, "ولكنني لم أقله يومئذٍ ليمضي الله قدره", "but I did not say it on that day, so that Allah’s decree would take its course.”", "只是那天我没有念它,好让真主的定命得以实现。”"),
    (36.80, 38.32, "رواه أبو داود والترمذي", "(Narrated by Abu Dawud and al-Tirmidhi)", "(艾布·达伍德与提尔密济传述)"),
    (38.83, 41.32, "أذكار الصباح والمساء هي حصنٌ من الله", "The morning and evening adhkar are a fortress from Allah,", "早晚的赞念是来自真主的堡垒,"),
    (41.62, 45.09, "ولكنها لا تمنع قدر الله إذا أراد ابتلاء عبده", "but they do not prevent Allah’s decree when He wills to test His servant.", "但当真主要考验祂的仆人时,它们并不能阻止真主的定命。"),
    (45.54, 48.02, "ولا يعني من مرض أنه قصّر في الذكر", "And it does not mean that whoever falls ill was negligent in dhikr.", "患病并不意味着他在赞念上有所疏忽。"),
    (48.20, 49.56, "فاحفظ هذا الذكر", "So keep this dhikr,", "所以请记住这句赞念,"),
    (49.68, 52.15, "وقله ثلاث مرات صباحًا ومساءً", "and say it three times, morning and evening.", "早晚各念三遍。"),
    (52.57, 55.72, "شارك هذه القصة مع من تحب، وتابع القناة", "Share this story with someone you love, and follow the channel.", "把这个故事分享给你爱的人,并关注本频道。"),
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
