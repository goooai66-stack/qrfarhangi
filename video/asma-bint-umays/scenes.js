function haloEl(p, label, size = 210, fs = 46) { const s = box(size, size, "-105 -105 210 210", p); mk("circle", { r: 84, fill: T.fill, stroke: T.red, "stroke-width": 8, "stroke-dasharray": "16 11" }, s); const t = mk("text", { x: 0, y: fs / 3, "text-anchor": "middle", "font-family": "Cairo", "font-weight": 800, "font-size": fs, fill: T.ink }, s); t.textContent = label; return s; }
function heartEl(p, w = 120) { const s = box(w, w, "0 0 100 100", p); mk("path", { d: "M50,86 C10,56 14,22 36,20 C44,20 49,26 50,32 C51,26 56,20 64,20 C86,22 90,56 50,86 Z", fill: T.red, stroke: T.ink, "stroke-width": 5, "stroke-linejoin": "round" }, s); return s; }
const V1 = spread("أم جاءت إلى النبي صلى الله عليه وسلم خائفة على أولادها", 0.21, 4.37), V3 = spread("جاءت أسماء بنت عميس رضي الله عنها إلى النبي صلى الله عليه وسلم", 6.29, 10.53), V5 = spread("إن بني جعفر تسرع إليهم العين", 12.02, 14.39);
const V7 = spread("فقال النبي صلى الله عليه وسلم نعم", 16.18, 18.33), V8 = spread("لو كان شيء يسبق القدر", 18.66, 20.37), V11 = spread("فالنبي صلى الله عليه وسلم لم يسخر من خوفها", 23.24, 25.9), V12 = spread("ولم ينكر أن العين حقيقة", 26.14, 27.74), V13 = spread("بل أذن لها بالرقية لأولادها", 28.3, 29.96);
const V15 = spread("فعوذهم بما كان يعوذ به النبي صلى الله عليه وسلم الحسن والحسين", 32.47, 36.92), V16 = spread("أعيذكما بكلمات الله التامة", 37.29, 38.95), V17 = spread("من كل شيطان وهامة", 39.57, 41.15), V18 = spread("ومن كل عين لامة", 41.44, 42.85), V19 = spread("شارك هذه القصة مع كل أم تخاف على أولادها", 43.47, 46.2), tFol = 46.58;
A("low", { x: 540, y: 1440, o: 1 }); A("pat2", { x: 540, y: 1440, o: .05 }); A("band", { x: 540, y: 967, o: 1 });
A("orb", { x: 880, y: 250, s: (t) => 1 + .05 * Math.sin(t * 1.5), o: .85 });
// SA
SC("SA", 0.15, 5.75); { const S = $("SA"), mo = haloEl(S, "أمّ", 240, 62), sl = sealEl(S), ar = arrowEl(S, 640, 380, 470, 380), hs = [330, 540, 750].map(() => haloEl(S, "", 150)), fe = chipEl(S, "خائفة", "c", 62), q = textEl(S, "؟", 200, T.red);
  SS(mo, V1[0][1], 5.5, .2, { x: 790, y: 380 }); SS(sl, V1[3][1], 5.5, .2, { x: 290, y: 380 }); D(ar, inc(V1[1][1], V1[3][1] + 0.2)); A(ar.parentNode, { x: 540, y: 960, o: seg(V1[1][1], 5.5, .2) });
  hs.forEach((h, i) => SS(h, V1[10][1] + i * 0.12 - 0.3, 5.5, .2, { x: 330 + i * 210, y: 760 })); SS(fe, V1[8][1], 5.5, .2, { x: 540, y: 600 }); SS(q, 4.8, 5.5, .2, { x: 540, y: 880 }); BURSTS.push({ t: V1[3][1] + 0.4, x: 290, y: 380 }); }
// SB
SC("SB", 6.2, 14.55); { const S = $("SB"), a = chipEl(S, "أسماء بنت عميس", "y", 54), sl = sealEl(S), ar = arrowEl(S, 520, 330, 440, 330), hs = [330, 540, 750].map(() => haloEl(S, "", 150)), jf = chipEl(S, "بنو جعفر", "b", 58), ey = eyeEl(S), ar2 = arrowEl(S, 780, 860, 330, 860);
  SS(a, V3[1][1], 14.3, .2, { x: 790, y: 330 }); SS(sl, V3[8][1], 14.3, .2, { x: 290, y: 330 }); hs.forEach((h, i) => SS(h, V5[1][1] + i * 0.1, 14.3, .2, { x: 750 - i * 210, y: 600 })); SS(jf, V5[2][1], 14.3, .2, { x: 540, y: 470 });
  SS(ey, V5[3][1], 14.3, .2, { x: [[V5[3][1], 880], [V5[4][1] + 0.4, 330, "in"]], y: 860 }); D(ar2, inc(V5[3][1], V5[4][1] + 0.4, "in")); A(ar2.parentNode, { x: 540, y: 960, o: seg(V5[3][1], 14.3, .2) }); BURSTS.push({ t: V5[4][1] + 0.5, x: 330, y: 860 }); }
// SC
SC("SC", 14.65, 18.55); { const S = $("SC"), b = bubbleEl(S, "أفأسترقي لهم؟", 76), sl = sealEl(S), nm = chipEl(S, "نعم", "m", 84);
  SS(b, 14.75, 16.0, .2, { x: 540, y: 400 }); SS(sl, 16.2, 18.35, .2, { x: 540, y: 380 }); SS(nm, V7[6][1], 18.35, .2, { x: 540, y: 640 }); TICK(S, 540, 880, V7[6][1] + 0.2, 18.35, 190); BURSTS.push({ t: V7[6][1] + 0.3, x: 540, y: 640 }); }
// SD
SC("SD", 18.6, 22.8); { const S = $("SD"), c1 = chipEl(S, "القدر", "y", 66), c2 = chipEl(S, "العين", "c", 66), tr = chipEl(S, "الترمذي", "b", 52), b1 = document.createElement("div"), b2 = document.createElement("div");
  [b1, b2].forEach((b, i) => { b.className = "a"; b.style.cssText = `width:620px; height:46px; border:6px solid ${T.ink}; border-radius:30px; background:rgba(255,255,255,.35); overflow:hidden`; const f = document.createElement("div"); f.style.cssText = `position:absolute; right:0; top:0; bottom:0; width:0; background:${i ? T.red : T.gold}`; b.appendChild(f); S.appendChild(b); b.f = f; });
  SS(c1, V8[4][1], 22.6, .2, { x: 860, y: 430 }); SS(c2, V8[4][1] + 0.2, 22.6, .2, { x: 860, y: 640 }); A(b1, { x: 440, y: 430, o: seg(V8[4][1], 22.6, .2) }); A(b2, { x: 440, y: 640, o: seg(V8[4][1] + 0.2, 22.6, .2) });
  CUST.push((t) => { b1.f.style.width = (92 * clamp((t - V8[4][1]) / 1.4)) + "%"; b2.f.style.width = (100 * EZ.in(clamp((t - V8[4][1] - 0.1) / 1.9))) + "%"; }); BURSTS.push({ t: 21.9 - 0.2, x: 440, y: 640 }); SS(tr, 21.95, 22.6, .2, { x: 540, y: 860 }); }
// SE
SC("SE", 23.2, 28.2); { const S = $("SE"), sl = sealEl(S), mo = haloEl(S, "أمّ", 200, 56), sk = chipEl(S, "سخرية", "c", 58), ey = eyeEl(S), hq = chipEl(S, "العين حقيقة", "m", 58);
  SS(sl, V11[0][1], 28.0, .2, { x: 790, y: 330 }); SS(mo, V11[8][1], 28.0, .2, { x: 290, y: 330 }); SS(sk, V11[6][1], 25.8, .2, { x: 540, y: 600 }); X(S, 540, 600, V11[6][1] + 0.4, 25.8, 300); SS(ey, V12[3][1], 28.0, .2, { x: 790, y: 760 }); SS(hq, V12[4][1], 28.0, .2, { x: 360, y: 760 }); TICK(S, 540, 900, V12[4][1] + 0.3, 28.0, 140); }
// SF
SC("SF", 28.25, 30.2); { const S = $("SF"), ms = mushEl(S, 300), hs = [330, 540, 750].map(() => haloEl(S, "", 150)), rq = chipEl(S, "رقية", "m", 66);
  SS(ms, V13[3][1], 30.0, .2, { x: 540, y: 400 }); SS(rq, V13[3][1] + 0.1, 30.0, .2, { x: 540, y: 600 }); hs.forEach((h, i) => SS(h, V13[4][1] + i * 0.1, 30.0, .2, { x: 750 - i * 210, y: 820 })); }
// SG
SC("SG", 30.5, 37.1); { const S = $("SG"), hs = chipEl(S, "الحسن", "y", 60), hn = chipEl(S, "الحسين", "y", 60), sh = shieldEl(S), sl = sealEl(S), co = chipEl(S, "عوّذهم", "m", 66), ey = eyeEl(S);
  SS(ey, 31.0, 32.4, .2, { x: 540, y: 330 }); SS(sh, 32.8, 36.9, .2, { x: 540, y: 600, s: [[32.8, .5], [33.3, .85, "pop"]] }); SS(co, V15[0][1], 36.9, .2, { x: 540, y: 330 }); SS(sl, V15[5][1], 36.9, .2, { x: 540, y: 900, s: [[V15[5][1], .5], [V15[5][1] + 0.4, .6, "pop"]] }); SS(hs, V15[10][1], 36.9, .2, { x: 790, y: 640 }); SS(hn, V15[11][1], 36.9, .2, { x: 290, y: 640 }); BURSTS.push({ t: 33.4, x: 540, y: 600 }); }
// SH
SC("SH", 37.2, 43.0); { const S = $("SH"), card = cardEl(S, 900, 600); A(card, { x: 540, y: 520, s: pop(37.25, .45), o: seg(37.25, 42.9, .2) });
  const mkL = (txt, y, t) => { const d = textEl(S, txt, 66, T.ink); A(d, { x: 540, y: [[t - 0.001, y + 24], [t + 0.35, y, "out"]], o: [[t - 0.001, 0], [t, 1], [42.9, 1], [43.1, 0, "in"]] }); BURSTS.push({ t: t + 0.1, x: 540, y }); };
  mkL("أعيذكما بكلمات الله التامة", 400, V16[0][1]); mkL("من كل شيطان وهامّة", 530, V17[0][1]); mkL("ومن كل عين لامّة", 660, V18[0][1]); const h = heartEl(S, 130); SS(h, 38.9, 42.9, .2, { x: 790, y: 880 }); }
SC("SL", 43.2, 80);
A("lamp", { x: 540, y: 330, s: [[43.4, .78], [44.1, .66, "out"]], o: [[43.3, 0], [43.7, 1]] }); A("name", { x: 540, y: 600, s: [[43.5, 1.1], [44.3, 1, "out"]], o: [[43.5, 0], [43.9, 1]] });
D("sh1", inc(V19[0][1], V19[0][1] + 0.45)); D("sh2", inc(V19[0][1] + 0.3, V19[0][1] + 0.7)); D("sh3", inc(V19[0][1] + 0.6, V19[0][1] + 0.85));
A("share", { x: 380, y: 830, s: [[V19[0][1] + 0.49, .6], [V19[0][1] + 1.0, 1, "back"]], o: [[V19[0][1] + 0.49, 0], [V19[0][1] + 0.5, 1]] });
A("bell", { x: 700, y: 830, s: [[tFol - 0.01, .6], [tFol + .5, 1, "back"]], r: [[tFol + 0.6, 0], [tFol + 0.7, 14, "out"], [tFol + 0.85, -12, "io"], [tFol + 1.0, 8, "io"], [tFol + 1.15, 0, "io"]], o: [[tFol - 0.01, 0], [tFol, 1]] }); D("bl1", inc(tFol, tFol + 0.6)); D("bl2", inc(tFol + 0.5, tFol + 0.8));
