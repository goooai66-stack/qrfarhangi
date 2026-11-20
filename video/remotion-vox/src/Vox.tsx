import React, { useMemo } from "react";
import { AbsoluteFill, Easing, interpolate, Sequence, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { Audio } from "@remotion/media";
import { ICONS, INK, star4 } from "./icons";
import { PAL, rng, salHtml, torn } from "./paper";

export type Cue = { a: number; b: number; ar: string; en: string; zh: string };
export type Item = [number, "c" | "q", string, string, string | null, number];
export type Sec = { a: number; b: number; num?: string; ar: string; en: string; col: string; ic: string; items: Item[] };
export type VoxData = { dur: number; voice: string; caps: Cue[]; secs: Sec[]; sfx: [number, string, number][] };

const W = 1920;
const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
const outBack = Easing.bezier(0.34, 1.56, 0.64, 1);
const outCubic = Easing.bezier(0.16, 1, 0.3, 1);

const Icon: React.FC<{ name: string; shadow?: number }> = ({ name, shadow = 5 }) => (
  <div style={{ width: "100%", height: "100%", filter: `drop-shadow(${shadow}px ${shadow + 3}px 0 rgba(29,26,22,.25))` }}>
    <svg viewBox="0 0 200 200" style={{ width: "100%", height: "100%", overflow: "visible" }} fill="none" stroke={INK} strokeWidth={7}
      strokeLinecap="round" strokeLinejoin="round" dangerouslySetInnerHTML={{ __html: ICONS[name] ?? "" }} />
  </div>
);

const shadow = { filter: "drop-shadow(4px 7px 0 rgba(29,26,22,.22))" };

// ---------- background: paper grain, halftone patches, drifting doodles, progress bar
const DOODLES: [number, number, number][] = [[120, 880, 0], [1790, 90, 1], [960, 760, 2], [1850, 760, 3], [60, 500, 1], [880, 40, 0], [1000, 480, 3], [760, 800, 2]];
const DOODLE_SVG = [star4(100, 100, 90, "#f6d56a"), `<circle cx="100" cy="100" r="60" fill="#e0624f"/>`,
  `<path d="M20,100 Q60,40 100,100 T180,100" stroke="#3aa0a8" stroke-width="16"/>`, `<path d="M100,20 L100,180 M20,100 L180,100" stroke="#e8607a" stroke-width="22"/>`];

const Paper: React.FC<{ dur: number }> = ({ dur }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  return (
    <AbsoluteFill style={{ background: "radial-gradient(ellipse at 50% 45%, rgba(0,0,0,0) 60%, rgba(120,80,30,.22) 100%), radial-gradient(ellipse at 22% 14%, rgba(255,255,255,.55), rgba(255,255,255,0) 45%), #efe6d2" }}>
      <svg width={1920} height={1080} style={{ position: "absolute", inset: 0, opacity: 0.5, mixBlendMode: "multiply" }}>
        <filter id="nf"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves={2} seed={4} /><feColorMatrix values="0 0 0 0 .45  0 0 0 0 .36  0 0 0 0 .25  0 0 0 .22 0" /></filter>
        <rect width={1920} height={1080} filter="url(#nf)" />
      </svg>
      <div style={{ position: "absolute", left: -140, top: -170, width: 700, height: 700, backgroundImage: "radial-gradient(#efa9b8 2.4px, transparent 2.9px)", backgroundSize: "17px 17px", WebkitMaskImage: "radial-gradient(circle at 30% 30%, #000 0, transparent 62%)" }} />
      <div style={{ position: "absolute", right: -160, top: 300, width: 700, height: 700, backgroundImage: "radial-gradient(#8fcfd3 2.4px, transparent 2.9px)", backgroundSize: "17px 17px", WebkitMaskImage: "radial-gradient(circle at 70% 50%, #000 0, transparent 60%)" }} />
      {DOODLES.map(([x, y, k], i) => (
        <div key={i} style={{ position: "absolute", left: x, top: y, width: 34 + (i % 3) * 10, height: 34 + (i % 3) * 10, opacity: 0.85,
          translate: `${Math.sin(t * 0.5 + i * 1.7) * 14}px ${Math.cos(t * 0.42 + i * 1.7) * 18}px`, rotate: `${(t * 12 + i * 68) % 360}deg` }}>
          <svg viewBox="0 0 200 200" style={{ width: "100%", height: "100%", overflow: "visible" }} fill="none" stroke={INK} strokeWidth={7} strokeLinecap="round" dangerouslySetInnerHTML={{ __html: DOODLE_SVG[k] }} />
        </div>
      ))}
      <div style={{ position: "absolute", left: 0, top: 0, height: 7, background: "#e0624f", width: interpolate(frame, [0, dur * fps], [0, W], clamp) }} />
    </AbsoluteFill>
  );
};

// ---------- one section: colour block, title, number sticker, big icon, chips and quote cards
type Placed = { kind: "c" | "q"; t0: number; t1: number; text: string; col: string; ic: string | null; y: number; rot: number; ph: number; clip: string; fs: number };

const layout = (S: Sec, si: number) => {
  const r = rng(100 + si * 31);
  const clips = { block: torn(r, 5, 18, 6), tape: torn(r, 8, 8, 2), tape2: torn(r, 8, 8, 2), title: torn(r, 6, 14, 4), sub: torn(r, 8, 12, 3) };
  const its = S.items.map(([t, kind, text, col, ic, g]) => ({ t, kind, text, col, ic, g }));
  const gs = [...new Set(its.map((i) => i.g))].sort((a, b) => a - b);
  const placed: Placed[] = [];
  gs.forEach((g, gi) => {
    const gItems = its.filter((i) => i.g === g).sort((a, b) => a.t - b.t);
    const gEnd = gi + 1 < gs.length ? Math.min(...its.filter((i) => i.g === gs[gi + 1]).map((i) => i.t)) : S.b;
    const gq = gItems.filter((i) => i.kind === "q");
    const lower = gq.length > 0;
    let slot = 0;
    gItems.forEach((it) => {
      if (it.kind === "q") {
        const nextQ = gq.find((q) => q.t > it.t);
        const len = it.text.length;
        placed.push({ kind: "q", t0: it.t, t1: nextQ ? nextQ.t : gEnd, text: it.text, col: "w", ic: null, y: 62, rot: -0.6 + r() * 1.2, ph: r() * 6,
          clip: torn(r, 2.6, 18, 6), fs: len <= 30 ? 70 : len <= 60 ? 58 : len <= 100 ? 48 : 42 });
      } else {
        const len = it.text.length;
        placed.push({ kind: "c", t0: it.t, t1: gEnd, text: it.text, col: it.col, ic: it.ic, y: lower ? 470 + slot * 96 : 70 + slot * 112,
          rot: -1.2 + r() * 2.4, ph: r() * 6, clip: torn(r, 6, 14, 4), fs: len > 36 ? 40 : len > 28 ? 46 : 52 });
        slot++;
      }
    });
  });
  return { clips, placed };
};

const SectionScene: React.FC<{ S: Sec; si: number }> = ({ S, si }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = S.a + frame / fps;
  const age = frame / fps;
  const { clips, placed } = useMemo(() => layout(S, si), [S, si]);
  const out = interpolate(t, [S.b, S.b + 0.3], [1, 0], clamp);
  const fs = S.ar.length > 20 ? 50 : S.ar.length > 13 ? 60 : 72;
  const pIcon = interpolate(age, [0.25, 0.8], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: 28, top: 262, width: 776, height: 500, ...shadow,
        translate: `${interpolate(age, [0, 0.5], [-900, 0], { ...clamp, easing: outCubic })}px 0px`, rotate: `${-1.4 + Math.sin(t * 0.9 + si) * 0.35}deg` }}>
        <div style={{ width: "100%", height: "100%", background: S.col, clipPath: clips.block }} />
      </div>
      <div style={{ position: "absolute", left: 70, top: 240, width: 150, height: 46, background: "rgba(246,213,106,.85)", rotate: "-6deg", clipPath: clips.tape, opacity: interpolate(age, [0.3, 0.45], [0, 1], clamp) }} />
      <div style={{ position: "absolute", left: 640, top: 740, width: 150, height: 46, background: "rgba(224,98,79,.8)", rotate: "5deg", clipPath: clips.tape2, opacity: interpolate(age, [0.4, 0.55], [0, 1], clamp) }} />
      <div style={{ position: "absolute", left: 195, top: 290, width: 440, height: 440, opacity: Math.min(1, pIcon * 4),
        translate: `0px ${Math.sin(t * 1.6 + si) * 8}px`,
        rotate: `${interpolate(age, [0.25, 0.8], [-14, 0], { ...clamp, easing: outBack }) + Math.sin(t * 1.1 + si) * 2.5}deg`,
        scale: interpolate(age, [0.25, 0.8], [0.15, 1], { ...clamp, easing: outBack }) }}>
        <Icon name={S.ic} />
      </div>
      <div style={{ position: "absolute", right: W - 800, top: 40, display: "flex", flexDirection: "column", alignItems: "flex-end", gap: 10, maxWidth: S.num ? 560 : 740,
        opacity: interpolate(age, [0, 0.15], [0, 1], clamp),
        translate: `0px ${interpolate(age, [0.05, 0.55], [-90, 0], { ...clamp, easing: outBack })}px` }}>
        <div style={shadow}>
          <div style={{ background: PAL.y, fontFamily: "'Reem Kufi', Cairo", fontWeight: 700, fontSize: fs, lineHeight: 1.25, textAlign: "right", direction: "rtl", clipPath: clips.title, padding: "14px 40px 18px" }}
            dangerouslySetInnerHTML={{ __html: salHtml(S.ar) }} />
        </div>
        <div style={shadow}>
          <div style={{ background: PAL.w, fontFamily: "Cairo", fontWeight: 700, fontSize: 28, direction: "ltr", textAlign: "right", clipPath: clips.sub, padding: "8px 26px 10px" }}>{S.en}</div>
        </div>
      </div>
      {S.num ? (
        <div style={{ position: "absolute", left: 36, top: 30, width: 200, height: 200, ...shadow, opacity: interpolate(age, [0, 0.12], [0, 1], clamp),
          scale: interpolate(age, [0.02, 0.52], [0.2, 1], { ...clamp, easing: outBack }),
          rotate: `${interpolate(age, [0.02, 0.52], [-20, -6], { ...clamp, easing: outBack }) + Math.sin(t * 1.3) * 2}deg` }}>
          <div style={{ position: "absolute", inset: 0, borderRadius: "50%", background: "#e0624f", display: "flex", alignItems: "center", justifyContent: "center", color: "#fff",
            fontFamily: "'Reem Kufi'", fontWeight: 700, fontSize: 150, lineHeight: 1, paddingBottom: 18, boxSizing: "border-box", border: "8px dashed rgba(255,255,255,.7)", outline: `7px solid ${INK}`, outlineOffset: -6 }}>{S.num}</div>
        </div>
      ) : null}
      {placed.map((p, i) => {
        if (t < p.t0 || t >= p.t1 + 0.25) return null;
        const o = Math.min(interpolate(t, [p.t0, p.t0 + 0.1], [0, 1], clamp), interpolate(t, [p.t1, p.t1 + 0.2], [1, 0], clamp));
        const common: React.CSSProperties = {
          position: "absolute", right: 60, top: p.y, opacity: o,
          translate: `${p.kind === "c" ? interpolate(t, [p.t0, p.t0 + 0.4], [90, 0], { ...clamp, easing: outCubic }) : 0}px 0px`,
          rotate: `${p.rot + Math.sin(t * 1.2 + p.ph) * 0.5}deg`,
          scale: interpolate(t, [p.t0, p.t0 + 0.4], [0.72, 1], { ...clamp, easing: outBack }),
        };
        if (p.kind === "q") {
          return (
            <div key={i} style={{ ...common, width: 1040, ...shadow }}>
              <div style={{ position: "relative", boxSizing: "border-box", padding: "42px 50px", textAlign: "center", direction: "rtl", fontFamily: "Amiri", fontWeight: 700, color: INK, background: "#fff8e4", fontSize: p.fs, lineHeight: 1.85, clipPath: p.clip }}>
                <span dangerouslySetInnerHTML={{ __html: salHtml(p.text) }} />
                <div style={{ position: "absolute", inset: 14, border: "3px dashed rgba(29,26,22,.55)" }} />
              </div>
            </div>
          );
        }
        return (
          <div key={i} style={{ ...common, display: "flex", flexDirection: "row", direction: "rtl", alignItems: "center", gap: 16 }}>
            {p.ic ? <div style={{ width: 92, height: 92, flex: "none" }}><Icon name={p.ic} shadow={3} /></div> : null}
            <div style={shadow}>
              <div style={{ display: "inline-block", padding: "15px 38px 17px", fontFamily: "Cairo", fontWeight: 800, lineHeight: 1.25, direction: "rtl", whiteSpace: "nowrap",
                background: PAL[p.col] ?? PAL.w, color: p.col === "r" ? "#fff" : INK, fontSize: p.fs, clipPath: p.clip }} dangerouslySetInnerHTML={{ __html: salHtml(p.text) }} />
            </div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

// ---------- trilingual caption card
const CAP_CLIP = torn(rng(5), 2.2, 22, 4);
const Caption: React.FC<{ c: Cue }> = ({ c }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const d = c.b - c.a;
  const t = frame / fps;
  const big = c.ar.length + c.en.length / 2.2 + c.zh.length * 1.4;
  const [fa, fe] = big > 260 ? [34, 21] : big > 200 ? [38, 23] : big > 150 ? [43, 25] : big > 110 ? [46, 27] : [50, 29];
  return (
    <div style={{ position: "absolute", left: 110, width: 1700, bottom: 24, ...shadow,
      opacity: Math.min(interpolate(t, [0, 0.12], [0, 1], clamp), interpolate(t, [d - 0.1, d], [1, 0], clamp)),
      translate: `0px ${interpolate(t, [0, 0.12], [14, 0], clamp)}px` }}>
      <div style={{ background: "#fbf5e6", padding: "20px 44px", textAlign: "center", clipPath: CAP_CLIP }}>
        <div style={{ fontFamily: "Cairo", fontWeight: 700, color: INK, direction: "rtl", lineHeight: 1.55, fontSize: fa }} dangerouslySetInnerHTML={{ __html: salHtml(c.ar) }} />
        <div style={{ fontFamily: "Cairo", fontWeight: 500, color: "#6b5a45", direction: "ltr", lineHeight: 1.35, marginTop: 4, fontSize: fe }}>{c.en}</div>
        <div style={{ fontFamily: "'Noto Sans SC'", fontWeight: 500, color: "#a8372b", direction: "ltr", lineHeight: 1.35, marginTop: 2, fontSize: fe }}>{c.zh}</div>
      </div>
    </div>
  );
};

export const Vox: React.FC<{ data: VoxData }> = ({ data }) => {
  const { fps } = useVideoConfig();
  const f = (s: number) => Math.round(s * fps);
  return (
    <AbsoluteFill style={{ fontFamily: "Cairo", color: INK }}>
      <Paper dur={data.dur} />
      {data.secs.map((S, si) => (
        <Sequence key={si} name={`Section ${si + 1}: ${S.en}`} from={f(S.a)} durationInFrames={f(S.b - S.a + 0.35)} layout="absolute-fill">
          <SectionScene S={S} si={si} />
        </Sequence>
      ))}
      {data.caps.map((c, i) => (
        <Sequence key={i} name={`Caption ${i + 1}`} from={f(c.a)} durationInFrames={Math.max(1, f(c.b - c.a))} layout="absolute-fill">
          <Caption c={c} />
        </Sequence>
      ))}
      <Audio src={staticFile(data.voice)} />
      {data.sfx.map(([t, name, vol], i) => (
        <Sequence key={`s${i}`} name={`SFX ${name}`} from={f(t)} durationInFrames={f(2)} layout="none">
          <Audio src={staticFile(`sfx/${name}.wav`)} volume={vol} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
