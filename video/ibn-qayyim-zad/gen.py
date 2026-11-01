#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.29, 2.69, "قصةُ شيخ الإسلام ابن تيمية مع المصروع", "The story of Shaykh al-Islam Ibn Taymiyyah with a person afflicted by a jinn,", "伊斯兰学者伊本·泰米叶与一位被精灵附体者的故事,"),
    (2.99, 4.61, "كما رواها تلميذه ابن القيم", "as told by his student Ibn al-Qayyim.", "由他的学生伊本·盖伊姆讲述。"),
    (5.27, 6.91, "يقول ابن القيم في «زاد المعاد»", "Ibn al-Qayyim says in Zad al-Ma‘ad:", "伊本·盖伊姆在《来世的干粮》中说:"),
    (7.30, 11.09, "وشهدتُ شيخَنا يرسل إلى المصروع من يخاطب الروح التي فيه",
     "I saw our Shaykh send someone to the afflicted person to address the spirit within him,", "我曾见我们的谢赫派人去找那位被附体者,与他体内的灵体对话,"),
    (11.36, 11.82, "ويقول", "saying:", "并说:"),
    (12.19, 13.76, "قال لك الشيخ: اخرجي", "“The Shaykh says to you: Come out,", "“谢赫对你说:出来,"),
    (14.10, 17.09, "فإن هذا لا يحل لك»، فيفيق المصروع", "for this is not permitted to you.” — and the person would come to.", "因为这对你是不允许的。”于是那人便清醒过来。"),
    (17.59, 18.78, "وربما خاطبها بنفسه", "Sometimes he addressed it himself,", "有时他亲自与之对话,"),
    (19.03, 21.38, "وكان ينهاها عن الظلم ويذكّرها بالله", "forbidding it from wrongdoing and reminding it of Allah.", "禁止它作恶,并提醒它敬畏真主。"),
    (22.18, 25.23, "وليس معنى هذا أن كل من يدّعي مخاطبة الجني صادق", "This does not mean everyone who claims to speak with a jinn is truthful.", "但这并不意味着每一个声称能与精灵交谈的人都是诚实的。"),
    (25.50, 32.06, "فكثير من الدجّالين يستغلون ذلك، ولا ينبغي للعامة أن تتكلف مثل هذا أو تعرّض المريض للأذى",
     "Many charlatans exploit this, and ordinary people should not take on such a thing or expose the patient to harm.",
     "许多骗子利用这一点;普通人不应勉强去做这类事,也不应让病人受到伤害。"),
    (32.93, 41.48, "وذكر ابن القيم أن أكثر ما تتسلط الأرواح الخبيثة على من قلّ دينه وخرب قلبه ولسانه من الذكر والتعاويذ والتحصينات النبوية",
     "Ibn al-Qayyim noted that harmful spirits most often overpower those whose religion is weak and whose heart and tongue are empty of dhikr, protective supplications and the Prophetic means of protection.",
     "伊本·盖伊姆指出:邪灵最常侵扰的,是信仰薄弱、心与舌缺少赞念、祈护词和先知所教的护佑方法的人。"),
    (41.76, 43.90, "فحصّن نفسك بالقرآن والأذكار", "So protect yourself with the Qur’an and the adhkar,", "所以,请用《古兰经》和祈祷词来护佑自己,"),
    (44.21, 46.15, "وراجع الطبيب إن استمرت الأعراض", "and see a doctor if the symptoms persist.", "如果症状持续,请去看医生。"),
    (46.67, 49.72, "شارك هذه القصة مع من تحب، وتابع القناة", "Share this story with someone you love, and follow the channel.", "把这个故事分享给你爱的人,并关注本频道。"),
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
