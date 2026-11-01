// render frames [from, to) of comp.html to JPEGs
const { chromium } = require('playwright');
const [,, html, out, from, to, fps] = process.argv;
(async () => {
  const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', e => console.error('PAGEERROR', e.message));
  await p.goto('file://' + html); await p.evaluate(() => window.ready);
  for (let f = +from; f < +to; f++) {
    await p.evaluate(t => render(t), f / +fps);
    await p.screenshot({ path: `${out}/f${String(f).padStart(5, '0')}.jpg`, type: 'jpeg', quality: 93 });
  }
  await b.close();
})();
