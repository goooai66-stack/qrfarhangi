C = dict(dir="/home/user/qrfarhangi/video/ruqyah-adab-vox", scenes="/home/user/qrfarhangi/video/ruqyah-adab-vox/scenes.js",
 T=dict(ink="#241a10", fill="#f3ece0", gold="#e5b14a", gold2="#b9852a", red="#c8372d", green="#5d8a54", blue="#3d6f9c", violet="#6a5a8e", book="#3a2a1a", bookText="#f3ece0", pink="#c8372d", cyan="#3d6f9c"),
 bg="radial-gradient(ellipse at 50% 45%, rgba(0,0,0,0) 55%, rgba(70,40,10,.45) 100%), radial-gradient(ellipse at 28% 18%, rgba(255,255,255,.4), rgba(255,255,255,0) 45%), radial-gradient(ellipse at 82% 80%, rgba(120,80,30,.28), rgba(120,80,30,0) 50%), linear-gradient(90deg, rgba(0,0,0,0) 49.6%, rgba(80,50,20,.2) 50%, rgba(0,0,0,0) 50.4%), linear-gradient(0deg, rgba(0,0,0,0) 49.7%, rgba(80,50,20,.18) 50%, rgba(0,0,0,0) 50.3%), #e6d7b4",
 low="linear-gradient(180deg, #2a1d12 0%, #140d08 100%)",
 capAr="color: #f6ecd6; text-shadow: none;", capZh="color: #e8b24a; direction: ltr; text-shadow: none;", capEn="color: #cdbf9f; direction: ltr; text-shadow: none;",
 patTop="#5a3d1a", patBot="#ffffff", patTopOp=.0, lamp="#241a10", nameColor="#241a10", nameShadow="text-shadow: 4px 4px 0 #e5b14a", orbBg="#e5b14a",
 css="""div.a:has(> .chip) { filter: drop-shadow(3px 6px 5px rgba(40,20,0,.45)); }
.bub { background:#f3ece0; border:none; color:#241a10; clip-path: polygon(0 3%, 6% 0, 20% 2%, 40% 0, 60% 3%, 80% 0, 100% 2%, 99% 40%, 100% 70%, 98% 100%, 70% 98%, 40% 100%, 10% 98%, 0 100%, 1% 60%); box-shadow:none; } .bub::after { display:none; }
.a svg, svg.a { filter: drop-shadow(3px 5px 4px rgba(40,20,0,.4)); }""",
 fx='for (const d of RAIN) { const y = 980 - ((d.y0 + d.v * 0.1 * t) % 1000), x = d.x * 0.9 + Math.sin(t * .3 + d.y0) * 10; fb.globalAlpha = d.a * 1.2; fb.fillStyle = "#5a3d1a"; fb.beginPath(); fb.arc(x, y, 1.2 + d.l / 60, 0, 7); fb.fill(); }')
