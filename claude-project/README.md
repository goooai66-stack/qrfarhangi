# پروژه‌ی claude.ai برای کانال رقیه شرعیه

همه‌ی چیزهایی که برای ساختن یک Project در claude.ai لازم است. این فایل‌ها با
`python3 tools/build_claude_project.py` از پلاگین `plugins/ruqyah-youtube` ساخته می‌شوند. هر وقت
پلاگین تغییر کرد، همین دستور را دوباره اجرا کنید.

| فایل | کجا می‌رود |
| --- | --- |
| `instructions.md` | دستورالعمل پروژه (Project instructions) |
| `knowledge/niche.md`، `knowledge/voice.md` | دانش پروژه (Project knowledge) |
| `skills/*.zip` (۱۵ فایل) | اسکیل‌های حساب شما (Settings → Capabilities → Skills) |

## ۱. فعال کردن اسکیل‌ها (یک بار برای کل حساب)

1. در claude.ai به **Settings → Capabilities** بروید.
2. **Code execution and file creation** را روشن کنید. ابزارهای امتیاز هوک، بررسی عنوان، چپتر و
   ریتنشن بدون آن اجرا نمی‌شوند.
3. در بخش **Skills** گزینه‌ی **Upload skill** را بزنید و zipها را یکی‌یکی آپلود کنید.

اگر نمی‌خواهید همه را آپلود کنید، این پنج تا مهم‌ترند: `yt-script`، `yt-package`، `yt-seo`،
`youtube` و `yt-comment`.

## ۲. ساختن پروژه

1. در claude.ai به **Projects → Create project** بروید. نام پیشنهادی: «کانال رقیه شرعیه».
2. متن `instructions.md` را در **Project instructions** (دستورالعمل پروژه) کپی کنید.
3. `knowledge/niche.md` و `knowledge/voice.md` را به **Project knowledge** اضافه کنید.

## ۳. استفاده

داخل پروژه گفتگو را شروع کنید، مثلاً:

- «برای ویدیوی "تفاوت رقیه شرعیه با دعانویسی" اسکریپت بنویس»
- «برای این ویدیو عنوان و متن تامبنیل پیشنهاد بده»
- «این کامنت‌ها را جواب بده: ...»
- «برنامه‌ی هفته‌ی بعد را بچین؛ ۶ ساعت وقت دارم»

## به‌روزرسانی voice.md

`voice.md` هنوز قالب خالی است. پس از پر شدن، نسخه‌ی داخل Project knowledge را جایگزین کنید. اگر
اسکیل‌ها را آپلود کرده‌اید، zipها را هم دوباره بسازید و آپلود کنید، چون هر zip یک نسخه از
`voice.md` را با خودش دارد.
