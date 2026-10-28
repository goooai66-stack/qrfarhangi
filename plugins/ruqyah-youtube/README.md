# ruqyah-youtube

پلاگین Claude Code که همه‌ی اسکیل‌های یوتیوب کانال رقیه شرعیه را یک‌جا دارد. همه‌ی اسکیل‌ها خروجی را
به فارسی می‌نویسند و خطوط قرمز [`youtube/niche.md`](youtube/niche.md) را رعایت می‌کنند: بدون وعده‌ی
شفای قطعی، بدون جایگزین کردن پزشک، بدون تشخیص از راه دور، بدون ترساندن، و بدون نوشتن آیه یا حدیث
از حافظه.

## نصب

در Claude Code:

```
/plugin marketplace add goooai66-stack/qrfarhangi
/plugin install ruqyah-youtube@qrfarhangi
```

اگر ریپو خصوصی است، دسترسی git به آن لازم است.

## پروفایل کانال

- `youtube/niche.md`: حوزه، قالب‌ها، جستجوهای مخاطب و خطوط قرمز
- `youtube/voice.md`: لحن شما. قالب خالی است و باید پر شود.

اسکیل‌ها اول `.claude/youtube/niche.md` و `.claude/youtube/voice.md` را در پروژه‌ی فعلی
می‌خوانند و اگر نبود، از نسخه‌ی داخل همین پلاگین استفاده می‌کنند. برای پروفایل اختصاصی هر پروژه،
این دو فایل را در `.claude/youtube/` همان پروژه کپی کنید.

## اسکیل‌ها (۱۵ تا)

| اسکیل | کار |
| --- | --- |
| `yt-script` | اسکریپت از یک ایده، با ۵ هوک امتیازدار (`hookscore.py` فارسی را می‌فهمد) |
| `yt-package` | عنوان و تامبنیل به‌عنوان یک جفت (`title.py`) |
| `yt-seo` | توضیحات، تگ و سه جستجویی که ویدیو باید ببرد |
| `yt-chapters` | چپتر از ترنسکریپت، مطابق قوانین یوتیوب |
| `yt-edit` | فهرست برش: سکوت، تکرار و برداشت‌های اضافه |
| `yt-shorts` | شورتس‌های پنهان در ویدیوی بلند |
| `yt-retention` | تحلیل خروجی ریتنشن YouTube Studio |
| `yt-comment` | دسته‌بندی کامنت‌ها و پاسخ با لحن شما |
| `yt-plan` | برنامه‌ی هفتگی متناسب با وقت واقعی شما |
| `yt-viral` | ویدیوهای موفق حوزه، رتبه‌بندی‌شده نسبت به میانه‌ی کانال خودشان |
| `yt-audit` | بررسی کل کانال و یک اصلاح اولویت‌دار |
| `youtube` | ۱۴ زیردستور: `audit`، `seo`، `script`، `hook`، `thumbnail`، `strategy`، `calendar`، `shorts`، `analyze`، `repurpose`، `monetize`، `competitor`، `metadata`، `ideate` |
| `youtube-seo` | سئوی یوتیوب و گوگل |
| `youtube-own-channel-analyzer` | تحلیل کانال خودتان با YouTube Data API |
| `youtube-competitor-analyzer` | پیدا کردن و مقایسه‌ی رقبا با YouTube Data API |

دو اسکیل آخر و اسکریپت‌های `youtube` کلید را از متغیر محیطی `YOUTUBE_API_KEY` می‌خوانند. کلید را در
هیچ فایلی از ریپو ذخیره نکنید.

## منابع و مجوزها

همه با مجوز MIT، با تغییراتی برای زبان فارسی و حوزه‌ی رقیه:

- `yt-*`: [Jakeschincariol/youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) (`licenses/youtube-agent-skill-LICENSE`)
- `youtube`: [AgriciDaniel/claude-youtube](https://github.com/AgriciDaniel/claude-youtube)
- `youtube-seo`: [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills)
- `youtube-own-channel-analyzer`، `youtube-competitor-analyzer`: [nikhilbhansali/claude-youtube-skills](https://github.com/nikhilbhansali/claude-youtube-skills)
