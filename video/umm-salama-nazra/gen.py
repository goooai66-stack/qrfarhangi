#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.23, 3.90, "رأى النبي صلى الله عليه وسلم في بيت أم سلمة فتاةً", "The Prophet (peace be upon him) saw a girl in the house of Umm Salamah", "先知(愿主福安之)在温姆·赛拉姆的家里看到一个女孩,"),
    (4.01, 5.60, "فقال لها جملةً عجيبة", "and said a remarkable sentence about her.", "并说了一句令人惊讶的话。"),
    (6.17, 8.76, "دخل النبي صلى الله عليه وسلم على أم سلمة رضي الله عنها", "The Prophet (peace be upon him) entered upon Umm Salamah (may Allah be pleased with her),", "先知(愿主福安之)进入温姆·赛拉姆(愿真主喜悦她)的家,"),
    (8.88, 9.75, "وفي البيت فتاة", "and in the house was a girl", "家里有个女孩,"),
    (10.08, 11.98, "بوجهها سَفْعة", "with a mark on her face —", "她的脸上有一块印记——"),
    (12.32, 13.89, "أي صُفرة وعلامة مرض", "a yellowish pallor, a sign of illness.", "即发黄和生病的迹象。"),
    (14.42, 16.13, "فقال النبي صلى الله عليه وسلم", "The Prophet (peace be upon him) said:", "先知(愿主福安之)说:"),
    (16.52, 17.43, "«استرقوا لها", "“Seek ruqyah for her,", "“为她诵经祛病吧,"),
    (17.72, 18.72, "فإن بها النَّظرة»", "for she has been struck by the nazrah.”", "因为她中了邪眼。”"),
    (19.07, 20.10, "أي أصابتها العين", "That is, the evil eye had struck her.", "也就是说,她被邪眼所伤。"),
    (20.43, 22.11, "كما في صحيح البخاري ومسلم", "As in Sahih al-Bukhari and Muslim.", "见于《布哈里圣训集》和《穆斯林圣训集》。"),
    (22.68, 25.56, "لم ينتظر النبي صلى الله عليه وسلم ولم يهمل الأمر", "The Prophet (peace be upon him) neither waited nor neglected the matter,", "先知(愿主福安之)既没有等待,也没有忽视这件事,"),
    (25.91, 27.36, "بل أمر بالرقية فورًا", "but ordered ruqyah at once.", "而是立即吩咐诵经祛病。"),
    (27.74, 29.25, "فهذا تعليمٌ منه لأمّته", "This is a lesson from him to his Ummah:", "这是他对自己乌玛的教导:"),
    (29.62, 30.85, "ألا تستخفّ بالعين", "do not take the evil eye lightly,", "不要轻视邪眼,"),
    (31.10, 33.19, "وألا تتأخر في التحصين والعلاج", "and do not delay protection and treatment,", "也不要在护佑和治疗上拖延,"),
    (33.76, 35.58, "ولكن لا تجعل كل عَرَضٍ عينًا", "but do not make every symptom an evil eye.", "但也不要把每一种症状都当作邪眼。"),
    (35.94, 36.94, "فإن استمر المرض", "If the illness continues,", "如果疾病持续,"),
    (37.20, 38.51, "فراجع الطبيب مع الرقية", "see a doctor alongside ruqyah.", "请在诵经祛病的同时去看医生。"),
    (39.00, 42.20, "شارك هذه القصة مع من تحب، وتابع القناة", "Share this story with someone you love, and follow the channel.", "把这个故事分享给你爱的人,并关注本频道。"),
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
