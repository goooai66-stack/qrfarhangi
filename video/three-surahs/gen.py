#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.05, 2.25, "ثلاثُ سورٍ قصيرة", "Three short surahs", "三章短章"),
    (2.25, 5.56, "قال عنها النبيُّ صلى الله عليه وسلم إنها تكفيك من كل شيء",
     "the Prophet (peace be upon him) said they are enough for you against everything.", "先知(愿主福安之)说,它们足以护佑你远离一切。"),
    (6.22, 10.20, "قال عبدُ الله بن خُبيب رضي الله عنه: خرجنا في ليلة مطيرة وظلمة شديدة",
     "‘Abdullah ibn Khubayb (may Allah be pleased with him) said: We went out on a rainy night, in deep darkness,",
     "阿卜杜拉·本·胡拜卜(愿真主喜悦他)说:我们在一个下雨的漆黑夜晚出门,"),
    (10.20, 14.52, "نطلب رسول الله صلى الله عليه وسلم ليصلّي بنا",
     "looking for the Messenger of Allah (peace be upon him) to lead us in prayer,", "寻找真主的使者(愿主福安之),请他带我们礼拜,"),
    (14.82, 15.49, "فأدركناه", "and we caught up with him.", "我们追上了他。"),
    (15.95, 17.02, "فقال: قل", "He said: “Say.”", "他说:“说。”"),
    (17.46, 18.36, "فلم أقل شيئًا", "I said nothing.", "我没有说话。"),
    (18.79, 20.09, "ثم قال: قل", "Then he said: “Say.”", "他又说:“说。”"),
    (20.36, 21.55, "فلم أقل شيئًا", "I said nothing.", "我还是没有说话。"),
    (21.92, 23.07, "ثم قال: قل", "Then he said again: “Say.”", "他再次说:“说。”"),
    (23.51, 24.33, "قلتُ: ما أقول؟", "I said: “What should I say?”", "我说:“我该说什么?”"),
    (24.76, 30.32, "قال: «قل هو الله أحد والمعوّذتين، حين تمسي وحين تصبح، ثلاث مرات",
     "He said: “Say Qul huwa Allahu ahad and the two Mu‘awwidhatayn, when you reach the evening and when you reach the morning, three times —",
     "他说:“你念《忠诚章》和两章护佑章,在傍晚和清晨各念三遍——"),
    (30.65, 33.85, "تكفيك من كل شيء» رواه أبو داود والترمذي",
     "they will be enough for you against everything.” (Narrated by Abu Dawud and al-Tirmidhi)", "它们足以护佑你远离一切。”(艾布·达伍德与提尔密济传述)"),
    (34.42, 37.40, "ثلاث سور قصيرة تقرؤها في دقيقة صباحًا ومساءً",
     "Three short surahs you can recite in a minute, morning and evening,", "三章短章,一分钟就能念完,早晚各一次,"),
    (37.40, 40.73, "فتكون حصنًا لك بإذن الله", "and by Allah’s permission they become a fortress for you.", "凭真主的许可,它们将成为你的堡垒。"),
    (41.13, 44.13, "مع الأخذ بأسباب العلاج ومراجعة الطبيب عند الحاجة",
     "Take the means of treatment too, and see a doctor when needed.", "同时也要采取治疗措施,需要时请去看医生。"),
    (44.73, 47.60, "شارك هذه القصة مع من تحب، وتابع القناة", "Share this story with someone you love, and follow the channel.",
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
    chars = "".join(sorted({ch for c in CAPS for ch in c[4]} | set("点击关注")))
    css = subprocess.run(["curl", "-sS", "-m", "40", "-A", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
                          f"https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@500;700&text={quote(chars)}"],
                         capture_output=True, text=True, check=True).stdout
    url = re.search(r"url\((https://[^)]+)\)", css).group(1)
    subprocess.run(["curl", "-sS", "-m", "60", "-o", os.path.join(HERE, "fonts", "NotoSansSC-subset.woff2"), url], check=True)
    print("font subset:", len(chars), "characters")


def build_html():
    tpl = open(os.path.join(HERE, "comp.tpl.html"), encoding="utf-8").read()
    # the first caption would only repeat the big title on screen
    caps = [{"a": c[0], "b": c[1], "ar": "" if i == 0 else c[2], "en": c[3], "zh": c[4]} for i, c in enumerate(CAPS)]
    open(os.path.join(HERE, "comp.html"), "w", encoding="utf-8").write(tpl.replace("__CAPS__", json.dumps(caps, ensure_ascii=False)))
    print("wrote comp.html")


if __name__ == "__main__":
    write_srt()
    if "--no-font" not in sys.argv:
        fetch_font()
    build_html()
