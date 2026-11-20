import React, { useMemo } from "react";
import { AbsoluteFill, Easing, interpolate, Sequence, spring, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { Audio } from "@remotion/media";
import { ICONS, INK } from "./icons";
import type { Cue, Sec, VoxData } from "./Vox";

// "Kinetic pop" style: bright drifting gradients, chapter colour wipes, bento cards, karaoke Arabic captions.
const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
const outExpo = Easing.bezier(0.16, 1, 0.3, 1);
const inOut = Easing.bezier(0.65, 0, 0.35, 1);
const TINT: Record<string, string> = { y: "#ffe7a3", p: "#ffd0dc", t: "#c8f0ee", g: "#d3f2c9", r: "#ffd1c9", w: "#ffffff", o: "#ffdcc0", b: "#d4e6ff" };
const DOT: Record<string, string> = { y: "#f4b400", p: "#ec5f86", t: "#18a7a0", g: "#3fae5a", r: "#e8503a", w: "#7c6cf0", o: "#f08a24", b: "#3b82f6" };
const sal = (s: string) => s.replace(/ﷺ/g, '<span style="font-family:Amiri">ﷺ</span>');
const darken = (hex: string, k = 0.55) => { const n = parseInt(hex.slice(1), 16); const c = [(n >> 16) & 255, (n >> 8) & 255, n & 255].map((v) => Math.round(v * k)); return `rgb(${c.join(",")})`; };

const Icon: React.FC<{ name: string }> = ({ name }) => (
  <svg viewBox="0 0 200 200" style={{ width: "100%", height: "100%", overflow: "visible" }} fill="none" stroke={INK} strokeWidth={7}
    strokeLinecap="round" strokeLinejoin="round" dangerouslySetInnerHTML={{ __html: ICONS[name] ?? "" }} />
);

// ---------- background: drifting colour blobs + panning dot grid
const Backdrop: React.FC<{ col: string }> = ({ col }) => {
  const frame = useCurrentFrame();
  const t = frame / 30;
  const blob = (x: number, y: number, r: number, c: string, ph: number) => (
    <div style={{ position: "absolute", left: x + Math.sin(t * 0.21 + ph) * 120, top: y + Math.cos(t * 0.17 + ph) * 90, width: r, height: r, borderRadius: "50%", background: c, filter: "blur(90px)", opacity: 0.75 }} />
  );
  return (
    <AbsoluteFill style={{ background: "#fff8ef", overflow: "hidden" }}>
      {blob(-200, -260, 900, "#ffd9c2", 0)}
      {blob(1250, -200, 820, "#d9f3ee", 2)}
      {blob(900, 520, 760, "#e8e0ff", 4)}
      {blob(-120, 600, 700, col, 1)}
      <div style={{ position: "absolute", inset: -60, backgroundImage: "radial-gradient(rgba(40,30,60,.13) 2px, transparent 2.6px)", backgroundSize: "36px 36px",
        translate: `${(t * 6) % 36}px ${(t * 4) % 36}px` }} />
    </AbsoluteFill>
  );
};

// ---------- top bar: channel tag + chapter dots + progress
const TopBar: React.FC<{ data: VoxData }> = ({ data }) => {
  const frame = useCurrentFrame();
  const t = frame / 30;
  const cur = data.secs.findIndex((s) => t >= s.a && t < s.b);
  return (
    <div style={{ position: "absolute", left: 60, right: 60, top: 26, height: 56, display: "flex", alignItems: "center", gap: 18, direction: "rtl" }}>
      <div style={{ fontFamily: "Changa", fontWeight: 800, fontSize: 30, color: "#fff", background: "#2b2350", borderRadius: 999, padding: "4px 26px 8px" }}>في معية الله</div>
      <div style={{ flex: 1, display: "flex", gap: 8, height: 12 }}>
        {data.secs.map((s, i) => (
          <div key={i} style={{ flex: s.b - s.a, borderRadius: 99, background: "rgba(43,35,80,.12)", overflow: "hidden" }}>
            <div style={{ height: "100%", borderRadius: 99, background: i === cur ? "#2b2350" : "#7c6cf0", width: `${interpolate(t, [s.a, s.b], [0, 100], clamp)}%` }} />
          </div>
        ))}
      </div>
    </div>
  );
};

// ---------- layout of one section's cards
type Card = { kind: "c" | "q"; t0: number; t1: number; text: string; col: string; ic: string | null; x: number; y: number; w: number; h: number; fs: number };
const COL_R = 690, COL_L = 100, CW = 550, FULL = 1140;
const layout = (S: Sec): Card[] => {
  const its = S.items.map(([t, kind, text, col, ic, g]) => ({ t, kind, text, col, ic, g }));
  const gs = [...new Set(its.map((i) => i.g))].sort((a, b) => a - b);
  const out: Card[] = [];
  gs.forEach((g, gi) => {
    const gItems = its.filter((i) => i.g === g).sort((a, b) => a.t - b.t);
    const gEnd = gi + 1 < gs.length ? Math.min(...its.filter((i) => i.g === gs[gi + 1]).map((i) => i.t)) : S.b;
    const gq = gItems.filter((i) => i.kind === "q");
    let y = gq.length ? 470 : 130, half: "R" | "L" = "R";
    gItems.forEach((it) => {
      if (it.kind === "q") {
        const nextQ = gq.find((q) => q.t > it.t), len = it.text.length;
        out.push({ kind: "q", t0: it.t, t1: nextQ ? nextQ.t : gEnd, text: it.text, col: it.col, ic: null, x: COL_L, y: 120, w: FULL, h: 320, fs: len <= 30 ? 68 : len <= 60 ? 56 : len <= 100 ? 46 : 40 });
        return;
      }
      const wide = it.text.length > 14;
      if (wide && half === "L") { y += 150; half = "R"; }
      const x = wide ? COL_L : half === "R" ? COL_R : COL_L;
      out.push({ kind: "c", t0: it.t, t1: gEnd, text: it.text, col: it.col, ic: it.ic, x, y, w: wide ? FULL : CW, h: 130, fs: it.text.length > 34 ? 38 : wide ? 44 : 42 });
      if (wide || half === "L") { y += 150; half = "R"; } else half = "L";
    });
  });
  return out;
};

const Burst: React.FC<{ age: number; color: string }> = ({ age, color }) => {
  if (age > 0.6) return null;
  return (
    <>
      {Array.from({ length: 8 }).map((_, k) => {
        const a = (k / 8) * Math.PI * 2, d = interpolate(age, [0, 0.6], [20, 110], { ...clamp, easing: outExpo });
        return <div key={k} style={{ position: "absolute", right: 70 + Math.cos(a) * d, top: 65 + Math.sin(a) * d, width: 14, height: 14, borderRadius: 7, background: color, opacity: interpolate(age, [0.2, 0.6], [1, 0], clamp) }} />;
      })}
    </>
  );
};

const SectionStage: React.FC<{ S: Sec; si: number }> = ({ S, si }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const age = frame / fps, t = S.a + age;
  const cards = useMemo(() => layout(S), [S]);
  const out = interpolate(t, [S.b - 0.05, S.b + 0.3], [1, 0], clamp);
  const heroIn = spring({ frame: frame - 0.9 * fps, fps, config: { damping: 12, stiffness: 120 } });
  const r = (k: number) => `${44 + Math.sin(t * 0.9 + k) * 8}% ${56 + Math.cos(t * 0.7 + k) * 8}% ${48 + Math.sin(t * 0.8 + k * 2) * 8}% ${52 + Math.cos(t + k) * 8}% / ${50 + Math.sin(t * 0.6 + k) * 8}% ${46 + Math.cos(t * 0.9 + k) * 8}% ${54 + Math.sin(t * 0.7) * 8}% ${50 + Math.cos(t * 0.5 + k) * 8}%`;
  return (
    <AbsoluteFill style={{ opacity: out, scale: `${1 + age * 0.0015}` }}>
      {/* hero blob + icon on the right */}
      <div style={{ position: "absolute", left: 1330, top: 150, width: 500, height: 500, scale: `${heroIn}`, rotate: `${(1 - heroIn) * -25}deg` }}>
        <div style={{ position: "absolute", inset: 0, borderRadius: r(si), background: S.col, boxShadow: `0 30px 60px ${S.col}` }} />
        <div style={{ position: "absolute", inset: 40, borderRadius: r(si + 3), border: "5px dashed rgba(255,255,255,.8)" }} />
        <div style={{ position: "absolute", left: 90, top: 80, width: 320, height: 320, translate: `0px ${Math.sin(t * 1.5) * 12}px`, rotate: `${Math.sin(t * 1.1) * 4}deg`,
          filter: "drop-shadow(0 16px 18px rgba(40,30,60,.25))" }}><Icon name={S.ic} /></div>
      </div>
      <div style={{ position: "absolute", left: 1330, top: 670, width: 500, textAlign: "center", direction: "rtl", opacity: interpolate(age, [1.1, 1.5], [0, 1], clamp),
        translate: `0px ${interpolate(age, [1.1, 1.5], [20, 0], { ...clamp, easing: outExpo })}px` }}>
        <span style={{ fontFamily: "Changa", fontWeight: 800, fontSize: 40, color: "#2b2350", background: "#fff", borderRadius: 999, padding: "6px 30px 12px", boxShadow: "0 10px 30px rgba(43,35,80,.12)" }}
          dangerouslySetInnerHTML={{ __html: (S.num ? S.num + " · " : "") + sal(S.ar) }} />
      </div>
      {cards.map((c, i) => {
        if (t < c.t0 || t >= c.t1 + 0.3) return null;
        const f0 = Math.round(c.t0 * fps) - Math.round(S.a * fps);
        const sp = spring({ frame: frame - f0, fps, config: { damping: 14, stiffness: 140 } });
        const o = Math.min(interpolate(t, [c.t0, c.t0 + 0.12], [0, 1], clamp), interpolate(t, [c.t1, c.t1 + 0.25], [1, 0], clamp));
        const tilt = Math.sin(t * 0.8 + i) * 2;
        if (c.kind === "q") {
          return (
            <div key={i} style={{ position: "absolute", left: c.x, top: c.y, width: c.w, minHeight: c.h, opacity: o, perspective: 1200 }}>
              <div style={{ rotate: `x ${(1 - sp) * 60}deg`, transformOrigin: "50% 0%", borderRadius: 36, padding: 6, background: "linear-gradient(120deg,#ffb86b,#ff6fa3,#8b7bff,#3cc8c0)", boxShadow: "0 30px 70px rgba(80,50,120,.22)" }}>
                <div style={{ borderRadius: 31, background: "#fffdf8", padding: "40px 60px 46px", textAlign: "center", direction: "rtl", fontFamily: "Amiri", fontWeight: 700, color: "#2b2350", fontSize: c.fs, lineHeight: 1.8, rotate: `y ${tilt}deg` }}
                  dangerouslySetInnerHTML={{ __html: sal(c.text) }} />
              </div>
            </div>
          );
        }
        return (
          <div key={i} style={{ position: "absolute", left: c.x, top: c.y, width: c.w, height: c.h, opacity: o, perspective: 1000 }}>
            <div style={{ position: "absolute", inset: 0, borderRadius: 30, background: TINT[c.col] ?? "#fff", boxShadow: "0 18px 40px rgba(43,35,80,.14)", border: "3px solid rgba(255,255,255,.9)",
              display: "flex", flexDirection: "row", direction: "rtl", alignItems: "center", gap: 22, padding: "0 30px",
              translate: `0px ${(1 - sp) * 80}px`, rotate: `y ${(1 - sp) * -40}deg`, scale: `${0.85 + 0.15 * sp}` }}>
              {c.ic ? <div style={{ width: 92, height: 92, flex: "none", borderRadius: 26, background: "#fff", padding: 12, boxSizing: "border-box", rotate: `${Math.sin(t * 1.3 + i) * 5}deg` }}><Icon name={c.ic} /></div> : null}
              <div style={{ fontFamily: "Changa", fontWeight: 800, fontSize: c.fs, color: c.col === "r" ? darken(DOT.r, 0.8) : "#2b2350", lineHeight: 1.25 }} dangerouslySetInnerHTML={{ __html: sal(c.text) }} />
              <div style={{ position: "absolute", left: 18, top: 18, width: 16, height: 16, borderRadius: 8, background: DOT[c.col] ?? DOT.w }} />
            </div>
            <Burst age={t - c.t0} color={DOT[c.col] ?? DOT.w} />
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

// ---------- chapter wipe: a colour circle grows from the hero, shows the title, then shrinks away
const ChapterWipe: React.FC<{ S: Sec }> = ({ S }) => {
  const frame = useCurrentFrame();
  const age = frame / 30;
  const grow = interpolate(age, [0, 0.45], [0, 2300], { ...clamp, easing: inOut });
  const shrink = interpolate(age, [1.15, 1.6], [2300, 0], { ...clamp, easing: inOut });
  const rad = age < 1.15 ? grow : shrink;
  const cx = age < 1.15 ? 1580 : 960, cy = age < 1.15 ? 400 : 540;
  const words = S.ar.split(" ");
  return (
    <AbsoluteFill style={{ clipPath: `circle(${rad}px at ${cx}px ${cy}px)`, background: `linear-gradient(135deg, ${S.col}, #fff3e6)` }}>
      <div style={{ position: "absolute", inset: 0, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 24 }}>
        {S.num ? <div style={{ fontFamily: "Changa", fontWeight: 800, fontSize: 150, lineHeight: 1, color: "#2b2350", scale: `${spring({ frame: frame - 5, fps: 30, config: { damping: 10 } })}` }}>{S.num}</div> : null}
        <div style={{ display: "flex", flexDirection: "row", direction: "rtl", gap: 26, flexWrap: "wrap", justifyContent: "center", maxWidth: 1600 }}>
          {words.map((w, k) => (
            <span key={k} style={{ fontFamily: "Changa", fontWeight: 800, fontSize: 112, color: "#2b2350", lineHeight: 1.2, display: "inline-block",
              translate: `0px ${(1 - spring({ frame: frame - 8 - k * 3, fps: 30, config: { damping: 12 } })) * 80}px`,
              opacity: interpolate(frame, [8 + k * 3, 14 + k * 3], [0, 1], clamp) }} dangerouslySetInnerHTML={{ __html: sal(w) }} />
          ))}
        </div>
        <div style={{ fontFamily: "Changa", fontWeight: 500, fontSize: 40, color: darken("#7c6cf0", 0.7), direction: "ltr", opacity: interpolate(frame, [16, 24], [0, 1], clamp) }}>{S.en}</div>
      </div>
    </AbsoluteFill>
  );
};

// ---------- karaoke caption: Arabic words light up in turn, English + Chinese beneath
const Caption: React.FC<{ c: Cue }> = ({ c }) => {
  const frame = useCurrentFrame();
  const t = frame / 30, d = c.b - c.a;
  const words = c.ar.split(" ");
  const weights = words.map((w) => Math.max(2, w.replace(/[ً-ْ«»﴾﴿،.:؟!]/g, "").length));
  const total = weights.reduce((a, b) => a + b, 0);
  let acc = 0;
  const p = (t / Math.max(0.3, d - 0.15)) * total;
  const big = c.ar.length + c.en.length / 2.2 + c.zh.length * 1.4;
  const [fa, fe] = big > 260 ? [34, 21] : big > 200 ? [38, 23] : big > 150 ? [43, 25] : big > 110 ? [46, 27] : [50, 29];
  return (
    <div style={{ position: "absolute", left: 120, right: 120, bottom: 22, borderRadius: 34, background: "rgba(255,255,255,.88)", boxShadow: "0 20px 50px rgba(43,35,80,.16)",
      padding: "18px 40px 18px", textAlign: "center", border: "3px solid #fff",
      opacity: Math.min(interpolate(t, [0, 0.12], [0, 1], clamp), interpolate(t, [d - 0.1, d], [1, 0], clamp)), translate: `0px ${interpolate(t, [0, 0.15], [20, 0], clamp)}px` }}>
      <div style={{ direction: "rtl", fontFamily: "Cairo", fontWeight: 800, fontSize: fa, lineHeight: 1.6 }}>
        {words.map((w, k) => {
          const s = acc; acc += weights[k];
          const state = p >= acc ? 2 : p >= s ? 1 : 0;
          return (
            <span key={k} style={{ display: "inline-block", margin: "0 0.12em", padding: "0 0.14em", borderRadius: 12,
              color: state === 0 ? "rgba(43,35,80,.38)" : "#2b2350", background: state === 1 ? "#ffe07a" : "transparent" }} dangerouslySetInnerHTML={{ __html: sal(w) }} />
          );
        })}
      </div>
      <div style={{ fontFamily: "Changa", fontWeight: 500, color: "#6a5f8f", direction: "ltr", lineHeight: 1.35, marginTop: 2, fontSize: fe }}>{c.en}</div>
      <div style={{ fontFamily: "'Noto Sans SC'", fontWeight: 500, color: "#e0567c", direction: "ltr", lineHeight: 1.35, marginTop: 2, fontSize: fe }}>{c.zh}</div>
    </div>
  );
};

export const Kinetic: React.FC<{ data: VoxData }> = ({ data }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const f = (s: number) => Math.round(s * fps);
  const t = frame / fps;
  const cur = data.secs.find((s) => t >= s.a && t < s.b) ?? data.secs[0];
  return (
    <AbsoluteFill style={{ color: INK }}>
      <Backdrop col={cur.col} />
      <TopBar data={data} />
      {data.secs.map((S, si) => (
        <Sequence key={si} name={`Stage ${si + 1}: ${S.en}`} from={f(S.a)} durationInFrames={f(S.b - S.a + 0.35)} layout="absolute-fill">
          <SectionStage S={S} si={si} />
        </Sequence>
      ))}
      {data.secs.map((S, si) => (
        <Sequence key={`w${si}`} name={`Chapter wipe ${si + 1}`} from={f(S.a)} durationInFrames={f(1.65)} layout="absolute-fill">
          <ChapterWipe S={S} />
        </Sequence>
      ))}
      {data.caps.map((c, i) => (
        <Sequence key={`c${i}`} name={`Caption ${i + 1}`} from={f(c.a)} durationInFrames={Math.max(1, f(c.b - c.a))} layout="absolute-fill">
          <Caption c={c} />
        </Sequence>
      ))}
      <Audio src={staticFile(data.voice)} />
      {data.sfx.map(([st, name, vol], i) => (
        <Sequence key={`s${i}`} name={`SFX ${name}`} from={f(st)} durationInFrames={f(2)} layout="none">
          <Audio src={staticFile(`sfx/${name}.wav`)} volume={vol} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
