const { chromium } = require('playwright');
const [,, html, out, ...times] = process.argv;
(async () => {
  const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', e => console.error('PAGEERROR', e.message));
  p.on('console', m => { if (m.type() === 'error') console.error('CONSOLE', m.text()); });
  await p.goto('file://' + html); await p.evaluate(() => window.ready);
  for (const t of times) { await p.evaluate(t => render(+t), t); await p.screenshot({ path: `${out}/s_${t}.png` }); }
  await b.close();
})();
