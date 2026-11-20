const { chromium } = require('playwright');
const [,, html, out, ...ts] = process.argv;
(async () => { const b = await chromium.launch({ args: ['--allow-file-access-from-files'] }); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  p.on('pageerror', e => console.error('PAGEERROR', e.message)); p.on('console', m => { if (m.type() === 'error') console.error('CONSOLE', m.text()); });
  await p.goto('file://' + html); await p.evaluate(() => window.ready);
  for (const t of ts) { await p.evaluate(t => render(t), +t); await p.screenshot({ path: `${out}/s_${t}.png` }); }
  await b.close(); })();
