C = dict(dir="/home/user/qrfarhangi/video/asma-bint-umays", scenes="/home/user/qrfarhangi/video/asma-bint-umays/scenes.js",
 T=dict(ink="#3d2a6b", fill="#fffaf5", gold="#ffb870", gold2="#e08a2e", red="#ef6f8b", green="#2fa58a", blue="#6a8fe8", violet="#8d6ad8", book="#6a4cb8", bookText="#fffaf5", pink="#ef6f8b", cyan="#6a8fe8"),
 bg="radial-gradient(ellipse at 50% 30%, #f1e7ff 0%, #d4c1f5 55%, #a98bdc 100%)", low="linear-gradient(180deg, #fdebe0 0%, #f6d3c2 100%)",
 capAr="color: #3d2a6b; text-shadow: none;", capZh="color: #b4451f; direction: ltr; text-shadow: none;", capEn="color: #5b4a7a; direction: ltr; text-shadow: none;",
 patTop="#ffffff", patBot="#3d2a6b", patTopOp=.12, lamp="#ffb870", nameColor="#3d2a6b", nameShadow="text-shadow: 0 6px 0 rgba(255,184,112,.7)", orbBg="#ffd9b3",
 css=""".chip { background:#fffaf5; border:5px solid #3d2a6b; color:#3d2a6b; box-shadow:0 9px 0 rgba(61,42,107,.25); border-radius:36px; }
.chip.y { background:#ffe3c2; border-color:#e08a2e; } .chip.c { background:#ffd3de; border-color:#ef6f8b; color:#8e2a45; } .chip.m { background:#c9f0e3; border-color:#2fa58a; } .chip.b { background:#dbe5ff; border-color:#6a8fe8; }
.bub { background:#fffaf5; border-color:#3d2a6b; color:#3d2a6b; box-shadow:0 12px 0 rgba(61,42,107,.25); border-radius:50px; } .bub::after { border-top-color:#3d2a6b; }""",
 fx='for (const d of RAIN) { const y = 980 - ((d.y0 + d.v * 0.2 * t) % 1000), x = d.x * 0.9 + Math.sin(t * .6 + d.y0) * 24; fb.globalAlpha = d.a * 2.2; fb.fillStyle = d.l > 70 ? "#ffd9b3" : "#ffffff"; fb.beginPath(); fb.arc(x, y, 3 + d.l / 22, 0, 7); fb.fill(); }')
