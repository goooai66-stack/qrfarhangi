#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.28, 2.02, "قال النبي صلى الله عليه وسلم", "The Prophet (peace be upon him) said:", "先知(愿主福安之)说:"),
    (2.37, 3.78, "«اعرضوا عليَّ رُقاكم»", "“Present your ruqyahs to me.”", "“把你们的咒语念给我听。”"),
    (4.22, 5.66, "فما قصةُ هذه الجملة؟", "So what is the story behind this sentence?", "这句话背后有什么故事?"),
    (6.21, 9.00, "كان الناس في الجاهلية يرقون بكلمات فيها شرك", "In the Jahiliyyah, people used to perform ruqyah with words that contained shirk.", "在蒙昧时代,人们用含有多神崇拜内容的词句来念咒。"),
    (9.37, 10.40, "فلما جاء الإسلام", "When Islam came,", "伊斯兰到来后,"),
    (10.64, 13.61, "جاء آل عمرو بن حزم إلى النبي صلى الله عليه وسلم", "the family of ‘Amr ibn Hazm came to the Prophet (peace be upon him)", "阿慕尔·本·哈兹姆的家人来见先知(愿主福安之),"),
    (13.87, 14.35, "وقالوا", "and said:", "并说:"),
    (14.59, 16.89, "عندنا رُقيةٌ نَرقي بها من العقرب", "“We have a ruqyah we use for scorpion stings.”", "“我们有一种咒语,用来治疗蝎子蜇伤。”"),
    (17.32, 18.12, "فعرضوها عليه", "They presented it to him,", "他们把它念给他听,"),
    (18.52, 20.26, "فقال النبي صلى الله عليه وسلم", "and the Prophet (peace be upon him) said:", "先知(愿主福安之)说:"),
    (20.52, 21.57, "«ما أرى بأسًا", "“I see no harm in it.", "“我看不出有什么不妥。"),
    (21.84, 24.64, "من استطاع منكم أن ينفع أخاه فلينفعه»", "Whoever among you can benefit his brother, let him do so.”", "你们中谁能帮助自己的兄弟,就让他去帮助吧。”"),
    (24.98, 25.64, "رواه مسلم", "(Narrated by Muslim)", "(穆斯林传述)"),
    (26.25, 27.46, "وفي رواية أخرى قال", "In another narration he said:", "另一段传述中他说:"),
    (27.73, 30.03, "«لا بأس بالرُّقى ما لم يكن فيه شرك»", "“There is no harm in ruqyah as long as it contains no shirk.”", "“只要咒语中没有多神崇拜,就无妨。”"),
    (30.59, 31.60, "هذا هو الميزان", "This is the criterion:", "这就是标准:"),
    (32.08, 35.17, "كل رقية لا شرك فيها ولا كلمات مجهولة", "every ruqyah that has no shirk and no unknown words", "凡是没有多神崇拜、也没有不明词句的咒语,"),
    (35.17, 35.95, "فهي مشروعة", "is permissible,", "都是合法的;"),
    (36.29, 38.41, "وكل رقية فيها شرك أو طلاسم", "and every ruqyah that contains shirk or cryptic charms", "凡含有多神崇拜或神秘符咒的咒语,"),
    (38.72, 39.49, "فهي مردودة", "is rejected.", "都应被拒绝。"),
    (40.04, 42.45, "فاعرض ما تسمعه على القرآن والسنة", "So measure what you hear against the Qur’an and the Sunnah,", "所以,要把你听到的内容拿来对照《古兰经》和圣训,"),
    (42.56, 44.17, "ولا ترضَ بكلمات لا تفهمها", "and do not accept words you do not understand.", "不要接受你听不懂的词句。"),
    (44.70, 47.72, "شارك هذا المقطع مع من تحب، وتابع القناة", "Share this clip with someone you love, and follow the channel.", "把这段视频分享给你爱的人,并关注本频道。"),
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
