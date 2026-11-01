#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.34, 1.53, "قصةٌ من بيت النبوة", "A story from the household of the Prophet.", "来自先知家中的一个故事。"),
    (1.95, 4.62, "كيف رقَتْ عائشةُ النبيَّ صلى الله عليه وسلم",
     "How ‘A’ishah performed ruqyah for the Prophet (peace be upon him)", "阿伊莎如何为先知(愿主福安之)诵经祛病"),
    (5.14, 6.95, "تقول عائشة رضي الله عنها", "‘A’ishah (may Allah be pleased with her) said:", "阿伊莎(愿真主喜悦她)说:"),
    (7.37, 11.65, "كان النبيُّ صلى الله عليه وسلم إذا اشتكى يقرأ على نفسه بالمعوّذات",
     "When the Prophet (peace be upon him) fell ill, he would recite the Mu‘awwidhat over himself,",
     "先知(愿主福安之)每当患病,就为自己诵读护佑诸章,"),
    (11.90, 12.57, "وينفث", "and blow lightly.", "并轻轻吹气。"),
    (13.14, 14.12, "فلما اشتدّ وجعه", "When his pain grew severe,", "当他的疼痛加剧时,"),
    (14.47, 17.45, "كانت عائشة تجلس عنده فتقرأ عليه بها", "‘A’ishah would sit by him and recite them over him,", "阿伊莎就坐在他身旁,为他诵读它们,"),
    (17.74, 20.39, "وتمسح عليه بيده رجاء بركتها", "and wipe him with his own hand, hoping for its blessing.", "并用他自己的手为他抚摩,希望得到那只手的福佑。"),
    (21.23, 22.47, "هذا هو نبيُّ الله", "This is the Prophet of Allah —", "这就是真主的先知——"),
    (22.79, 26.68, "وهو أعظم الخلق توكّلًا، يلجأ إلى القرآن عند المرض",
     "the one with the greatest trust in Allah of all creation — turning to the Qur’an in illness.",
     "他是万物中最信赖真主的人,生病时依然求助于《古兰经》。"),
    (26.96, 30.61, "ويرقي نفسه بنفسه، ثم ترقيه زوجته عند اشتداد الألم",
     "He recited over himself first, and his wife recited over him when the pain intensified.",
     "他先自己为自己诵读,疼痛加剧时,才由妻子为他诵读。"),
    (31.34, 33.67, "فلا تحتاج إلى شيخ أو قارئ مشهور", "So you do not need a sheikh or a famous reciter.", "所以,你不需要什么谢赫或名气很大的诵经者。"),
    (33.92, 35.71, "ابدأ بنفسك وبأهل بيتك", "Start with yourself and your family,", "从你自己和你的家人开始,"),
    (36.01, 39.02, "كما فعل النبيُّ صلى الله عليه وسلم وأهلُ بيته", "as the Prophet (peace be upon him) and his family did.", "就像先知(愿主福安之)和他的家人那样。"),
    (39.44, 42.56, "شارك هذه القصة مع من تحب، وتابع القناة", "Share this story with someone you love, and follow the channel.",
     "把这个故事分享给你爱的人,并关注本频道。"),
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
