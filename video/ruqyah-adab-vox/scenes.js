// torn-paper strips (override of the kit's chipEl)
const TORN = ["#e8dcc0", "#d6b987", "#c8372d", "#e5b14a", "#f3ece0"]; let tornN = 0;
function tornPoly(r) { const pts = [], n = 10; for (let i = 0; i <= n; i++) pts.push([i / n * 100, r() * 4]); for (let i = 1; i < 4; i++) pts.push([100 - r() * 2.5, i / 4 * 100]); for (let i = n; i >= 0; i--) pts.push([i / n * 100, 100 - r() * 4]); for (let i = 3; i > 0; i--) pts.push([r() * 2.5, i / 4 * 100]); return "polygon(" + pts.map((p) => p[0].toFixed(1) + "% " + p[1].toFixed(1) + "%").join(",") + ")"; }
function chipEl(parent, txt, cls = "", size = 54) { const d = document.createElement("div"); d.className = "a"; const s = document.createElement("span"); const r = rng(77 + tornN * 13); s.className = "chip " + cls; s.style.fontSize = size + "px"; s.style.fontFamily = "Amiri"; s.style.fontWeight = 700;
  const bg = cls === "c" ? "#c8372d" : cls === "y" ? "#e5b14a" : cls === "m" ? "#a9c7a0" : cls === "b" ? "#d6b987" : TORN[tornN % 2 ? 4 : 0]; tornN++; s.style.background = bg; s.style.color = cls === "c" ? "#fbf1e0" : "#241a10"; s.style.clipPath = tornPoly(r); s.style.transform = `rotate(${((r() - .5) * 5).toFixed(1)}deg)`; s.style.border = "none"; s.style.boxShadow = "none"; s.style.padding = "8px 44px 16px";
  s.textContent = txt; d.appendChild(s); parent.appendChild(d); return d; }
function numEl(p, n) { const s = box(240, 240, "-120 -120 240 240", p); mk("circle", { r: 100, fill: "#1c1612", stroke: "#e5b14a", "stroke-width": 8, "stroke-dasharray": "3 14", "stroke-linecap": "round" }, s); const t = mk("text", { x: 0, y: 46, "text-anchor": "middle", "font-family": "Amiri", "font-weight": 700, "font-size": 150, fill: "#f3ece0" }, s); t.textContent = n; return s; }
function handEl(p, w = 240) { const s = box(w, w, "0 0 240 240", p); mk("path", { d: "M70,130 L70,60 Q70,46 84,46 Q98,46 98,60 L98,104 L98,36 Q98,22 112,22 Q126,22 126,36 L126,104 L126,44 Q126,30 140,30 Q154,30 154,44 L154,110 L154,70 Q154,56 168,56 Q182,56 182,70 L182,150 Q182,214 126,222 Q84,224 66,186 L40,134 Q34,120 48,114 Q62,110 70,130 Z", fill: T.fill, stroke: "#241a10", "stroke-width": 8, "stroke-linejoin": "round" }, s); return s; }
function dropEl(p, w = 140) { const s = box(w, w, "0 0 100 100", p); mk("path", { d: "M50,10 C30,38 18,52 18,66 C18,84 33,92 50,92 C67,92 82,84 82,66 C82,52 70,38 50,10 Z", fill: "#6aa7d8", stroke: "#241a10", "stroke-width": 5, "stroke-linejoin": "round" }, s); return s; }
function targetEl(p, w = 220) { const s = box(w, w, "0 0 100 100", p); [44, 30, 16].forEach((r, i) => mk("circle", { cx: 50, cy: 50, r, fill: i % 2 ? "#c8372d" : "#f3ece0", stroke: "#241a10", "stroke-width": 3 }, s)); return s; }
const G1 = spread("آداب الرقية الشرعية التي يغفل عنها كثير من الناس", 0.27, 3.63), G2 = spread("أخلص نية لله", 5.03, 5.94), G3 = spread("واقرأ بيقين وحضور قلب", 6.2, 7.85), G4 = spread("واعتقد أن الشفاء بيد الله وحده", 8.0, 9.72);
const G5 = spread("اقتصر على القرآن والأذكار الثابتة عن النبي صلى الله عليه وسلم", 10.66, 14.28), G6 = spread("ولا تقبل كلمات لا تفهمها أو رموزا مجهولة", 14.42, 17.23), G7 = spread("ضع يدك على موضع الألم", 18.51, 19.99), G9 = spread("ولا بأس بالنفث الخفيف بلا مبالغة", 22.19, 24.18);
const G10 = spread("يستحب أن تكون على طهارة", 25.45, 26.94), G11 = spread("وأن تدعو بتضرع وانكسار", 27.16, 28.93), G12 = spread("فهذا أقرب للإجابة", 29.17, 30.54), G13 = spread("لا تخل بامرأة أجنبية للرقية", 31.74, 33.76), G14 = spread("ولا تضرب المريض ولا تطلب مالا مقابل الشفاء", 33.99, 36.92);
const G15 = spread("اجمع بين الرقية والأخذ بأسباب العلاج", 38.06, 40.25), G16 = spread("فهذا هدي النبي صلى الله عليه وسلم", 40.53, 42.84), G17 = spread("شارك هذا المقطع لمن تحب", 43.42, 44.65), tFol = 44.87;
A("low", { x: 540, y: 1440, o: 1 }); A("pat2", { x: 540, y: 1440, o: .0 }); A("band", { x: 540, y: 967, o: 1 }); A("orb", { x: 880, y: 250, s: 1, o: .0 });
const NUM = (S, n, t, to, y = 330) => { const e = numEl(S, n); A(e, { x: 790, y, s: [[t - 0.001, 1.8], [t + 0.35, 1, "out"]], r: [[t - 0.001, -14], [t + 0.35, -6, "out"]], o: seg(t, to, .2) }); BURSTS.push({ t: t + 0.35, x: 790, y }); return e; };
// S0
SC("SA", 0.2, 3.85); { const S = $("SA"), a = chipEl(S, "آداب الرقية الشرعية", "c", 80), b = chipEl(S, "يغفل عنها كثير من الناس", "", 56), ms = mushEl(S, 300);
  SS(a, G1[0][1], 3.65, .2, { x: 540, y: 330 }); SS(b, G1[4][1], 3.65, .2, { x: 540, y: 520 }); SS(ms, G1[3][1], 3.65, .2, { x: 540, y: 760 }); BURSTS.push({ t: G1[0][1] + 0.3, x: 540, y: 330 }); }
// 1
SC("SB", 4.25, 10.05); { const S = $("SB"), a = chipEl(S, "إخلاص النية لله", "y", 60), b = chipEl(S, "يقين وحضور قلب", "", 58), c = chipEl(S, "الشفاء بيد الله وحده", "m", 58);
  NUM(S, "١", 4.31, 9.85, 330); SS(a, G2[1][1], 9.85, .2, { x: 400, y: 520 }); SS(b, G3[1][1], 9.85, .2, { x: 400, y: 690 }); SS(c, G4[3][1], 9.85, .2, { x: 400, y: 860 }); }
// 2
SC("SC", 10.15, 17.4); { const S = $("SC"), a = chipEl(S, "القرآن", "m", 62), b = chipEl(S, "الأذكار الثابتة", "m", 58), c = chipEl(S, "كلمات لا تفهمها", "c", 54), d = chipEl(S, "رموز مجهولة", "c", 54);
  NUM(S, "٢", 10.2, 17.2, 330); SS(a, G5[2][1], 17.2, .2, { x: 400, y: 450 }); SS(b, G5[3][1], 17.2, .2, { x: 400, y: 600 }); SS(c, G6[2][1], 17.2, .2, { x: 400, y: 760 }); X(S, 400, 760, G6[4][1] + 0.3, 17.2, 170); SS(d, G6[6][1], 17.2, .2, { x: 400, y: 910 }); X(S, 400, 910, G6[7][1] + 0.2, 17.2, 170); }
// 3
SC("SD", 17.8, 24.4); { const S = $("SD"), tg = targetEl(S, 240), hd = handEl(S, 260), mw = chipEl(S, "موضع الألم", "y", 56), nf = chipEl(S, "نفث خفيف", "b", 56), dr = dropEl(S, 90), mb = chipEl(S, "مبالغة", "c", 56);
  NUM(S, "٣", 17.9, 24.2, 330); SS(tg, G7[3][1], 24.2, .2, { x: 400, y: 560 }); SS(mw, G7[3][1] + 0.1, 24.2, .2, { x: 400, y: 740 }); A(hd, { x: [[G7[0][1], 160], [G7[1][1] + 0.2, 400, "io"]], y: [[G7[0][1], 560], [G7[1][1] + 0.2, 520, "io"]], r: -20, s: pop(G7[0][1]), o: seg(G7[0][1], 24.2, .2) });
  SS(nf, G9[2][1], 24.2, .2, { x: 400, y: 860 }); SS(dr, G9[3][1], 24.2, .2, { x: 650, y: 860 }); SS(mb, G9[5][1], 24.2, .2, { x: 790, y: 700 }); X(S, 790, 700, G9[5][1] + 0.3, 24.2, 170); }
// 4
SC("SE", 24.75, 30.7); { const S = $("SE"), a = chipEl(S, "طهارة", "b", 66), dr = dropEl(S, 130), b = chipEl(S, "تضرّع وانكسار", "y", 58), c = chipEl(S, "أقرب للإجابة", "m", 60);
  NUM(S, "٤", 24.86, 30.5, 330); SS(a, G10[4][1], 30.5, .2, { x: 400, y: 500 }); SS(dr, G10[4][1], 30.5, .2, { x: 640, y: 500 }); SS(b, G11[3][1], 30.5, .2, { x: 400, y: 700 }); SS(c, G12[2][1], 30.5, .2, { x: 400, y: 880 }); TICK(S, 760, 880, G12[2][1] + 0.3, 30.5, 150); }
// 5
SC("SF", 31.05, 37.15); { const S = $("SF"), a = chipEl(S, "خلوة بامرأة أجنبية", "c", 54), b = chipEl(S, "ضرب المريض", "c", 56), c = chipEl(S, "طلب المال", "c", 56);
  NUM(S, "٥", 31.1, 36.95, 330); SS(a, G13[3][1], 36.95, .2, { x: 400, y: 520 }); X(S, 400, 520, G13[4][1] + 0.3, 36.95, 170); SS(b, G14[2][1], 36.95, .2, { x: 400, y: 710 }); X(S, 400, 710, G14[2][1] + 0.5, 36.95, 170); SS(c, G14[5][1], 36.95, .2, { x: 400, y: 900 }); X(S, 400, 900, G14[6][1] + 0.2, 36.95, 170); }
// 6
SC("SG", 37.4, 43.0); { const S = $("SG"), ms = mushEl(S, 300), md = medEl(S, 220), pl = textEl(S, "+", 160, "#c8372d"), sl = sealEl(S);
  SS(ms, G15[2][1], 42.8, .2, { x: 790, y: 520 }); SS(md, G15[5][1], 42.8, .2, { x: 290, y: 520 }); SS(pl, G15[3][1], 42.8, .2, { x: 540, y: 520 }); SS(sl, G16[2][1], 42.8, .2, { x: 540, y: 820 }); BURSTS.push({ t: G15[5][1] + 0.3, x: 290, y: 520 }, { t: G16[2][1] + 0.3, x: 540, y: 820 }); }
SC("SL", 43.2, 80);
A("lamp", { x: 540, y: 330, s: [[43.4, .78], [44.1, .66, "out"]], o: [[43.3, 0], [43.7, 1]] }); A("name", { x: 540, y: 600, s: [[43.5, 1.1], [44.3, 1, "out"]], o: [[43.5, 0], [43.9, 1]] });
D("sh1", inc(G17[0][1], G17[0][1] + 0.45)); D("sh2", inc(G17[0][1] + 0.3, G17[0][1] + 0.7)); D("sh3", inc(G17[0][1] + 0.6, G17[0][1] + 0.85));
A("share", { x: 380, y: 830, s: [[G17[0][1] + 0.49, .6], [G17[0][1] + 1.0, 1, "back"]], o: [[G17[0][1] + 0.49, 0], [G17[0][1] + 0.5, 1]] });
A("bell", { x: 700, y: 830, s: [[tFol - 0.01, .6], [tFol + .5, 1, "back"]], r: [[tFol + 0.6, 0], [tFol + 0.7, 14, "out"], [tFol + 0.85, -12, "io"], [tFol + 1.0, 8, "io"], [tFol + 1.15, 0, "io"]], o: [[tFol - 0.01, 0], [tFol, 1]] }); D("bl1", inc(tFol, tFol + 0.6)); D("bl2", inc(tFol + 0.5, tFol + 0.8));
