function scaleEl(p, key) { const s = mk("svg", { width: 760, height: 620, viewBox: "0 0 760 620", class: "a" }, p), cx = 380, cy = 150, L = 270;
  mk("path", { d: `M${cx},${cy} V540`, stroke: T.ink, "stroke-width": 12, fill: "none", "stroke-linecap": "round" }, s); mk("path", { d: "M240,570 H520 L470,540 H290 Z", stroke: T.ink, "stroke-width": 9, fill: T.fill, "stroke-linejoin": "round" }, s);
  const beam = mk("line", { stroke: T.gold2, "stroke-width": 14, "stroke-linecap": "round" }, s); mk("circle", { cx, cy, r: 18, fill: T.fill, stroke: T.gold2, "stroke-width": 8 }, s);
  const pans = [0, 1].map(() => { const g = mk("g", {}, s); return { c1: mk("line", { stroke: T.ink, "stroke-width": 5 }, g), c2: mk("line", { stroke: T.ink, "stroke-width": 5 }, g), pan: mk("path", { fill: T.fill, stroke: T.ink, "stroke-width": 8, "stroke-linejoin": "round" }, g), g }; });
  CUST.push((t) => { const th = tw(t, key.th) * Math.PI / 180, vis = key.vis(t); const xr = cx + L * Math.cos(th), yr = cy + L * Math.sin(th), xl = cx - L * Math.cos(th), yl = cy - L * Math.sin(th);
    beam.setAttribute("x1", xl); beam.setAttribute("y1", yl); beam.setAttribute("x2", xr); beam.setAttribute("y2", yr);
    [[pans[0], xr, yr], [pans[1], xl, yl]].forEach(([P, sx, sy]) => { const dy = 150; P.c1.setAttribute("x1", sx); P.c1.setAttribute("y1", sy); P.c1.setAttribute("x2", sx - 100); P.c1.setAttribute("y2", sy + dy); P.c2.setAttribute("x1", sx); P.c2.setAttribute("y1", sy); P.c2.setAttribute("x2", sx + 100); P.c2.setAttribute("y2", sy + dy); P.pan.setAttribute("d", `M${sx - 110},${sy + dy} Q${sx},${sy + dy + 76} ${sx + 110},${sy + dy} Z`); }); }); return s; }
const P1 = spread("قال النبي صلى الله عليه وسلم", 0.28, 2.02), P4 = spread("كان الناس في الجاهلية يرقون بكلمات فيها شرك", 6.21, 9.0), P6 = spread("جاء آل عمرو بن حزم إلى النبي صلى الله عليه وسلم", 10.64, 13.61), P7 = spread("عندنا رقية نرقي بها من العقرب", 14.59, 16.89);
const P10 = spread("ما أرى بأسا", 20.52, 21.57), P11 = spread("من استطاع منكم أن ينفع أخاه فلينفعه", 21.84, 24.64), P14 = spread("لا بأس بالرقى ما لم يكن فيه شرك", 27.73, 30.03), P16 = spread("كل رقية لا شرك فيها ولا كلمات مجهولة", 32.08, 35.17), P18 = spread("وكل رقية فيها شرك أو طلاسم", 36.29, 38.41);
const P20 = spread("فاعرض ما تسمعه على القرآن والسنة", 40.04, 42.45), P21 = spread("ولا ترض بكلمات لا تفهمها", 42.56, 44.17), P22 = spread("شارك هذا المقطع مع من تحب", 44.7, 46.31), tFol = 46.59;
A("low", { x: 540, y: 1440, o: 1 }); A("pat2", { x: 540, y: 1440, o: .05 }); A("band", { x: 540, y: 967, o: 1 });
A("orb", { x: 880, y: 250, s: (t) => 1 + 0.04 * Math.sin(t * 1.4), o: .7 }); CUST.push((t) => { $("orb").style.boxShadow = `0 0 ${60 + 10 * Math.sin(t)}px 10px rgba(255,255,255,.35)`; });
// SA
SC("SA", 0.2, 4.35); { const S = $("SA"), sl = sealEl(S), b = bubbleEl(S, "اعرضوا عليَّ رُقاكم", 76);
  SS(sl, P1[1][1], 4.1, .2, { x: 540, y: 340 }); BURSTS.push({ t: P1[1][1] + 0.4, x: 540, y: 340 }); SS(b, 2.37, 4.1, .2, { x: 540, y: 700 }); BURSTS.push({ t: 2.6, x: 540, y: 700 }); }
// SB
SC("SB", 4.2, 9.25); { const S = $("SB"), q = textEl(S, "؟", 260, T.red), j = chipEl(S, "الجاهلية", "y", 66), w = bubbleEl(S, "كلمات فيها شرك", 66, T.red);
  SS(q, 4.3, 5.9, .2, { x: 540, y: 480 }); BURSTS.push({ t: 4.5, x: 540, y: 480 }); SS(j, P4[3][1], 9.0, .2, { x: 540, y: 330 }); SS(w, P4[5][1], 9.0, .2, { x: 540, y: 640 }); X(S, 540, 880, P4[7][1], 9.0, 170); }
// SC
SC("SC", 9.3, 17.25); { const S = $("SC"), md = moonEl(S), isl = chipEl(S, "الإسلام", "m", 60), fam = chipEl(S, "آل عمرو بن حزم", "b", 52), sl = sealEl(S), ar = arrowEl(S, 600, 640, 440, 640), sc = scrollEl(S, 190), rq = chipEl(S, "رقية العقرب", "y", 54);
  SS(md, 9.4, 10.35, .2, { x: 540, y: 400 }); SS(isl, 9.5, 10.35, .2, { x: 540, y: 600 }); SS(fam, P6[1][1], 17.0, .2, { x: 790, y: 330 }); SS(sl, P6[6][1], 17.0, .2, { x: 290, y: 330 }); D(ar, inc(P6[4][1], P6[6][1] + 0.2, "io")); A(ar.parentNode, { x: 540, y: 960 + 0, o: seg(P6[4][1], 17.0, .2) });
  SS(sc, P7[1][1], 17.0, .2, { x: 540, y: 780 }); SS(rq, P7[5][1], 17.0, .2, { x: 540, y: 960 - 80 }); BURSTS.push({ t: P7[5][1] + 0.3, x: 540, y: 880 }); }
// SD
SC("SD", 17.3, 21.75); { const S = $("SD"), fam = chipEl(S, "آل عمرو", "b", 56), sl = sealEl(S), sc = scrollEl(S, 190), tk = chipEl(S, "لا بأس", "m", 80);
  SS(fam, 17.4, 21.5, .2, { x: 790, y: 360 }); SS(sl, 17.4, 21.5, .2, { x: 290, y: 360 }); A(sc, { x: [[17.32, 790], [18.12, 340, "io"]], y: [[17.32, 660], [18.12, 660]], s: pop(17.32), o: seg(17.32, 21.5, .2) }); SS(tk, P10[2][1], 21.5, .2, { x: 540, y: 560 }); TICK(S, 540, 800, P10[2][1] + 0.2, 21.5, 190); }
// SE
SC("SE", 21.8, 25.7); { const S = $("SE"), a = chipEl(S, "أنت", "y", 66), b = chipEl(S, "أخوك", "m", 66), ar = arrowEl(S, 640, 480, 440, 480), n = chipEl(S, "ينفعه", "b", 60), m = chipEl(S, "رواه مسلم", "y", 56);
  SS(a, P11[1][1], 25.4, .2, { x: 790, y: 480 }); SS(b, P11[5][1], 25.4, .2, { x: 290, y: 480 }); D(ar, inc(P11[4][1], P11[5][1] + 0.3)); A(ar.parentNode, { x: 540, y: 960, o: seg(P11[4][1], 25.4, .2) }); SS(n, P11[6][1], 25.4, .2, { x: 540, y: 330 }); TICK(S, 540, 700, P11[6][1] + 0.3, 25.4, 190); SS(m, 25.0, 25.4, .2, { x: 540, y: 880 }); }
// SF
SC("SF", 26.2, 30.15); { const S = $("SF"), c = chipEl(S, "رواية أخرى", "y", 62), b = bubbleEl(S, "لا بأس بالرقى<br>ما لم يكن فيه شرك", 66);
  SS(c, 26.3, 30.0, .2, { x: 540, y: 330 }); SS(b, P14[0][1], 30.0, .2, { x: 540, y: 620 }); X(S, 540, 880, P14[7][1], 30.0, 150); }
// SG
SC("SG", 30.5, 36.1); { const S = $("SG"), sc = scaleEl(S, { th: [[30.5, 0], [P16[1][1], 0], [P16[1][1] + 0.6, 12, "io"], [36.0, 12]], vis: () => 1 }), a = chipEl(S, "لا شرك", "m", 56), b = chipEl(S, "لا كلمات مجهولة", "m", 50), d = chipEl(S, "الميزان", "y", 70), ok = chipEl(S, "مشروعة", "m", 72);
  A(sc, { x: 540, y: 690, s: pop(30.62), o: seg(30.62, 36.0, .2) }); SS(d, 30.9, 36.0, .2, { x: 540, y: 270 }); SS(a, P16[3][1], 36.0, .2, { x: 790, y: 480 }); SS(b, P16[6][1], 36.0, .2, { x: 270, y: 480 }); SS(ok, 35.2, 36.0, .2, { x: 540, y: 400 }); BURSTS.push({ t: 35.5, x: 540, y: 400 }); }
// SH
SC("SH", 36.2, 39.7); { const S = $("SH"), sc = scaleEl(S, { th: [[36.2, 0], [P18[3][1], 0], [P18[3][1] + 0.6, -12, "io"], [39.6, -12]], vis: () => 1 }), a = chipEl(S, "شرك", "c", 62), b = chipEl(S, "طلاسم", "c", 62), r = chipEl(S, "مردودة", "c", 76);
  A(sc, { x: 540, y: 690, s: pop(36.3), o: seg(36.3, 39.5, .2) }); SS(a, P18[3][1], 39.5, .2, { x: 790, y: 330 }); SS(b, P18[5][1], 39.5, .2, { x: 290, y: 330 }); A(r, { x: 540, y: 460, s: [[38.72, 1.7], [39.1, 1, "out"]], r: -5, o: seg(38.72, 39.5, .2) }); BURSTS.push({ t: 39.1, x: 540, y: 460 }); }
// SI
SC("SI", 39.95, 44.3); { const S = $("SI"), h = chipEl(S, "ما تسمعه", "y", 60), ar = arrowEl(S, 540, 420, 540, 560), q = chipEl(S, "القرآن", "m", 58), sn = chipEl(S, "السنة", "m", 58), ms = mushEl(S, 260), nu = chipEl(S, "كلمات لا تفهمها", "c", 52);
  SS(h, P20[2][1], 44.1, .2, { x: 540, y: 330 }); D(ar, inc(P20[3][1], P20[3][1] + 0.4, "io")); A(ar.parentNode, { x: 540, y: 960, o: seg(P20[3][1], 44.1, .2) }); SS(q, P20[4][1], 44.1, .2, { x: 790, y: 650 }); SS(sn, P20[5][1], 44.1, .2, { x: 290, y: 650 }); SS(ms, P20[4][1], 44.1, .2, { x: 540, y: 760 }); SS(nu, P21[2][1], 44.1, .2, { x: 540, y: 900 }); X(S, 540, 900, P21[4][1], 44.1, 150); }
SC("SL", 44.5, 80);
A("lamp", { x: 540, y: 330, s: [[44.7, .78], [45.4, .66, "out"]], o: [[44.6, 0], [45.0, 1]] }); A("name", { x: 540, y: 600, s: [[44.8, 1.1], [45.6, 1, "out"]], o: [[44.8, 0], [45.2, 1]] });
D("sh1", inc(P22[0][1], P22[0][1] + 0.45)); D("sh2", inc(P22[0][1] + 0.3, P22[0][1] + 0.7)); D("sh3", inc(P22[0][1] + 0.6, P22[0][1] + 0.85));
A("share", { x: 380, y: 830, s: [[P22[0][1] + 0.49, .6], [P22[0][1] + 1.0, 1, "back"]], o: [[P22[0][1] + 0.49, 0], [P22[0][1] + 0.5, 1]] });
A("bell", { x: 700, y: 830, s: [[tFol - 0.01, .6], [tFol + .5, 1, "back"]], r: [[tFol + 0.6, 0], [tFol + 0.7, 14, "out"], [tFol + 0.85, -12, "io"], [tFol + 1.0, 8, "io"], [tFol + 1.15, 0, "io"]], o: [[tFol - 0.01, 0], [tFol, 1]] }); D("bl1", inc(tFol, tFol + 0.6)); D("bl2", inc(tFol + 0.5, tFol + 0.8));
