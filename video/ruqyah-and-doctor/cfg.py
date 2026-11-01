C = dict(dir="/home/user/qrfarhangi/video/ruqyah-and-doctor", scenes="/home/user/qrfarhangi/video/ruqyah-and-doctor/scenes.js",
 T=dict(ink="#14163a", fill="#ffffff", gold="#ffc83d", gold2="#14163a", red="#ff6b5a", green="#0e9f94", blue="#2b6fd8", violet="#7a5af8", book="#14163a", bookText="#ffffff", pink="#ff6b5a", cyan="#2b6fd8"),
 bg="#ff6b5a", low="linear-gradient(180deg, #14163a 0%, #0a0b22 100%)",
 capAr="color: #ffffff; text-shadow: none;", capZh="color: #ffc83d; direction: ltr; text-shadow: none;", capEn="color: #c3c6ee; direction: ltr; text-shadow: none;",
 patTop="#ffffff", patBot="#ffffff", patTopOp=.08, lamp="#ffffff", nameColor="#14163a", nameShadow="text-shadow: 6px 6px 0 #ffffff", orbBg="rgba(0,0,0,0)",
 css=""".chip { background:#ffffff; border:5px solid #14163a; color:#14163a; border-radius:999px; box-shadow:7px 7px 0 #14163a; }
.chip.y { background:#ffc83d; } .chip.c { background:#ff6b5a; color:#fff; } .chip.m { background:#7fe3c3; } .chip.b { background:#bcd8ff; }
.bub { background:#ffffff; border-color:#14163a; color:#14163a; box-shadow:8px 8px 0 #14163a; } .bub::after { border-top-color:#14163a; }""",
 fx='for (const d of RAIN) { const y = 980 - ((d.y0 + d.v * 0.2 * t) % 1000), x = d.x * 0.9 + Math.sin(t * .5 + d.y0) * 20; fb.globalAlpha = d.a * 1.6; fb.fillStyle = "#ffffff"; fb.beginPath(); fb.arc(x, y, 2.5 + d.l / 28, 0, 7); fb.fill(); }')
