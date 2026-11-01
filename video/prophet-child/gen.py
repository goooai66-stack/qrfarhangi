#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.05, 3.46, "أتت أمٌّ إلى النبيِّ صلى الله عليه وسلم بابنها المريض",
     "A mother brought her sick son to the Prophet (peace be upon him).", "一位母亲带着生病的儿子来见先知(愿主福安之)。"),
    (3.80, 4.49, "فماذا قال له؟", "So what did he say to him?", "他对那孩子说了什么?"),
    (5.25, 9.90, "روى أحمد أن النبيَّ صلى الله عليه وسلم أُتيَ بصبيٍّ مصابٍ بمسٍّ من الجن",
     "Ahmad narrated that the Prophet (peace be upon him) was brought a boy afflicted by jinn possession.",
     "艾哈迈德传述:有人把一个被精灵附体的男孩带到先知(愿主福安之)面前。"),
    (10.42, 12.54, "فجعل النبيُّ صلى الله عليه وسلم يقول:", "The Prophet (peace be upon him) began to say:", "先知(愿主福安之)开始说:"),
    (12.94, 14.35, "«اخرج عدوَّ الله", "“Come out, enemy of Allah!", "“出来,真主的敌人!"),
    (14.69, 15.75, "أنا رسول الله»", "I am the Messenger of Allah.”", "我是真主的使者。”"),
    (16.02, 17.76, "فبرأ الصبيُّ بإذن الله", "and the boy recovered, by Allah’s permission.", "凭真主的许可,那男孩痊愈了。"),
    (18.13, 21.25, "وهذا حديثٌ صحّح إسنادَه الحاكم ووافقه الذهبي",
     "This is a hadith whose chain al-Hakim graded sound, and al-Dhahabi agreed.", "这段圣训,哈基姆认定其传述系统可靠,扎哈比也表示同意。"),
    (21.71, 25.84, "وفيه أن النبيَّ صلى الله عليه وسلم خاطب ما في الصبي من الأذى بالحق",
     "In it, the Prophet (peace be upon him) addressed the harm within the boy with the truth,", "其中,先知(愿主福安之)用真理对男孩体内的邪害说话,"),
    (26.18, 28.03, "ولم يترك الأمَّ وابنها وحدهما", "and did not leave the mother and her son alone.", "并没有把母子二人单独丢下。"),
    (28.30, 32.60, "لكن هذا خاصٌّ بما ثبت عن النبي صلى الله عليه وسلم وبأهل العلم",
     "But this is specific to what is established from the Prophet (peace be upon him), and to people of knowledge,",
     "但这仅限于有确证出自先知(愿主福安之)的做法,以及有学识的人,"),
    (32.98, 34.85, "وليس لك أن تصنع مثله مع كل مريض", "and it is not for you to do the same with every sick person.", "你不应对每一个病人都这样做。"),
    (35.24, 38.60, "فكثيرٌ من الأطفال مرضُه عضويٌّ أو نفسيّ", "For many children, the illness is physical or psychological.", "因为许多孩子的病是身体上的或心理上的。"),
    (38.60, 41.29, "فإذا مرض طفلك فعوِّذه بالقرآن والأذكار", "So if your child falls ill, protect him with the Qur’an and the adhkar,", "所以,如果你的孩子生病了,用《古兰经》和祈祷词为他祈求庇护,"),
    (41.66, 43.37, "واذهب به إلى الطبيب فورًا", "and take him to the doctor right away.", "并立即带他去看医生。"),
    (44.13, 47.00, "شارك هذه القصة مع من تحب، وتابع القناة", "Share this story with someone you love, and follow the channel.",
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
