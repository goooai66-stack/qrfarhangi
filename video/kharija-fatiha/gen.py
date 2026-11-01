#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.31, 3.26, "قصة الرجل الذي قرأ الفاتحة ثلاثة أيام", "The story of the man who recited al-Fatihah for three days.", "那个连续三天诵读《开端章》的人的故事。"),
    (4.00, 8.23, "مرّ عمّ خارجة بن الصلت بقومٍ عندهم رجل مريض مقيّد بالحديد", "The uncle of Kharijah ibn al-Salt passed by some people who had a sick man bound in iron.", "哈里吉·本·萨勒特的叔叔路过一群人,他们那里有个被铁链捆着的病人。"),
    (8.67, 9.23, "فقال له", "One of them said to him:", "其中一人对他说:"),
    (9.56, 11.02, "هل عندك ما تداويه به؟", "“Do you have anything to treat him with?”", "“你有什么可以治疗他的办法吗?”"),
    (11.42, 13.15, "فقرأ عليه سورة الفاتحة", "So he recited Surat al-Fatihah over him", "于是他为那人诵读了《开端章》,"),
    (13.28, 14.07, "ثلاثة أيام", "for three days,", "连续三天,"),
    (14.31, 15.39, "صباحًا ومساءً", "morning and evening,", "早晚各一次,"),
    (15.74, 17.55, "يجمع بُزاقه ويتفل", "gathering his saliva and spitting lightly.", "聚起唾液轻轻吹出。"),
    (18.01, 19.65, "فكأنما نشط من عقال", "It was as if the man was released from a bond,", "那人仿佛挣脱了束缚,"),
    (20.02, 21.73, "وأعطاه القوم جعلًا من الغنم", "and the people gave him a payment of sheep.", "那些人给了他一份羊作为酬劳。"),
    (22.27, 24.51, "فأتى النبي صلى الله عليه وسلم وأخبره", "He came to the Prophet (peace be upon him) and told him,", "他来到先知(愿主福安之)面前,把事情告诉了他,"),
    (24.91, 26.85, "فقال له النبي صلى الله عليه وسلم", "and the Prophet (peace be upon him) said to him:", "先知(愿主福安之)对他说:"),
    (27.16, 27.40, "«كُلْ", "“Eat.", "“吃吧。"),
    (27.72, 29.75, "فلَعَمري لمن أكل برقية باطل", "By my life, whoever eats by a false ruqyah —", "我以生命起誓,有人靠虚假的咒语取食——"),
    (30.00, 31.49, "لقد أكلتَ برقية حقّ»", "you have eaten by a true ruqyah.”", "而你吃的是正当的诵经所得。”"),
    (31.98, 32.38, "تأمّل", "Reflect:", "请思考:"),
    (32.80, 35.90, "سورة الفاتحة التي تقرؤها كل يوم في صلاتك", "the Surat al-Fatihah you recite every day in your prayer", "你每天在礼拜中诵读的《开端章》,"),
    (36.19, 39.69, "هي نفسها الرقية التي أقرّها النبي صلى الله عليه وسلم", "is the very ruqyah the Prophet (peace be upon him) approved.", "正是先知(愿主福安之)所认可的那种诵经祛病。"),
    (40.26, 43.00, "شارك هذه القصة مع من تحب، وتابع القناة", "Share this story with someone you love, and follow the channel.", "把这个故事分享给你爱的人,并关注本频道。"),
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
