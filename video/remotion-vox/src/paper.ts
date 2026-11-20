// Deterministic helpers for the torn-paper look.
export const rng = (seed: number) => {
  let s = seed >>> 0 || 1;
  return () => (s = (s * 1664525 + 1013904223) >>> 0) / 4294967296;
};

export const torn = (r: () => number, amp = 4.2, nx = 16, ny = 5): string => {
  const p: [number, number][] = [];
  for (let i = 0; i <= nx; i++) p.push([(i / nx) * 100, r() * amp]);
  for (let i = 1; i < ny; i++) p.push([100 - r() * amp * 0.6, (i / ny) * 100]);
  for (let i = nx; i >= 0; i--) p.push([(i / nx) * 100, 100 - r() * amp]);
  for (let i = ny - 1; i > 0; i--) p.push([r() * amp * 0.6, (i / ny) * 100]);
  return "polygon(" + p.map(([x, y]) => `${x.toFixed(1)}% ${y.toFixed(1)}%`).join(",") + ")";
};

export const PAL: Record<string, string> = {
  y: "#f6d56a", p: "#f4a9b8", t: "#9fd3d6", g: "#a9d8a0", r: "#e0624f", w: "#fbf5e6", o: "#f5b88a", b: "#a9cdf0",
};

// Wraps ﷺ in Amiri so the ligature renders properly.
export const salHtml = (s: string) => s.replace(/ﷺ/g, '<span style="font-family:Amiri">ﷺ</span>');
