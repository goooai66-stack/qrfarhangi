C = dict(dir="/home/user/qrfarhangi/video/ruqyah-adab-patient", scenes="/home/user/qrfarhangi/video/ruqyah-adab-patient/scenes.js",
 T=dict(ink="#f4efe0", fill="rgba(0,0,0,0)", gold="#d8aa4c", gold2="#d8aa4c", red="#e08a6a", green="#8fcf9c", blue="#9ec5d8", violet="#b9a6e0", book="#0b1f18", bookText="#d8aa4c", pink="#e08a6a", cyan="#9ec5d8"),
 bg="radial-gradient(ellipse at 50% 20%, #0f3a2c 0%, #082219 55%, #050f0c 100%)", low="linear-gradient(180deg, #050f0c 0%, #030a08 100%)",
 capAr="color: #f4efe0; text-shadow: none;", capZh="color: #d8aa4c; direction: ltr; text-shadow: none;", capEn="color: #b9c4bd; direction: ltr; text-shadow: none;",
 patTop="#d8aa4c", patBot="#ffffff", patTopOp=.05, lamp="#d8aa4c", nameColor="#d8aa4c", nameShadow="text-shadow: 0 0 36px rgba(216,170,76,.45)", orbBg="rgba(0,0,0,0)",
 css=""".chip { background:rgba(8,34,25,.7); border:3px solid #d8aa4c; color:#f4efe0; border-radius:999px; box-shadow:none; padding:0 38px 8px; }
.chip.y { border-color:#d8aa4c; color:#d8aa4c; } .chip.c { border-color:#e08a6a; color:#f0b49c; } .chip.m { border-color:#8fcf9c; color:#b5e5bf; } .chip.b { border-color:#9ec5d8; color:#c4dde9; }
.chip.y, .chip.c, .chip.m, .chip.b { background: rgba(8,34,25,.7); }
.bub { background:#082219; border:3px solid #d8aa4c; color:#f4efe0; box-shadow:none; } .bub::after { border-top-color:#d8aa4c; }""",
 fx='for (const d of RAIN) { const y = 980 - ((d.y0 + d.v * 0.06 * t) % 1000), x = d.x * 0.9; fb.globalAlpha = d.a * (1.4 + Math.sin(t * 2 + d.y0)); fb.fillStyle = "#f4efe0"; fb.beginPath(); fb.arc(x, y, 1.2 + d.l / 70, 0, 7); fb.fill(); }')
