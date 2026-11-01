function chipEl(parent, txt, cls = "", size = 54) { const d = document.createElement("div"); d.className = "a"; const s = document.createElement("span"); s.className = "chip " + cls; s.style.fontSize = size + "px"; s.style.fontFamily = "Amiri"; s.style.fontWeight = 700; s.textContent = txt; d.appendChild(s); parent.appendChild(d); return d; }
function flagEl(p, w = 240) { const s = box(w, w * 1.2, "0 0 200 240", p); mk("line", { x1: 40, y1: 14, x2: 40, y2: 230, stroke: T.ink, "stroke-width": 10, "stroke-linecap": "round" }, s); mk("path", { d: "M46,20 L180,50 L46,120 Z", fill: T.red, stroke: T.ink, "stroke-width": 6, "stroke-linejoin": "round" }, s); mk("circle", { cx: 100, cy: 62, r: 14, fill: T.gold }, s); return s; }
function dropEl(p, w = 100) { const s = box(w, w, "0 0 100 100", p); mk("path", { d: "M50,10 C30,38 18,52 18,66 C18,84 33,92 50,92 C67,92 82,84 82,66 C82,52 70,38 50,10 Z", fill: T.blue, stroke: T.ink, "stroke-width": 5, "stroke-linejoin": "round" }, s); return s; }
function sparkEl(p, w = 300) { const s = box(w, w, "0 0 200 200", p); mk("path", { d: "M100,10 L116,84 L190,100 L116,116 L100,190 L84,116 L10,100 L84,84 Z", fill: T.gold, stroke: T.ink, "stroke-width": 7, "stroke-linejoin": "round" }, s); return s; }
function heartEl(p, w = 150) { const s = box(w, w, "0 0 100 100", p); mk("path", { d: "M50,86 C10,56 14,22 36,20 C44,20 49,26 50,32 C51,26 56,20 64,20 C86,22 90,56 50,86 Z", fill: T.red, stroke: T.ink, "stroke-width": 5, "stroke-linejoin": "round" }, s); return s; }
// the collage backdrop: arch, circles, halftone
{ const mkS = (css, x, y) => { const d = document.createElement("div"); d.className = "a"; d.style.cssText = css; ACT.appendChild(d); A(d, { x, y, o: 1 }); return d; };
  mkS("width:560px; height:700px; border-radius:280px 280px 0 0; background:#4f8a78; opacity:.55", 170, 640);
  mkS("width:420px; height:420px; border-radius:50%; background:#c8553a; opacity:.5", 930, 760);
  mkS("width:420px; height:420px; border-radius:50%; background: radial-gradient(circle, #3a2a20 23%, transparent 25%) 0 0/24px 24px; opacity:.28; clip-path: circle(50%)", 930, 760);
  mkS("width:360px; height:180px; border-radius:180px 180px 0 0; background:#e2a93b; opacity:.6", 520, 960 - 90); }
const R2 = spread("لأعطين الراية غدا رجلا يفتح الله على يديه", 2.35, 5.73), R4 = spread("في غزوة خيبر قال النبي صلى الله عليه وسلم", 8.2, 10.78), R8 = spread("هو يشتكي عينيه", 14.49, 15.51), R9 = spread("فأرسلوا إليه فأتوا به", 16.2, 17.54), R10 = spread("فبصق النبي صلى الله عليه وسلم في عينيه ودعا له", 17.94, 20.88);
const R12 = spread("كأن لم يكن به وجع", 22.05, 23.24), R13 = spread("رواه البخاري ومسلم", 23.61, 24.76), R14 = spread("وهذا من معجزات النبي صلى الله عليه وسلم", 25.17, 28.16), R16 = spread("ولا يفعل مثلها مع المرضى", 29.96, 31.32), R18 = spread("أنه دعا لعلي وهو يتألم", 32.53, 34.73), R19 = spread("ولم يتركه مريضا", 35.05, 36.01);
const R20 = spread("علمنا النبي صلى الله عليه وسلم أن المريض لا يترك", 36.82, 40.02), R23 = spread("ويستشفى له من الله", 41.99, 43.22), R24 = spread("شارك هذه القصة مع من تحب", 43.88, 45.43), tFol = 45.68;
A("low", { x: 540, y: 1440, o: 1 }); A("pat2", { x: 540, y: 1440, o: .0 }); A("band", { x: 540, y: 967, o: 1 }); A("orb", { x: 880, y: 250, s: (t) => 1 + .04 * Math.sin(t * 1.3), o: 1 });
// SA
SC("SA", 0.15, 6.0); { const S = $("SA"), sl = sealEl(S), fl = flagEl(S, 230), ch = chipEl(S, "الراية", "y", 62), b = chipEl(S, "يفتح الله على يديه", "m", 56);
  SS(sl, 0.3, 5.8, .2, { x: 790, y: 380 }); SS(fl, R2[1][1], 5.8, .2, { x: 290, y: 420 }); SS(ch, R2[1][1] + 0.1, 5.8, .2, { x: 290, y: 650 }); SS(b, R2[5][1], 5.8, .2, { x: 540, y: 860 }); BURSTS.push({ t: 0.5, x: 790, y: 380 }, { t: R2[1][1] + 0.3, x: 290, y: 420 }); }
// SB
SC("SB", 6.25, 8.0); { const S = $("SB"), a = chipEl(S, "المفاجأة", "y", 70), md = medEl(S, 230); SS(a, 6.4, 7.8, .2, { x: 540, y: 380 }); SS(md, 7.0, 7.8, .2, { x: 540, y: 660 }); BURSTS.push({ t: 7.2, x: 540, y: 660 }); }
// SC
SC("SC", 8.15, 13.0); { const S = $("SC"), kh = chipEl(S, "خيبر", "c", 76), sl = sealEl(S), b = bubbleEl(S, "أين عليّ بن أبي طالب؟", 62);
  SS(kh, R4[2][1], 12.8, .2, { x: 790, y: 360 }); SS(sl, R4[4][1], 12.8, .2, { x: 290, y: 360 }); SS(b, 11.25, 12.8, .2, { x: 540, y: 740 }); BURSTS.push({ t: 11.4, x: 540, y: 740 }); }
// SD
SC("SD", 12.9, 16.4); { const S = $("SD"), a = chipEl(S, "عليّ", "m", 72), ey = eyeEl(S), pn = chipEl(S, "يشتكي عينيه", "c", 56);
  SS(a, 13.0, 16.2, .2, { x: 540, y: 330 }); SS(ey, R8[2][1], 16.2, .2, { x: 540, y: 620 }); SS(pn, R8[1][1], 16.2, .2, { x: 540, y: 820 }); BURSTS.push({ t: R8[2][1] + 0.3, x: 540, y: 620 }); }
// SE
SC("SE", 16.15, 17.95); { const S = $("SE"), sl = sealEl(S), ar = arrowEl(S, 440, 560, 640, 560), a = chipEl(S, "عليّ", "m", 66);
  SS(sl, 16.25, 17.75, .2, { x: 290, y: 560 }); D(ar, inc(R9[0][1], R9[3][1] + 0.1, "io")); A(ar.parentNode, { x: 540, y: 960, o: seg(R9[0][1], 17.75, .2) }); SS(a, R9[3][1], 17.75, .2, { x: 790, y: 560 }); }
// SF
SC("SF", 17.9, 21.1); { const S = $("SF"), sl = sealEl(S), dr = dropEl(S, 90), ey = eyeEl(S), du = chipEl(S, "دعاء", "y", 66);
  SS(sl, R10[0][1], 20.9, .2, { x: 790, y: 380 }); SS(ey, R10[7][1] - 0.5, 20.9, .2, { x: 290, y: 760 }); A(dr, { x: [[R10[6][1], 760], [R10[7][1] + 0.4, 320, "io"]], y: [[R10[6][1], 460], [R10[7][1] + 0.4, 700, "io"]], s: pop(R10[6][1]), o: seg(R10[6][1], R10[7][1] + 0.6, .1) }); SS(du, R10[8][1], 20.9, .2, { x: 540, y: 330 }); BURSTS.push({ t: R10[7][1] + 0.5, x: 300, y: 740 }); }
// SG
SC("SG", 21.2, 23.5); { const S = $("SG"), ey = eyeEl(S), a = chipEl(S, "فبرأ", "m", 80), b = chipEl(S, "كأن لم يكن به وجع", "y", 56);
  SS(ey, 21.3, 23.3, .2, { x: 540, y: 560 }); TICK(S, 540, 560, R12[0][1] - 0.4, 23.3, 300); SS(a, 21.32, 23.3, .2, { x: 540, y: 330 }); SS(b, R12[3][1], 23.3, .2, { x: 540, y: 830 }); }
// SH
SC("SH", 23.55, 24.95); { const S = $("SH"), a = chipEl(S, "البخاري", "y", 66), b = chipEl(S, "مسلم", "y", 66); SS(a, R13[1][1], 24.7, .2, { x: 790, y: 560 }); SS(b, R13[2][1], 24.7, .2, { x: 290, y: 560 }); }
// SI
SC("SI", 25.1, 31.45); { const S = $("SI"), sp = sparkEl(S, 320), mj = chipEl(S, "معجزة", "c", 76), nt = chipEl(S, "لا يُفعل مثلها", "b", 58);
  SS(sp, R14[2][1], 31.2, .2, { x: 540, y: 430 }); A(mj, { x: 540, y: 430, s: [[R14[2][1], 1.6], [R14[2][1] + 0.35, 1, "out"]], r: -6, o: seg(R14[2][1] + 0.1, 31.2, .2) }); BURSTS.push({ t: R14[2][1] + 0.4, x: 540, y: 430 }); SS(nt, R16[2][1], 31.2, .2, { x: 540, y: 760 }); X(S, 540, 760, R16[4][1], 31.2, 160); }
// SJ
SC("SJ", 31.55, 36.3); { const S = $("SJ"), a = chipEl(S, "العبرة", "y", 76), h = heartEl(S, 190), ey = eyeEl(S), c = chipEl(S, "لم يتركه مريضًا", "m", 56);
  SS(a, 31.7, 36.1, .2, { x: 540, y: 330 }); SS(ey, R18[2][1], 36.1, .2, { x: 290, y: 620 }); SS(h, R18[1][1], 36.1, .2, { x: 790, y: 620 }); SS(c, R19[1][1], 36.1, .2, { x: 540, y: 850 }); }
// SK
SC("SK", 36.7, 43.5); { const S = $("SK"), a = chipEl(S, "دعاء", "y", 66), b = chipEl(S, "علاج", "m", 66), c = chipEl(S, "استشفاء بالله", "b", 62), md = medEl(S, 200), h = heartEl(S, 180), ar = arrowEl(S, 540, 380, 540, 520);
  SS(a, 40.2, 43.3, .2, { x: 790, y: 700 }); SS(h, 40.3, 43.3, .2, { x: 790, y: 520 }); SS(b, 41.1, 43.3, .2, { x: 540, y: 700 }); SS(md, 41.2, 43.3, .2, { x: 540, y: 520 }); SS(c, R23[0][1], 43.3, .2, { x: 290, y: 700 }); BURSTS.push({ t: R23[0][1] + 0.3, x: 290, y: 700 });
  const t = chipEl(S, "المريض لا يُترك", "c", 70); SS(t, R20[7][1], 40.1, .2, { x: 540, y: 330 }); }
SC("SL", 43.7, 80);
A("lamp", { x: 540, y: 330, s: [[43.9, .78], [44.6, .66, "out"]], o: [[43.8, 0], [44.2, 1]] }); A("name", { x: 540, y: 600, s: [[44.0, 1.1], [44.8, 1, "out"]], o: [[44.0, 0], [44.4, 1]] });
D("sh1", inc(R24[0][1], R24[0][1] + 0.45)); D("sh2", inc(R24[0][1] + 0.3, R24[0][1] + 0.7)); D("sh3", inc(R24[0][1] + 0.6, R24[0][1] + 0.85));
A("share", { x: 380, y: 830, s: [[R24[0][1] + 0.49, .6], [R24[0][1] + 1.0, 1, "back"]], o: [[R24[0][1] + 0.49, 0], [R24[0][1] + 0.5, 1]] });
A("bell", { x: 700, y: 830, s: [[tFol - 0.01, .6], [tFol + .5, 1, "back"]], r: [[tFol + 0.6, 0], [tFol + 0.7, 14, "out"], [tFol + 0.85, -12, "io"], [tFol + 1.0, 8, "io"], [tFol + 1.15, 0, "io"]], o: [[tFol - 0.01, 0], [tFol, 1]] }); D("bl1", inc(tFol, tFol + 0.6)); D("bl2", inc(tFol + 0.5, tFol + 0.8));
