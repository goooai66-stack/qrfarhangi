#!/usr/bin/env python3
"""Builds comp.html (from comp.tpl.html), the three .srt files and the Chinese font subset.
Usage: python3 -I gen.py   (run inside this folder)"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# (start, end, show_arabic, Arabic, English, Chinese).  show_arabic=False where the Arabic is already
# on screen in big type (the duas), so the caption area carries only the two translations.
CAPS = [
    (0.08, 0.95, False, "العينُ حق", "The evil eye is real.", "邪眼是真实存在的。"),
    (1.17, 4.07, True, "كما قال النبيُّ صلى الله عليه وسلم في صحيح مسلم",
     "As the Prophet (peace be upon him) said in Sahih Muslim.", "正如先知(愿主福安之)在《穆斯林圣训集》中所说。"),
    (4.39, 7.08, True, "فكيف نتحصّن من العين والحسد؟",
     "So how do we protect ourselves from the evil eye and envy?", "那么,我们该如何防护邪眼和嫉妒?"),
    (8.09, 10.64, True, "ابدأ بالمحافظة على أذكار الصباح والمساء",
     "Start by keeping up the morning and evening remembrances (adhkar),", "首先,坚持早晚的赞念,"),
    (11.00, 13.16, True, "وقراءة آية الكرسي والمعوّذات",
     "and by reciting Ayat al-Kursi and the Mu‘awwidhat.", "并诵读《宝座节》和护佑诸章。"),
    (13.97, 17.30, True, "وإن خفتَ على نفسك أو على ولدك فقل",
     "If you fear for yourself or for your child, say", "如果你为自己或孩子担忧,就念诵"),
    (17.30, 20.19, True, "ما كان النبيُّ صلى الله عليه وسلم يعوّذ به الحسنَ والحسين",
     "what the Prophet (peace be upon him) used to recite to protect al-Hasan and al-Husayn:",
     "先知(愿主福安之)曾为哈桑和侯赛因念诵、求真主护佑的话:"),
    (21.30, 24.91, False, "",
     "“I seek refuge in the perfect words of Allah from every devil and every venomous creature,",
     "“我凭真主完美的言辞求庇护,远离一切恶魔和一切毒虫,"),
    (25.23, 26.74, False, "", "and from every harmful evil eye.”", "也远离一切带来伤害的邪眼。”"),
    (27.52, 31.30, True, "وإذا رأيتَ ما يعجبك من مال أو ولد أو نعمة فقل",
     "When you see something you admire — wealth, a child, a blessing — say:",
     "当你看到令你欣羡的财富、孩子或恩赐时,请说:"),
    (31.30, 34.78, False, "", "“Mā shā’ Allāh. Tabārak Allāh. O Allah, bless it.”",
     "“真主所意欲的!真主赐福!主啊,求你降福于它。”"),
    (35.21, 37.19, True, "فهذا من أعظم أسباب الوقاية",
     "This is one of the greatest means of prevention.", "这是最重要的预防方法之一。"),
    (37.77, 41.95, True, "وإن أصابتك العينُ فاقرأ على نفسك الفاتحة والمعوّذات",
     "If the evil eye does strike you, recite al-Fatiha and the Mu‘awwidhat over yourself,",
     "如果邪眼伤到了你,请为自己诵读《开端章》和护佑诸章,"),
    (41.95, 45.61, True, "وضعْ يدك على موضع الألم وقل: بسم الله ثلاثًا",
     "place your hand on the spot of pain, and say “Bismillah” three times,",
     "把手放在疼痛的地方,念“奉真主之名”三遍,"),
    (46.03, 50.87, False, "",
     "then say: “I seek refuge in the might and power of Allah from the evil of what I feel and what I fear” — seven times.",
     "然后念:“我凭真主的尊荣与权能求庇护,免遭我所感到的和我所畏惧的灾害”,共七遍。"),
    (51.22, 55.34, True, "مع الأخذ بأسباب العلاج ومراجعة الطبيب إن استمرّت الأعراض",
     "And take the means of treatment too — see a doctor if the symptoms persist.",
     "同时也要采取治疗措施;如果症状持续,请去看医生。"),
    (55.77, 57.83, True, "شارك هذا المقطع مع من يحتاجه", "Share this clip with someone who needs it", "把这段视频分享给需要的人"),
    (58.10, 59.80, True, "واحفظه لترجع إليه", "and save it so you can come back to it.", "并收藏起来,以便日后再看。"),
]


def srt_time(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def write_srt():
    langs = {"ar": 3, "en": 4, "zh": 5}
    for code, k in langs.items():
        lines, n = [], 0
        for c in CAPS:
            text = c[k]
            if code == "ar" and not text:
                continue  # the dua is shown on screen, the Arabic track still needs it:
            lines.append((c[0], c[1], text))
        # for the Arabic track fill the on-screen duas back in
        if code == "ar":
            duas = {21.30: "أَعُوذُ بِكَلِمَاتِ اللَّهِ التَّامَّةِ مِنْ كُلِّ شَيْطَانٍ وَهَامَّةٍ", 25.23: "وَمِنْ كُلِّ عَيْنٍ لَامَّةٍ",
                    31.30: "مَا شَاءَ اللَّهُ، تَبَارَكَ اللَّهُ، اللَّهُمَّ بَارِكْ فِيهِ",
                    46.03: "ثُمَّ: أَعُوذُ بِعِزَّةِ اللَّهِ وَقُدْرَتِهِ مِنْ شَرِّ مَا أَجِدُ وَأُحَاذِرُ — سَبْعًا"}
            lines = [(c[0], c[1], c[3] or duas[c[0]]) for c in CAPS]
        with open(os.path.join(HERE, f"subtitles.{code}.srt"), "w", encoding="utf-8") as f:
            for i, (a, b, t) in enumerate(lines, 1):
                f.write(f"{i}\n{srt_time(a)} --> {srt_time(b)}\n{t}\n\n")
        print("wrote", f"subtitles.{code}.srt", len(lines), "cues")


def fetch_font():
    chars = "".join(sorted({ch for c in CAPS for ch in c[5]}))
    from urllib.parse import quote
    css = subprocess.run(["curl", "-sS", "-m", "40", "-A", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
                          f"https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@500;700&text={quote(chars)}"],
                         capture_output=True, text=True, check=True).stdout
    url = re.search(r"url\((https://[^)]+)\)", css).group(1)
    subprocess.run(["curl", "-sS", "-m", "60", "-o", os.path.join(HERE, "fonts", "NotoSansSC-subset.woff2"), url], check=True)
    print("font subset:", len(chars), "characters,", os.path.getsize(os.path.join(HERE, "fonts", "NotoSansSC-subset.woff2")), "bytes")


def build_html():
    tpl = open(os.path.join(HERE, "comp.tpl.html"), encoding="utf-8").read()
    caps = [{"a": c[0], "b": c[1], "ar": c[3] if c[2] else "", "en": c[4], "zh": c[5]} for c in CAPS]
    open(os.path.join(HERE, "comp.html"), "w", encoding="utf-8").write(tpl.replace("__CAPS__", json.dumps(caps, ensure_ascii=False)))
    print("wrote comp.html")


if __name__ == "__main__":
    write_srt()
    if "--no-font" not in sys.argv:
        fetch_font()
    build_html()
