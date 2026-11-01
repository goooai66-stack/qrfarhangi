#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.20, 2.11, "قال النبي صلى الله عليه وسلم", "The Prophet (peace be upon him) said:", "先知(愿主福安之)说:"),
    (2.35, 5.73, "«لأُعطينَّ الراية غدًا رجلًا يفتح الله على يديه»", "“Tomorrow I will give the banner to a man at whose hands Allah will grant victory.”", "“明天我要把旗帜交给一个人,真主将借他的手赐予胜利。”"),
    (6.31, 7.59, "وكانت المفاجأة في المرض", "And the surprise was — he was ill.", "令人意外的是——他正患着病。"),
    (8.20, 10.78, "في غزوة خيبر قال النبي صلى الله عليه وسلم", "At the battle of Khaybar, the Prophet (peace be upon him) said:", "在海拜尔之战中,先知(愿主福安之)说:"),
    (11.22, 12.47, "أين علي بن أبي طالب؟", "“Where is ‘Ali ibn Abi Talib?”", "“阿里·本·艾布·塔利卜在哪里?”"),
    (12.97, 13.32, "فقيل", "It was said:", "有人回答:"),
    (13.56, 14.32, "يا رسول الله", "“O Messenger of Allah,", "“真主的使者啊,"),
    (14.49, 15.51, "هو يشتكي عينيه", "he is suffering from his eyes.”", "他的眼睛有病。”"),
    (16.20, 17.54, "فأرسلوا إليه فأتوا به", "So they sent for him and brought him,", "他们便派人去叫他,把他带了来,"),
    (17.94, 20.88, "فبصق النبي صلى الله عليه وسلم في عينيه ودعا له", "and the Prophet (peace be upon him) spat lightly in his eyes and made du‘a for him,", "先知(愿主福安之)轻轻地向他的眼睛吹了唾沫,并为他祈祷,"),
    (21.30, 21.68, "فبرأ", "and he recovered", "于是他痊愈了,"),
    (22.05, 23.24, "كأن لم يكن به وجع", "as if he had never had any pain.", "仿佛从未有过任何疼痛。"),
    (23.61, 24.76, "رواه البخاري ومسلم", "(Narrated by al-Bukhari and Muslim)", "(布哈里与穆斯林传述)"),
    (25.17, 28.16, "وهذا من معجزات النبي صلى الله عليه وسلم", "This was one of the miracles of the Prophet (peace be upon him)", "这是先知(愿主福安之)的奇迹之一,"),
    (28.26, 29.66, "التي أكرمه الله بها", "with which Allah honoured him,", "是真主赐予他的恩典,"),
    (29.96, 31.32, "ولا يُفعل مثلها مع المرضى", "and the like of it is not done with patients.", "不能照此对待病人。"),
    (31.61, 32.31, "ولكن العبرة", "But the lesson", "但其中的教益"),
    (32.53, 34.73, "أنه دعا لعليّ وهو يتألم", "is that he made du‘a for ‘Ali while he was in pain", "是他在阿里痛苦时为他祈祷,"),
    (35.05, 36.01, "ولم يتركه مريضًا", "and did not leave him ill.", "没有让他一直病着。"),
    (36.82, 40.02, "علّمنا النبي صلى الله عليه وسلم أن المريض لا يُترك", "The Prophet (peace be upon him) taught us that a patient is not to be left alone:", "先知(愿主福安之)教导我们:不应让病人听之任之,"),
    (40.22, 40.83, "بل يُدعى له", "du‘a is made for him,", "而要为他祈祷,"),
    (41.10, 41.76, "ويُعالج", "he is treated,", "为他治疗,"),
    (41.99, 43.22, "ويُستشفى له من الله", "and healing is sought for him from Allah.", "并向真主为他求取康复。"),
    (43.88, 46.76, "شارك هذه القصة مع من تحب، وتابع القناة", "Share this story with someone you love, and follow the channel.", "把这个故事分享给你爱的人,并关注本频道。"),
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
