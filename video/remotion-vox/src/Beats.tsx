import React, { useMemo } from "react";
import { AbsoluteFill, Easing, interpolate, Sequence, spring, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { Audio } from "@remotion/media";
import { ICONS, INK, star4 } from "./icons";
import { KCaption, TopBar } from "./Kinetic";
import type { Sec, VoxData } from "./Vox";

// "Beats" style: every point is its own full-screen shot (big illustration + big words) that enters and leaves;
// layouts, backgrounds and transitions rotate so each shot looks new.
const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
const outExpo = Easing.bezier(0.16, 1, 0.3, 1);
const inOut = Easing.bezier(0.65, 0, 0.35, 1);
const sal = (s: string) => s.replace(/ﷺ/g, '<span style="font-family:Amiri">ﷺ</span>');
const BG = ["#fff4e6", "#e9f7f4", "#f3efff", "#fff0f4", "#fdf7de", "#ecf4ff", "#f0fbe9"];
const ACC: Record<string, string> = { y: "#f4b400", p: "#ec5f86", t: "#18a7a0", g: "#3fae5a", r: "#e8503a", w: "#7c6cf0", o: "#f08a24", b: "#3b82f6" };
const INKP = "#2b2350";

type Beat = { kind: "chapter" | "c" | "q"; t0: number; t1: number; text: string; col: string; ic: string; S: Sec; si: number; n: number };

const buildBeats = (secs: Sec[]): Beat[] => {
  const out: Beat[] = [];
  let n = 0;
  secs.forEach((S, si) => {
    const its = [...S.items].sort((a, b) => a[0] - b[0]).filter((it, k, arr) => k === 0 || it[0] - arr[k - 1][0] > 0.15);
    const first = its.length ? its[0][0] : S.b;
    const chapEnd = Math.max(S.a + 1.6, first);
    out.push({ kind: "chapter", t0: S.a, t1: chapEnd, text: S.ar, col: "w", ic: S.ic, S, si, n: n++ });
    its.forEach((it, k) => {
      const t0 = Math.max(it[0], chapEnd), t1 = k + 1 < its.length ? Math.max(its[k + 1][0], chapEnd) : S.b;
      if (t1 - t0 < 0.5) return;
      out.push({ kind: it[1] === "q" ? "q" : "c", t0, t1, text: it[2], col: it[3], ic: it[4] ?? S.ic, S, si, n: n++ });
    });
  });
  return out;
};

const Icon: React.FC<{ name: string }> = ({ name }) => (
  <svg viewBox="0 0 200 200" style={{ width: "100%", height: "100%", overflow: "visible" }} fill="none" stroke={INK} strokeWidth={7}
    strokeLinecap="round" strokeLinejoin="round" dangerouslySetInnerHTML={{ __html: ICONS[name] ?? "" }} />
);
const DOODLES = [star4(100, 100, 90, "#f6d56a"), `<circle cx="100" cy="100" r="60" fill="#ff8fab"/>`, `<path d="M20,100 Q60,40 100,100 T180,100" stroke="#3aa0a8" stroke-width="16"/>`,
  `<path d="M100,20 L100,180 M20,100 L180,100" stroke="#7c6cf0" stroke-width="22"/>`, `<rect x="40" y="40" width="120" height="120" rx="30" fill="#9fd3d6"/>`];

// Illustration: morphing blob, dashed ring, bouncing icon and orbiting doodles
const Illustration: React.FC<{ ic: string; col: string; size: number; t: number; age: number; seed: number }> = ({ ic, col, size, t, age, seed }) => {
  const { fps } = useVideoConfig();
  const pop = spring({ frame: age * fps - 3, fps, config: { damping: 11, stiffness: 130 } });
  const r = (k: number) => `${46 + Math.sin(t * 0.9 + k) * 9}% ${54 + Math.cos(t * 0.7 + k) * 9}% ${48 + Math.sin(t * 0.8 + k * 2) * 9}% ${52 + Math.cos(t + k) * 9}% / ${50 + Math.sin(t * 0.6 + k) * 9}% ${46 + Math.cos(t * 0.9 + k) * 9}% ${54 + Math.sin(t * 0.7) * 9}% ${50 + Math.cos(t * 0.5 + k) * 9}%`;
  return (
    <div style={{ position: "relative", width: size, height: size, scale: `${pop}`, rotate: `${(1 - pop) * -30}deg` }}>
      <div style={{ position: "absolute", inset: 0, borderRadius: r(seed), background: col, boxShadow: `0 40px 80px ${col}` }} />
      <div style={{ position: "absolute", inset: size * 0.08, borderRadius: "50%", border: "6px dashed rgba(255,255,255,.85)", rotate: `${t * 20}deg` }} />
      {[0, 1, 2].map((k) => {
        const a = t * 0.8 + (k * Math.PI * 2) / 3 + seed, R = size * 0.56;
        return (
          <div key={k} style={{ position: "absolute", left: size / 2 + Math.cos(a) * R - 28, top: size / 2 + Math.sin(a) * R - 28, width: 56, height: 56, rotate: `${t * 60 + k * 40}deg` }}>
            <svg viewBox="0 0 200 200" style={{ width: "100%", height: "100%", overflow: "visible" }} fill="none" stroke={INK} strokeWidth={8} strokeLinecap="round" dangerouslySetInnerHTML={{ __html: DOODLES[(seed + k) % DOODLES.length] }} />
          </div>
        );
      })}
      <div style={{ position: "absolute", inset: size * 0.17, translate: `0px ${Math.sin(t * 1.8 + seed) * size * 0.025}px`, rotate: `${Math.sin(t * 1.2 + seed) * 5}deg`,
        filter: "drop-shadow(0 18px 20px rgba(40,30,60,.25))" }}><Icon name={ic} /></div>
    </div>
  );
};

// Big words: each word springs up in turn, with a marker bar that draws under the line
const Words: React.FC<{ text: string; age: number; size: number; align: "right" | "center"; color?: string; accent: string; maxWidth: number }> = ({ text, age, size, align, color = INKP, accent, maxWidth }) => {
  const { fps } = useVideoConfig();
  const words = text.split(" ");
  return (
    <div style={{ maxWidth, direction: "rtl", textAlign: align }}>
      <div style={{ display: "inline", fontFamily: "Changa", fontWeight: 800, fontSize: size, lineHeight: 1.3, color }}>
        {words.map((w, k) => {
          const sp = spring({ frame: age * fps - 6 - k * 3, fps, config: { damping: 12, stiffness: 150 } });
          return <span key={k} style={{ display: "inline-block", margin: "0 0.13em", translate: `0px ${(1 - sp) * 60}px`, opacity: Math.min(1, sp * 1.6) }} dangerouslySetInnerHTML={{ __html: sal(w) }} />;
        })}
      </div>
      <div style={{ height: 16, borderRadius: 8, background: accent, marginTop: 14, marginInlineStart: align === "center" ? "auto" : 0, marginInlineEnd: align === "center" ? "auto" : 0,
        width: `${interpolate(age, [0.35, 0.9], [0, Math.min(maxWidth, 520)], { ...clamp, easing: outExpo })}px` }} />
    </div>
  );
};

const fsFor = (s: string) => (s.length <= 12 ? 124 : s.length <= 20 ? 104 : s.length <= 30 ? 86 : 70);

const BeatShot: React.FC<{ b: Beat }> = ({ b }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const age = frame / fps, t = b.t0 + age, dur = b.t1 - b.t0;
  const bg = BG[b.n % BG.length], accent = ACC[b.col] ?? b.S.col;
  const trans = b.n % 4;
  const pin = interpolate(age, [0, 0.45], [0, 1], { ...clamp, easing: outExpo });
  const pout = interpolate(age, [dur - 0.05, dur + 0.3], [0, 1], { ...clamp, easing: inOut });
  const enter: React.CSSProperties =
    trans === 0 ? { translate: `${(1 - pin) * -1920 + pout * 1920}px 0px` }
      : trans === 1 ? { scale: `${0.7 + 0.3 * pin + pout * 0.2}`, opacity: Math.min(pin * 1.5, 1 - pout) }
        : trans === 2 ? { translate: `0px ${(1 - pin) * 1080 - pout * 200}px`, rotate: `${(1 - pin) * 6}deg`, opacity: 1 - pout }
          : { clipPath: `circle(${pin * 2300}px at ${b.n % 2 ? 1400 : 520}px 420px)`, opacity: 1 - pout };
  const lay = b.kind === "c" ? b.n % 5 : -1;
  const chip = (
    <div style={{ position: "absolute", right: 60, top: 92, direction: "rtl", fontFamily: "Changa", fontWeight: 800, fontSize: 30, color: INKP, background: "rgba(255,255,255,.85)",
      borderRadius: 999, padding: "4px 24px 8px", boxShadow: "0 8px 24px rgba(43,35,80,.1)", opacity: interpolate(age, [0.3, 0.6], [0, 1], clamp) }}
      dangerouslySetInnerHTML={{ __html: (b.S.num ? b.S.num + " · " : "") + sal(b.S.ar) }} />
  );
  let body: React.ReactNode = null;
  if (b.kind === "chapter") {
    body = (
      <AbsoluteFill style={{ background: `linear-gradient(135deg, ${b.S.col}, #fff6ea 75%)` }}>
        <div style={{ position: "absolute", left: 140, top: 150 }}><Illustration ic={b.ic} col="#ffffff" size={520} t={t} age={age} seed={b.si} /></div>
        <div style={{ position: "absolute", right: 120, top: 170, width: 1000, display: "flex", flexDirection: "column", alignItems: "flex-end", gap: 10 }}>
          {b.S.num ? <div style={{ fontFamily: "Changa", fontWeight: 800, fontSize: 170, lineHeight: 1, color: "#fff", WebkitTextStroke: `6px ${INKP}`, scale: `${spring({ frame: frame - 2, fps, config: { damping: 9 } })}` }}>{b.S.num}</div> : null}
          <Words text={b.S.ar} age={age} size={b.S.ar.length > 16 ? 96 : 120} align="right" accent={INKP} maxWidth={1000} />
          <div style={{ fontFamily: "Changa", fontWeight: 500, fontSize: 40, color: "#5d4f8f", direction: "ltr", opacity: interpolate(age, [0.5, 0.8], [0, 1], clamp) }}>{b.S.en}</div>
        </div>
      </AbsoluteFill>
    );
  } else if (b.kind === "q") {
    const len = b.text.length, fs = len <= 30 ? 84 : len <= 60 ? 68 : len <= 100 ? 56 : 46;
    body = (
      <AbsoluteFill style={{ background: bg }}>
        <div style={{ position: "absolute", left: 0, right: 0, top: 0, bottom: 0, opacity: 0.06, display: "flex", justifyContent: "center", alignItems: "center" }}>
          <div style={{ width: 900, height: 900, rotate: `${t * 4}deg` }}><Icon name="sparkle" /></div>
        </div>
        <div style={{ position: "absolute", left: 170, right: 170, top: 170, perspective: 1400 }}>
          <div style={{ borderRadius: 44, padding: 8, background: "linear-gradient(120deg,#ffb86b,#ff6fa3,#8b7bff,#3cc8c0)", boxShadow: "0 40px 90px rgba(80,50,120,.25)",
            rotate: `x ${interpolate(age, [0, 0.6], [50, 0], { ...clamp, easing: outExpo })}deg`, transformOrigin: "50% 0%" }}>
            <div style={{ borderRadius: 37, background: "#fffdf8", padding: "70px 80px 76px", textAlign: "center", direction: "rtl", fontFamily: "Amiri", fontWeight: 700, color: INKP, fontSize: fs, lineHeight: 1.85, rotate: `y ${Math.sin(t * 0.7) * 2.5}deg` }}
              dangerouslySetInnerHTML={{ __html: sal(b.text) }} />
          </div>
          <div style={{ position: "absolute", left: "50%", top: -64, width: 128, height: 128, marginLeft: -64, borderRadius: 40, background: "#fff", padding: 16, boxSizing: "border-box", boxShadow: "0 14px 30px rgba(43,35,80,.18)", rotate: `${Math.sin(t * 1.4) * 8}deg` }}>
            <Icon name={b.text.startsWith("﴿") ? "book" : "sparkle"} />
          </div>
        </div>
        {chip}
      </AbsoluteFill>
    );
  } else {
    const fs = fsFor(b.text);
    const ill = (size: number) => <Illustration ic={b.ic} col={b.S.col} size={size} t={t} age={age} seed={b.n} />;
    body = (
      <AbsoluteFill style={{ background: bg }}>
        <div style={{ position: "absolute", inset: -60, backgroundImage: "radial-gradient(rgba(40,30,60,.11) 2px, transparent 2.6px)", backgroundSize: "36px 36px", translate: `${(t * 6) % 36}px ${(t * 4) % 36}px` }} />
        {lay === 0 ? (<>
          <div style={{ position: "absolute", left: 170, top: 150 }}>{ill(520)}</div>
          <div style={{ position: "absolute", right: 110, top: 150, height: 520, width: 900, display: "flex", alignItems: "center", justifyContent: "flex-end" }}><Words text={b.text} age={age} size={fs} align="right" accent={accent} maxWidth={900} /></div>
        </>) : lay === 1 ? (<>
          <div style={{ position: "absolute", right: 170, top: 150 }}>{ill(520)}</div>
          <div style={{ position: "absolute", left: 110, top: 150, height: 520, width: 900, display: "flex", alignItems: "center", justifyContent: "flex-end" }}><Words text={b.text} age={age} size={fs} align="right" accent={accent} maxWidth={900} /></div>
        </>) : lay === 2 ? (<>
          <div style={{ position: "absolute", left: 960 - 190, top: 110 }}>{ill(380)}</div>
          <div style={{ position: "absolute", left: 120, right: 120, top: 520, display: "flex", justifyContent: "center" }}><Words text={b.text} age={age} size={Math.min(fs, 96)} align="center" accent={accent} maxWidth={1680} /></div>
        </>) : lay === 3 ? (<>
          <div style={{ position: "absolute", left: 0, top: 0, bottom: 0, width: 900, background: b.S.col, clipPath: "polygon(0 0, 100% 0, 82% 100%, 0 100%)" }} />
          <div style={{ position: "absolute", left: 150, top: 170 }}><Illustration ic={b.ic} col="#ffffff" size={480} t={t} age={age} seed={b.n} /></div>
          <div style={{ position: "absolute", right: 110, top: 150, height: 520, width: 860, display: "flex", alignItems: "center", justifyContent: "flex-end" }}><Words text={b.text} age={age} size={fs} align="right" accent={accent} maxWidth={860} /></div>
        </>) : (<>
          <div style={{ position: "absolute", left: 560, top: -40, width: 820, height: 820, opacity: 0.1, rotate: `${Math.sin(t * 0.5) * 8}deg` }}><Icon name={b.ic} /></div>
          <div style={{ position: "absolute", right: 120, top: 120 }}>{ill(240)}</div>
          <div style={{ position: "absolute", left: 120, right: 120, top: 240, height: 440, display: "flex", alignItems: "center", justifyContent: "center" }}><Words text={b.text} age={age} size={Math.round(fs * 1.12)} align="center" accent={accent} maxWidth={1680} /></div>
        </>)}
        {lay === 4 ? null : chip}
      </AbsoluteFill>
    );
  }
  return <AbsoluteFill style={enter}>{body}</AbsoluteFill>;
};

export const Beats: React.FC<{ data: VoxData }> = ({ data }) => {
  const { fps } = useVideoConfig();
  const f = (s: number) => Math.round(s * fps);
  const beats = useMemo(() => buildBeats(data.secs), [data.secs]);
  return (
    <AbsoluteFill style={{ background: "#fff8ef", color: INK }}>
      {beats.map((b, i) => (
        <Sequence key={i} name={`Beat ${i + 1}: ${b.kind}`} from={f(b.t0)} durationInFrames={Math.max(1, f(b.t1 - b.t0 + 0.35))} layout="absolute-fill">
          <BeatShot b={b} />
        </Sequence>
      ))}
      <TopBar data={data} />
      {data.caps.map((c, i) => (
        <Sequence key={`c${i}`} name={`Caption ${i + 1}`} from={f(c.a)} durationInFrames={Math.max(1, f(c.b - c.a))} layout="absolute-fill">
          <KCaption c={c} />
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
