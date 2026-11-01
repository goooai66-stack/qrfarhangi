#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.05, 3.42, "ماذا حدث مع الشيخ ابن باز عندما جاءت امرأة مصابة؟",
     "What happened with Sheikh Ibn Baz when an afflicted woman came to him?", "当一位被精灵附体的妇女来找谢赫伊本·巴兹时,发生了什么?"),
    (4.00, 6.29, "ذكر الشيخ عبد العزيز بن باز رحمه الله",
     "Sheikh ‘Abd al-‘Aziz ibn Baz (may Allah have mercy on him) mentioned", "谢赫阿卜杜勒-阿齐兹·伊本·巴兹(愿真主怜悯他)提到"),
    (6.38, 9.01, "أن امرأة كانت مصابة بمسٍّ من الجن،", "that a woman was afflicted by jinn possession,", "有一位妇女被精灵附体,"),
    (9.47, 11.71, "وأن الجني أعلن إسلامه أمامه", "and that the jinn declared his Islam in front of him.", "并且那个精灵当着他的面宣布了皈依伊斯兰。"),
    (12.26, 13.72, "ولما أنكر بعض الناس ذلك", "When some people denied this,", "有些人对此表示否认,"),
    (13.97, 17.49, "كتب الشيخ مقالًا يبيّن فيه أن دخول الجني في الإنسي",
     "the Sheikh wrote an article showing that a jinn’s entering a human", "谢赫便写了一篇文章,说明精灵进入人体"),
    (17.89, 20.70, "ثابت بالقرآن والسنة وإجماع أهل السنة",
     "is established by the Qur’an, the Sunnah and the consensus of Ahl al-Sunnah,", "这一点已由《古兰经》、圣训以及逊尼派学者的共识所证实,"),
    (21.14, 22.27, "وأن إنكاره خطأ", "and that denying it is a mistake.", "而否认它是错误的。"),
    (22.90, 23.87, "ولكن تنبّه", "But be careful:", "但请注意:"),
    (24.13, 29.27, "العلماء أنفسهم يقولون إن كثيرًا من المدّعين لمخاطبة الجن كاذبون",
     "the scholars themselves say that many of those who claim to speak with jinn are liars.", "学者们自己也说,许多声称能与精灵交谈的人都是骗子。"),
    (29.71, 31.55, "فلا تصدّق كل من يدّعي ذلك،", "So do not believe everyone who claims that,", "所以,不要相信每一个这样声称的人,"),
    (31.55, 33.17, "ولا تنسب كل مرض إلى الجن", "and do not attribute every illness to jinn.", "也不要把每一种疾病都归咎于精灵。"),
    (33.58, 35.49, "والحق في المسألة وسط", "The truth in this matter is the middle way:", "此事的真相在于中道:"),
    (35.90, 38.75, "لا إنكار للمسّ الثابت بالنص، ولا مبالغة فيه",
     "no denial of possession that is established by the text, and no exaggeration of it,", "既不否认经文所确证的附体,也不夸大它,"),
    (39.03, 41.30, "والجمع بين الرقية الشرعية والطبيب", "and combining sharʿī ruqyah with the doctor.", "并将合乎教法的诵经祛病与医生治疗结合起来。"),
    (41.45, 44.32, "شارك هذا المقطع مع من تحب، وتابع القناة", "Share this clip with someone you love, and follow the channel.",
     "把这段视频分享给你爱的人,并关注本频道。"),
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
