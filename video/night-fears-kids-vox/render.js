// render frames [from,to) of comp.html and pipe them straight into an x264 segment file (no frames on disk)
const { chromium } = require('playwright'); const { spawn } = require('child_process');
const [,, html, outFile, from, to, fps] = process.argv;
(async () => {
  const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', fps, '-c:v', 'mjpeg', '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-pix_fmt', 'yuv420p', '-r', fps, outFile], { stdio: ['pipe', 'inherit', 'inherit'] });
  const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  p.on('pageerror', e => console.error('PAGEERROR', e.message));
  await p.goto('file://' + html); await p.evaluate(() => window.ready);
  for (let f = +from; f < +to; f++) {
    await p.evaluate(t => render(t), f / +fps);
    const buf = await p.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close();
})();
