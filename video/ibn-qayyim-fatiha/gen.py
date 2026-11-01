#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.30, 2.64, "ماذا فعل ابن القيم حين مرض في مكة", "What did Ibn al-Qayyim do when he fell ill in Makkah", "伊本·盖伊姆在麦加生病时做了什么"),
    (2.89, 4.88, "ولم يجد طبيبًا ولا دواءً؟", "and could find no doctor and no medicine?", "而且找不到医生,也找不到药?"),
    (5.65, 8.40, "يحكي الإمام ابن القيم رحمه الله في «زاد المعاد»", "Imam Ibn al-Qayyim (may Allah have mercy on him) recounts in Zad al-Ma‘ad", "伊本·盖伊姆伊玛目(愿真主怜悯他)在《来世的干粮》中讲述了"),
    (8.52, 9.59, "تجربتَه الشخصية", "his own personal experience.", "他自己的亲身经历。"),
    (10.19, 12.14, "مرّ بوقتٍ في مكة مرض فيه", "He went through a time in Makkah in which he fell ill", "他在麦加经历过一段生病的时期,"),
    (12.58, 14.17, "وفقد الطبيب والدواء", "and had neither doctor nor medicine.", "既没有医生,也没有药物。"),
    (15.01, 16.60, "فكان يعالج نفسه بالفاتحة", "So he treated himself with al-Fatihah:", "于是他用《开端章》为自己治疗:"),
    (16.87, 18.56, "يأخذ شربةً من ماء زمزم", "he would take a drink of Zamzam water,", "他取一口渗渗泉水,"),
    (18.82, 21.52, "ويقرأ عليها الفاتحة مرارًا ثم يشربها", "recite al-Fatihah over it several times, then drink it.", "在上面多次诵读《开端章》,然后喝下。"),
    (22.00, 22.40, "يقول:", "He says:", "他说:"),
    (22.75, 24.37, "فوجدتُ بذلك البُرء التامّ", "“I found complete recovery through it.", "“我借此获得了完全的康复。"),
    (24.83, 27.67, "ثم صرتُ أعتمد ذلك عند كثير من الأوجاع", "Then I came to rely on it for many kinds of pain,", "后来我在许多种疼痛时都依靠它,"),
    (27.94, 29.80, "فانتفعتُ بها غاية الانتفاع", "and I benefited from it greatly.”", "并从中获益良多。”"),
    (30.56, 33.80, "هذه تجربة عالمٍ جليل حين قطعت به الأسباب", "This is the experience of a great scholar when all means were cut off from him.", "这是一位伟大学者在一切途径都断绝时的经历。"),
    (34.22, 36.45, "لا تعني أن نترك الطبيب متى كان موجودًا", "It does not mean we should abandon the doctor when one is available.", "这并不意味着在有医生时我们就该放弃医生。"),
    (36.99, 38.74, "فاجمع بين الفاتحة والعلاج", "So combine al-Fatihah with treatment,", "所以要把《开端章》与治疗结合起来,"),
    (38.94, 41.51, "وقل كما قال النبي صلى الله عليه وسلم", "and say as the Prophet (peace be upon him) said:", "并像先知(愿主福安之)那样说:"),
    (41.72, 44.76, "«ما أنزل الله داءً إلا أنزل له شفاءً»", "“Allah has not sent down a disease except that He sent down a cure for it.”", "“真主降下任何一种疾病,必同时降下它的治疗。”"),
    (45.27, 48.32, "شارك هذه القصة مع من تحب، وتابع القناة", "Share this story with someone you love, and follow the channel.", "把这个故事分享给你爱的人,并关注本频道。"),
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
