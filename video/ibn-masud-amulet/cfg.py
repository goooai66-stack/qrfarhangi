C = dict(dir="/home/user/qrfarhangi/video/ibn-masud-amulet", scenes="/home/user/qrfarhangi/video/ibn-masud-amulet/scenes.js",
 T=dict(ink="#35e0ff", fill="#0e1233", gold="#ffd23f", gold2="#ffd23f", red="#ff4d8d", green="#39ffb0", blue="#35e0ff", violet="#8d7bff", book="#10163f", bookText="#e8fbff", pink="#ff4d8d", cyan="#35e0ff"),
 bg="radial-gradient(ellipse at 50% 30%, #1d2270 0%, #0c1038 55%, #02030f 100%)", low="linear-gradient(180deg, #0d1130 0%, #02030f 100%)",
 capAr="color: #ffffff; text-shadow: 0 0 14px rgba(53,224,255,.55);", capZh="color: #ffd23f; direction: ltr; text-shadow: 0 0 12px rgba(255,210,63,.4);", capEn="color: #b9c4ff; direction: ltr; text-shadow: none;",
 patTop="#35e0ff", patBot="#ffffff", patTopOp=.08, lamp="#35e0ff", nameColor="#ffffff", nameShadow="text-shadow: 0 0 24px rgba(53,224,255,.8)", orbBg="rgba(141,123,255,.55)",
 css=""".chip { background:#0e1233; border:5px solid #35e0ff; color:#e8fbff; box-shadow:0 0 24px rgba(53,224,255,.55), inset 0 0 14px rgba(53,224,255,.25); }
.chip.y { border-color:#ffd23f; color:#ffd23f; box-shadow:0 0 24px rgba(255,210,63,.5), inset 0 0 14px rgba(255,210,63,.2); } .chip.c { border-color:#ff4d8d; color:#ff8fb4; box-shadow:0 0 24px rgba(255,77,141,.55), inset 0 0 14px rgba(255,77,141,.2); }
.chip.m { border-color:#39ffb0; color:#8dffd0; box-shadow:0 0 24px rgba(57,255,176,.5), inset 0 0 14px rgba(57,255,176,.2); } .chip.b { border-color:#8d7bff; color:#c9c0ff; box-shadow:0 0 24px rgba(141,123,255,.55), inset 0 0 14px rgba(141,123,255,.2); }
.bub { background:#0e1233; border-color:#35e0ff; color:#e8fbff; box-shadow:0 0 28px rgba(53,224,255,.5); } .bub::after { border-top-color:#35e0ff; }
.a svg, svg.a { filter: drop-shadow(0 0 7px rgba(53,224,255,.55)); }""",
 fx='for (const d of RAIN) { const y = 980 - ((d.y0 + d.v * 0.25 * t) % 1000), x = d.x * 0.9 + Math.sin(t * .5 + d.y0) * 20; fb.globalAlpha = d.a * 2.4; fb.fillStyle = d.l > 70 ? "#ff4d8d" : "#35e0ff"; fb.beginPath(); fb.arc(x, y, 2 + d.l / 30, 0, 7); fb.fill(); }')
