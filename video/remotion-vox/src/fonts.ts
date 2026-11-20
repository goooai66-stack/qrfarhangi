import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";

// Local fonts: Cairo (captions, chips), Reem Kufi (titles), Amiri (Qur'an / hadith cards, ﷺ), Noto Sans SC subset (Chinese captions)
export const fontsReady = Promise.all([
  loadFont({ family: "Cairo", url: staticFile("fonts/Cairo.ttf"), weight: "200 1000", format: "truetype" }),
  loadFont({ family: "Reem Kufi", url: staticFile("fonts/ReemKufi.ttf"), weight: "400 700", format: "truetype" }),
  loadFont({ family: "Amiri", url: staticFile("fonts/Amiri-Regular.woff"), weight: "400", format: "woff" }),
  loadFont({ family: "Amiri", url: staticFile("fonts/Amiri-Bold.woff"), weight: "700", format: "woff" }),
  loadFont({ family: "Noto Sans SC", url: staticFile("fonts/NotoSansSC-subset.woff2"), weight: "500", format: "woff2" }),
]);
