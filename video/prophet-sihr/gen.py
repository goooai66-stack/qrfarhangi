#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.30, 2.99, "هل أصاب السحرُ النبيَّ صلى الله عليه وسلم", "Was the Prophet (peace be upon him) ever affected by sihr?", "先知(愿主福安之)是否曾受过巫术的影响?"),
    (3.22, 4.40, "وكيف شفاه الله؟", "And how did Allah cure him?", "真主又是如何治愈他的?"),
    (5.31, 8.21, "روت عائشة رضي الله عنها في صحيح البخاري أنّ", "‘A’ishah (may Allah be pleased with her) narrated in Sahih al-Bukhari that", "阿伊莎(愿真主喜悦她)在《布哈里圣训集》中传述:"),
    (8.32, 11.62, "رجلًا من اليهود سحر النبيَّ صلى الله عليه وسلم", "a man from the Jews cast sihr on the Prophet (peace be upon him),", "有一个犹太人对先知(愿主福安之)施了巫术,"),
    (12.00, 14.95, "فكان يُخيَّل إليه أنه فعل الشيء وما فعله", "so that he would imagine he had done something he had not done.", "以致他常觉得自己做了某件其实没做的事。"),
    (15.60, 18.23, "فدعا النبي صلى الله عليه وسلم ربَّه كثيرًا", "The Prophet (peace be upon him) called upon his Lord much,", "先知(愿主福安之)多次向他的主祈祷,"),
    (18.64, 20.34, "ثم أخبره الله بما أصابه", "and then Allah informed him of what had afflicted him,", "之后真主告知了他所遭遇的事,"),
    (20.65, 22.02, "ونزلت المعوذتان", "and the two Mu‘awwidhatayn were revealed.", "两章护佑章随之降示。"),
    (22.62, 25.21, "فكان كلما قرأ آيةً انحلّت عقدة", "Each time he recited a verse, a knot came undone,", "每当他诵读一节,就有一个结被解开,"),
    (25.52, 27.70, "حتى قام كأنما نشط من عقال", "until he stood up as if released from a bond.", "直到他起身时,仿佛挣脱了束缚。"),
    (28.43, 29.33, "فالسحر حقيقة", "Sihr is real,", "巫术是真实存在的,"),
    (29.63, 32.44, "لكن علاجه من هدي النبي صلى الله عليه وسلم: دعاء الله", "but its remedy follows the guidance of the Prophet (peace be upon him): supplication to Allah", "但它的疗法遵循先知(愿主福安之)的指引:向真主祈祷,"),
    (32.77, 33.65, "وقراءة المعوذتين", "and reciting the two Mu‘awwidhatayn,", "并诵读两章护佑章,"),
    (33.95, 35.31, "لا طلاسم ولا شعوذة", "not cryptic charms or sorcery.", "而不是什么符咒或巫术。"),
    (37.50, 41.91, "فلا تخف من السحر حتى تترك العلاج، ولا تنسب كل ما يصيبك إليه", "So do not fear sihr to the point of abandoning treatment, and do not blame everything that befalls you on it.", "所以,不要因害怕巫术而放弃治疗,也不要把你遇到的每件事都归咎于它。"),
    (42.41, 45.93, "حصّن نفسك بالأذكار وراجع الطبيب إن استمرت الأعراض", "Protect yourself with the adhkar, and see a doctor if the symptoms persist.", "用祈祷词护佑自己;如果症状持续,请去看医生。"),
    (46.41, 49.56, "شارك هذه القصة مع من تحب، وتابع القناة", "Share this story with someone you love, and follow the channel.", "把这个故事分享给你爱的人,并关注本频道。"),
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
