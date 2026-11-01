C = dict(dir="/home/user/qrfarhangi/video/umm-salama-nazra", scenes="/home/user/qrfarhangi/video/umm-salama-nazra/scenes.js",
 T=dict(ink="#10285e", fill="#ffffff", gold="#ffc82e", gold2="#e0a100", red="#ff5a3c", green="#14a37f", blue="#4aa3ff", violet="#7a5af8", book="#10285e", bookText="#ffffff", pink="#ff5a3c", cyan="#4aa3ff"),
 bg="radial-gradient(ellipse at 50% 30%, #3b6df0 0%, #1f4fd8 55%, #123aa8 100%)", low="linear-gradient(180deg, #f6f0e2 0%, #e4dac0 100%)",
 capAr="color: #10285e; text-shadow: none;", capZh="color: #b4400f; direction: ltr; text-shadow: none;", capEn="color: #3d4668; direction: ltr; text-shadow: none;",
 patTop="#ffffff", patBot="#10285e", patTopOp=.1, lamp="#ffc82e", nameColor="#ffffff", nameShadow="text-shadow: 0 8px 0 rgba(16,40,94,.55)", orbBg="#ffc82e",
 css=""".chip { background:#ffffff; border:5px solid #10285e; color:#10285e; box-shadow:8px 8px 0 #10285e; border-radius:18px; }
.chip.y { background:#ffc82e; } .chip.c { background:#ff5a3c; color:#fff; } .chip.m { background:#7fe3c3; } .chip.b { background:#bcd8ff; }
.bub { background:#ffffff; border-color:#10285e; color:#10285e; box-shadow:9px 9px 0 #10285e; } .bub::after { border-top-color:#10285e; }""",
 fx='for (const d of RAIN) { const y = 980 - ((d.y0 + d.v * 0.2 * t) % 1000), x = d.x * 0.9 + Math.sin(t * .5 + d.y0) * 20; fb.globalAlpha = d.a * 2; fb.fillStyle = "#ffffff"; fb.beginPath(); fb.arc(x, y, 3 + d.l / 25, 0, 7); fb.fill(); }')
