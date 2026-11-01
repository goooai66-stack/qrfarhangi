#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.27, 3.63, "آداب الرقية الشرعية التي يغفل عنها كثير من الناس", "The etiquette of sharʿī ruqyah that many people overlook:", "许多人忽视的合乎教法的诵经祛病礼仪:"),
    (4.31, 4.65, "أولًا:", "First:", "第一:"),
    (5.03, 5.94, "أخلِص النية لله", "Be sincere to Allah,", "要对真主心怀诚意,"),
    (6.20, 7.85, "واقرأ بيقين وحضور قلب", "recite with certainty and a present heart,", "带着笃信与专注的心去诵读,"),
    (8.00, 9.72, "واعتقد أن الشفاء بيد الله وحده", "and believe that healing is in Allah’s hand alone.", "并相信治愈只掌握在真主手中。"),
    (10.20, 10.51, "ثانيًا:", "Second:", "第二:"),
    (10.66, 14.28, "اقتصر على القرآن والأذكار الثابتة عن النبي صلى الله عليه وسلم", "Stick to the Qur’an and the adhkar authentically reported from the Prophet (peace be upon him),", "只用《古兰经》和确证出自先知(愿主福安之)的祈祷词,"),
    (14.42, 17.23, "ولا تقبل كلماتٍ لا تفهمها أو رموزًا مجهولة", "and do not accept words you do not understand or unknown symbols.", "不要接受你听不懂的词句或不明的符号。"),
    (17.90, 18.24, "ثالثًا:", "Third:", "第三:"),
    (18.51, 19.99, "ضع يدك على موضع الألم", "Place your hand on the place of pain,", "把手放在疼痛的部位,"),
    (20.20, 22.04, "كما علّم النبي صلى الله عليه وسلم", "as the Prophet (peace be upon him) taught,", "正如先知(愿主福安之)所教导的,"),
    (22.19, 24.18, "ولا بأس بالنفث الخفيف بلا مبالغة", "and a light blowing is fine, without exaggeration.", "轻轻吹气也无妨,但不要夸张。"),
    (24.86, 25.24, "رابعًا:", "Fourth:", "第四:"),
    (25.45, 26.94, "يُستحب أن تكون على طهارة", "It is recommended to be in a state of purity", "最好保持洁净的状态,"),
    (27.16, 28.93, "وأن تدعو بتضرّع وانكسار", "and to supplicate with humility and brokenness,", "并带着谦卑与恳切祈祷,"),
    (29.17, 30.54, "فهذا أقرب للإجابة", "for that is closer to being answered.", "这样更容易得到回应。"),
    (31.10, 31.54, "خامسًا:", "Fifth:", "第五:"),
    (31.74, 33.76, "لا تخلُ بامرأة أجنبية للرقية", "Do not be alone with an unrelated woman for ruqyah,", "不要为了诵经与非亲属女子独处,"),
    (33.99, 36.92, "ولا تضرب المريض ولا تطلب مالًا مقابل الشفاء", "do not strike the patient, and do not demand money in return for healing.", "不要殴打病人,也不要以治愈为条件索要钱财。"),
    (37.47, 37.88, "وأخيرًا:", "And finally:", "最后:"),
    (38.06, 40.25, "اجمع بين الرقية والأخذ بأسباب العلاج", "Combine ruqyah with taking the means of treatment,", "把诵经祛病与采取治疗措施结合起来,"),
    (40.53, 42.84, "فهذا هدي النبي صلى الله عليه وسلم", "for this is the guidance of the Prophet (peace be upon him).", "这正是先知(愿主福安之)的指引。"),
    (43.42, 45.84, "شارك هذا المقطع لمن تحب، وتابع القناة", "Share this clip with someone you love, and follow the channel.", "把这段视频分享给你爱的人,并关注本频道。"),
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
