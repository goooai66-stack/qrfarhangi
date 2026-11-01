C = dict(dir="/home/user/qrfarhangi/video/ali-khaybar-eye", scenes="/home/user/qrfarhangi/video/ali-khaybar-eye/scenes.js",
 T=dict(ink="#3a2a20", fill="#f7ebd2", gold="#e2a93b", gold2="#b57a12", red="#c8553a", green="#4f8a78", blue="#3d6f8e", violet="#7a5c8a", book="#4f8a78", bookText="#f7ebd2", pink="#c8553a", cyan="#3d6f8e"),
 bg="radial-gradient(ellipse at 50% 45%, rgba(0,0,0,0) 60%, rgba(90,50,20,.22) 100%), #f1e4c8", low="linear-gradient(180deg, #b5472b 0%, #8a3320 100%)",
 capAr="color: #fbf0da; text-shadow: none;", capZh="color: #ffd98a; direction: ltr; text-shadow: none;", capEn="color: #f0d2c4; direction: ltr; text-shadow: none;",
 patTop="#3a2a20", patBot="#ffffff", patTopOp=.0, lamp="#3a2a20", nameColor="#3a2a20", nameShadow="text-shadow: 5px 5px 0 #e2a93b", orbBg="#e2a93b",
 css=""".chip { background:#f7ebd2; border:none; color:#3a2a20; border-radius:16px; box-shadow:7px 7px 0 rgba(58,42,32,.3); }
.chip.y { background:#e2a93b; } .chip.c { background:#c8553a; color:#fbf0da; } .chip.m { background:#8fbfae; } .chip.b { background:#8fb2c9; }
.bub { background:#f7ebd2; border:none; color:#3a2a20; border-radius:46px; box-shadow:8px 8px 0 rgba(58,42,32,.3); } .bub::after { border-top-color:#f7ebd2; }
svg.a, .a svg { filter: drop-shadow(4px 5px 0 rgba(58,42,32,.28)); }""",
 fx='for (const d of RAIN) { const y = 980 - ((d.y0 + d.v * 0.12 * t) % 1000), x = d.x * 0.9 + Math.sin(t * .3 + d.y0) * 10; fb.globalAlpha = d.a * 1.2; fb.fillStyle = "#3a2a20"; fb.beginPath(); fb.arc(x, y, 1.3 + d.l / 55, 0, 7); fb.fill(); }')
