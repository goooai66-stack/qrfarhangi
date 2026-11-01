C = dict(dir="/home/user/qrfarhangi/video/ruqyah-mizan", scenes="/home/user/qrfarhangi/video/ruqyah-mizan/scenes.js",
 T=dict(ink="#5a1f37", fill="#fff6ef", gold="#f2b134", gold2="#d98e04", red="#d6455d", green="#1f9d84", blue="#3b7fb6", violet="#8a63c9", book="#7a2848", bookText="#fff6ef", pink="#d6455d", cyan="#3b7fb6"),
 bg="radial-gradient(ellipse at 50% 30%, #ffd9d2 0%, #f7b8b4 55%, #e48f98 100%)", low="linear-gradient(180deg, #5a1f37 0%, #2e0f1e 100%)",
 capAr="color: #fff6ef; text-shadow: none;", capZh="color: #ffcf6b; direction: ltr; text-shadow: none;", capEn="color: #f0d3d8; direction: ltr; text-shadow: none;",
 patTop="#7a2848", patBot="#ffffff", patTopOp=.07, lamp="#d98e04", nameColor="#5a1f37", nameShadow="text-shadow: 0 6px 0 rgba(242,177,52,.6)", orbBg="#fff6ef",
 css=""".chip { background:#fff6ef; border:5px solid #5a1f37; color:#5a1f37; box-shadow:0 9px 0 rgba(90,31,55,.22); }
.chip.y { background:#ffe7a8; border-color:#b87800; color:#5a1f37; } .chip.c { background:#ffd1d6; border-color:#d6455d; color:#8e1f35; } .chip.m { background:#cdeedd; border-color:#1f9d84; color:#0f5547; } .chip.b { background:#d9e8ff; border-color:#3b7fb6; color:#1d4a73; }
.bub { background:#fff6ef; border-color:#5a1f37; color:#5a1f37; box-shadow:0 12px 0 rgba(90,31,55,.22); } .bub::after { border-top-color:#5a1f37; }""",
 fx='for (const d of RAIN) { const y = 980 - ((d.y0 + d.v * 0.2 * t) % 1000), x = d.x * 0.9 + Math.sin(t * .5 + d.y0) * 20; fb.globalAlpha = d.a * 2; fb.fillStyle = "#fff6ef"; fb.beginPath(); fb.arc(x, y, 2 + d.l / 28, 0, 7); fb.fill(); }')
