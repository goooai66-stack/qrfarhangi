# qrfarhangi

صفحهٔ نمایش اطلاعات حساب بانکی (`index.html`) که به **Google Apps Script** وصل است و به‌صورت Web App منتشر می‌شود.

## فایل‌ها

| فایل | کاربرد |
|---|---|
| `index.html` | صفحهٔ اصلی |
| `Code.js` | کد Apps Script؛ تابع `doGet` صفحه را نمایش می‌دهد |
| `appsscript.json` | تنظیمات پروژهٔ Apps Script (منطقهٔ زمانی تهران، دسترسی عمومی Web App) |
| `.claspignore` | فقط سه فایل بالا به گوگل فرستاده می‌شوند |
| `.clasp.json.example` | نمونهٔ تنظیم اتصال به اسکریپت شما |

## راه‌اندازی در ویندوز (پوشهٔ `D:\cluad`)

پیش‌نیاز: [Node.js](https://nodejs.org) و Git نصب باشد. سپس در PowerShell:

```powershell
cd D:\cluad
git clone https://github.com/goooai66-stack/qrfarhangi.git
cd qrfarhangi
npm install -g @google/clasp
clasp login
```

یک بار Apps Script API را روشن کنید: https://script.google.com/home/usersettings

### حالت ۱ — ساخت اسکریپت جدید

```powershell
clasp create --type webapp --title "qrfarhangi" --rootDir .
clasp push
```

### حالت ۲ — اتصال به اسکریپتی که از قبل دارید

`.clasp.json.example` را به `.clasp.json` کپی کنید و `scriptId` را بگذارید
(در ویرایشگر Apps Script: Project Settings ← Script ID)، بعد:

```powershell
clasp push
```

### انتشار Web App

```powershell
clasp deploy --description "v1"
```

یا از ویرایشگر: **Deploy ← New deployment ← Web app**، گزینهٔ Execute as: *Me* و Who has access: *Anyone*.
آدرس `https://script.google.com/macros/s/.../exec` را می‌توانید برای QR استفاده کنید.

هر بار که `index.html` را تغییر دادید: `clasp push` و سپس `clasp deploy -i <DEPLOYMENT_ID>` تا همان آدرس به‌روز شود.
