function haloEl(p, label, size = 210, fs = 42) { const s = box(size, size, "-105 -105 210 210", p); mk("circle", { r: 84, fill: T.fill, stroke: T.red, "stroke-width": 8, "stroke-dasharray": "16 11" }, s); const t = mk("text", { x: 0, y: fs / 3, "text-anchor": "middle", "font-family": "Cairo", "font-weight": 800, "font-size": fs, fill: T.ink }, s); t.textContent = label; return s; }
function chainEl(p) { const s = box(520, 130, "0 0 520 130", p); [60, 170, 280, 390].forEach((x, i) => mk("rect", { x: x - 55, y: 32, width: 110, height: 66, rx: 33, fill: "none", stroke: T.ink, "stroke-width": 12, transform: i % 2 ? "" : "" }, s)); return s; }
function dayEl(p, n) { const s = box(190, 220, "0 0 190 220", p); mk("rect", { x: 10, y: 20, width: 170, height: 190, rx: 20, fill: T.fill, stroke: T.ink, "stroke-width": 8 }, s); mk("rect", { x: 10, y: 20, width: 170, height: 52, rx: 20, fill: T.red, stroke: T.ink, "stroke-width": 8 }, s); const t = mk("text", { x: 95, y: 160, "text-anchor": "middle", "font-family": "Amiri", "font-weight": 700, "font-size": 96, fill: T.ink }, s); t.textContent = n; return s; }
const Y1 = spread("قصة الرجل الذي قرأ الفاتحة ثلاثة أيام", 0.31, 3.26), Y2 = spread("مر عم خارجة بن الصلت بقوم عندهم رجل مريض مقيد بالحديد", 4.0, 8.23), Y4 = spread("فقرأ عليه سورة الفاتحة", 11.42, 13.15), Y7 = spread("يجمع بزاقه ويتفل", 15.74, 17.55);
const Y8 = spread("فكأنما نشط من عقال", 18.01, 19.65), Y9 = spread("وأعطاه القوم جعلا من الغنم", 20.02, 21.73), Y10 = spread("فأتى النبي صلى الله عليه وسلم وأخبره", 22.27, 24.51), Y13 = spread("فلعمري لمن أكل برقية باطل", 27.72, 29.75), Y14 = spread("لقد أكلت برقية حق", 30.0, 31.49);
const Y16 = spread("سورة الفاتحة التي تقرؤها كل يوم في صلاتك", 32.8, 35.9), Y17 = spread("هي نفسها الرقية التي أقرها النبي صلى الله عليه وسلم", 36.19, 39.69), Y18 = spread("شارك هذه القصة مع من تحب", 40.26, 41.7), tFol = 41.95;
A("low", { x: 540, y: 1440, o: 1 }); A("pat2", { x: 540, y: 1440, o: .04 }); A("band", { x: 540, y: 967, o: 1 });
A("orb", { x: 880, y: 250, s: 1, o: .9 });
// SA
SC("SA", 0.25, 3.5); { const S = $("SA"), ms = mushEl(S, 330), fl = chipEl(S, "الفاتحة", "y", 66), d3 = chipEl(S, "٣ أيام", "c", 70);
  SS(ms, Y1[4][1], 3.3, .2, { x: 540, y: 420 }); SS(fl, Y1[4][1] + 0.1, 3.3, .2, { x: 540, y: 600 }); SS(d3, Y1[6][1], 3.3, .2, { x: 540, y: 820 }); BURSTS.push({ t: Y1[6][1] + 0.3, x: 540, y: 820 }); }
// SB
SC("SB", 3.95, 9.4); { const S = $("SB"), u = chipEl(S, "عمّ خارجة بن الصلت", "b", 50), ar = arrowEl(S, 640, 330, 460, 330), hs = [790, 540, 290].map(() => haloEl(S, "", 140)), sk = haloEl(S, "مريض", 230, 52), ch = chainEl(S);
  SS(u, Y2[2][1], 9.2, .2, { x: 790, y: 330 }); D(ar, inc(Y2[4][1], Y2[5][1])); A(ar.parentNode, { x: 540, y: 960, o: seg(Y2[4][1], 9.2, .2) }); hs.forEach((h, i) => SS(h, Y2[5][1] + i * 0.1, 9.2, .2, { x: 290 + i * 0, y: 330 })); 
  SS(sk, Y2[8][1], 9.2, .2, { x: 540, y: 640 }); SS(ch, Y2[10][1], 9.2, .2, { x: 540, y: 800 }); BURSTS.push({ t: Y2[10][1] + 0.3, x: 540, y: 800 }); }
// SC
SC("SC", 9.5, 11.2); { const S = $("SC"), b = bubbleEl(S, "هل عندك ما تداويه به؟", 70); SS(b, 9.6, 11.0, .2, { x: 540, y: 560 }); BURSTS.push({ t: 9.8, x: 540, y: 560 }); }
// SD
SC("SD", 11.35, 17.7); { const S = $("SD"), ms = mushEl(S, 300), fl = chipEl(S, "الفاتحة", "y", 62), ds = [1, 2, 3].map((n) => dayEl(S, "٣٢١"[3 - n])), sm = chipEl(S, "صباحًا ومساءً", "m", 52), sp = chipEl(S, "يتفل", "b", 62);
  SS(ms, Y4[3][1], 17.5, .2, { x: 540, y: 330 }); SS(fl, Y4[3][1] + 0.1, 17.5, .2, { x: 540, y: 500 }); ds.forEach((d, i) => SS(d, 13.28 + i * 0.25, 17.5, .2, { x: 790 - i * 250, y: 700 })); SS(sm, 14.35, 17.5, .2, { x: 540, y: 880 }); SS(sp, Y7[2][1], 17.5, .2, { x: 900, y: 330 }); BURSTS.push({ t: Y7[2][1] + 0.3, x: 900, y: 330 }); }
// SE
SC("SE", 17.95, 22.1); { const S = $("SE"), sk = haloEl(S, "مريض", 230, 52), ch = chainEl(S), [ts, tt] = tickEl(S, 200), jl = chipEl(S, "جُعل من الغنم", "y", 56);
  SS(sk, 18.0, 21.9, .2, { x: 540, y: 520 }); SS(ch, 18.0, 21.9, .2, { x: 540, y: 740 }); X(S, 540, 740, Y8[1][1], 21.9, 420); TICK(S, 540, 520, Y8[3][1], 21.9, 190); SS(jl, Y9[3][1], 21.9, .2, { x: 540, y: 900 }); }
// SF
SC("SF", 22.2, 27.5); { const S = $("SF"), a = chipEl(S, "الرجل", "m", 62), ar = arrowEl(S, 640, 400, 460, 400), sl = sealEl(S), b = bubbleEl(S, "كُلْ", 100);
  SS(a, Y10[0][1], 27.2, .2, { x: 790, y: 400 }); SS(sl, Y10[1][1], 27.2, .2, { x: 290, y: 400 }); D(ar, inc(Y10[0][1], Y10[1][1] + 0.2)); A(ar.parentNode, { x: 540, y: 960, o: seg(Y10[0][1], 27.2, .2) }); SS(b, 27.16, 27.5, .2, { x: 540, y: 760 }); BURSTS.push({ t: 27.3, x: 540, y: 760 }); }
// SG
SC("SG", 27.65, 31.6); { const S = $("SG"), a = chipEl(S, "رقية باطل", "c", 62), b = chipEl(S, "رقية حقّ", "m", 62);
  SS(a, Y13[4][1], 31.4, .2, { x: 790, y: 460 }); X(S, 790, 660, Y13[4][1], 31.4, 220); SS(b, Y14[3][1], 31.4, .2, { x: 290, y: 460 }); TICK(S, 290, 660, Y14[3][1], 31.4, 190); }
// SH
SC("SH", 31.95, 39.8); { const S = $("SH"), t = chipEl(S, "تأمّل", "y", 70), ms = mushEl(S, 300), fl = chipEl(S, "الفاتحة", "m", 56), pr = chipEl(S, "في صلاتك", "b", 56), eq = textEl(S, "=", 150, T.ink), rq = chipEl(S, "رقية أقرّها النبي", "y", 52), sl = sealEl(S);
  SS(t, 32.0, 32.5, .2, { x: 540, y: 330 }); SS(ms, Y16[1][1], 39.6, .2, { x: 540, y: 330 }); SS(fl, Y16[1][1] + 0.1, 39.6, .2, { x: 540, y: 500 }); SS(pr, Y16[7][1], 39.6, .2, { x: 790, y: 700 }); SS(eq, Y17[1][1], 39.6, .2, { x: 540, y: 700 }); SS(rq, Y17[4][1], 39.6, .2, { x: 290, y: 700 }); SS(sl, Y17[5][1], 39.6, .2, { x: 290, y: 880, s: [[Y17[5][1], .5], [Y17[5][1] + 0.4, .55, "pop"]] }); BURSTS.push({ t: Y17[4][1] + 0.3, x: 290, y: 700 }); }
SC("SL", 39.95, 80);
A("lamp", { x: 540, y: 330, s: [[40.1, .78], [40.8, .66, "out"]], o: [[40.0, 0], [40.4, 1]] }); A("name", { x: 540, y: 600, s: [[40.2, 1.1], [41.0, 1, "out"]], o: [[40.2, 0], [40.6, 1]] });
D("sh1", inc(Y18[0][1], Y18[0][1] + 0.45)); D("sh2", inc(Y18[0][1] + 0.3, Y18[0][1] + 0.7)); D("sh3", inc(Y18[0][1] + 0.6, Y18[0][1] + 0.85));
A("share", { x: 380, y: 830, s: [[Y18[0][1] + 0.49, .6], [Y18[0][1] + 1.0, 1, "back"]], o: [[Y18[0][1] + 0.49, 0], [Y18[0][1] + 0.5, 1]] });
A("bell", { x: 700, y: 830, s: [[tFol - 0.01, .6], [tFol + .5, 1, "back"]], r: [[tFol + 0.6, 0], [tFol + 0.7, 14, "out"], [tFol + 0.85, -12, "io"], [tFol + 1.0, 8, "io"], [tFol + 1.15, 0, "io"]], o: [[tFol - 0.01, 0], [tFol, 1]] }); D("bl1", inc(tFol, tFol + 0.6)); D("bl2", inc(tFol + 0.5, tFol + 0.8));
