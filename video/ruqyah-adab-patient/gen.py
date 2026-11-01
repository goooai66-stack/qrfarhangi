#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py [--no-font]   (run inside this folder)"""
import json, os, re, subprocess, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, Arabic, English, Chinese)
CAPS = [
    (0.24, 4.61, "تتمّة آداب الرقية الشرعية: ما تحتاجه أنت كمريض قبل أن تبدأ", "More on the etiquette of sharʿī ruqyah — what you need as the patient before you begin:", "合乎教法的诵经祛病礼仪(续)——作为病人,开始之前你需要做到:"),
    (4.85, 5.22, "أولًا:", "First:", "第一:"),
    (5.36, 6.35, "أحسِن الظن بالله", "Think well of Allah,", "要对真主存有好的期望,"),
    (6.66, 7.96, "فهو عند ظنّ عبده به", "for He is as His servant expects Him to be,", "因为真主正如祂的仆人所期望的那样,"),
    (8.26, 9.44, "ولا تستعجل النتيجة", "and do not rush the result,", "不要急于求成,"),
    (9.67, 12.01, "فالشفاء يأتي في وقته الذي يريد", "for healing comes in the time He wills.", "因为治愈会在祂所意愿的时间到来。"),
    (12.60, 12.93, "ثانيًا:", "Second:", "第二:"),
    (13.26, 15.05, "كرِّر الرقية وداوم عليها", "Repeat the ruqyah and keep at it,", "反复诵读并持之以恒,"),
    (15.28, 17.18, "فالعبد يُستجاب له ما لم يستعجل", "for a servant’s prayer is answered as long as he does not grow hasty.", "因为只要仆人不急躁,他的祈祷就会被回应。"),
    (17.69, 18.05, "ثالثًا:", "Third:", "第三:"),
    (18.30, 19.59, "استغفر وتُب إلى الله", "Seek forgiveness and turn back to Allah,", "求饶恕并向真主悔改,"),
    (19.74, 22.05, "وحافظ على الصلوات وأذكار الصباح والمساء", "keep up the prayers and the morning and evening adhkar,", "坚持礼拜和早晚的赞念,"),
    (22.54, 24.00, "فالطاعة هي الحصن الدائم", "for obedience is the lasting fortress.", "因为顺从是持久的堡垒。"),
    (24.59, 25.01, "رابعًا:", "Fourth:", "第四:"),
    (25.16, 26.06, "اصبر على البلاء", "Be patient with the trial,", "要耐心面对考验,"),
    (26.39, 27.63, "فالمرض يكفِّر السيئات", "for illness expiates sins", "因为疾病能抵消罪过,"),
    (27.91, 28.85, "ويرفع الدرجات", "and raises ranks", "也能提升品级,"),
    (29.12, 30.47, "إذا صبر المؤمن واحتسب", "when the believer is patient and seeks reward from Allah.", "只要信士忍耐并寄望真主的回报。"),
    (31.07, 31.47, "خامسًا:", "Fifth:", "第五:"),
    (31.72, 32.92, "لا تتعلّق بالراقي", "Do not become attached to the reciter,", "不要依附诵读者,"),
    (33.18, 35.62, "ولا تجعل نجاح الرقية مرهونًا بشخص", "and do not make the success of ruqyah depend on one person,", "也不要让诵经的成效取决于某个人,"),
    (35.86, 36.81, "فالشافي هو الله", "for the Healer is Allah.", "因为医治者是真主。"),
    (37.29, 39.13, "وإن طال المرض أو اشتدّت الأعراض", "If the illness drags on or the symptoms worsen,", "如果病情拖延或症状加重,"),
    (39.40, 42.11, "فراجع الطبيب مع استمرارك في الرقية والدعاء", "see a doctor while continuing the ruqyah and du‘a.", "请在继续诵经和祈祷的同时去看医生。"),
    (42.64, 45.40, "أرسل هذا المقطع لمن تحب، وتابع القناة", "Send this clip to someone you love, and follow the channel.", "把这段视频发给你爱的人,并关注本频道。"),
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
