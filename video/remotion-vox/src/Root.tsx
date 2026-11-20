import React from "react";
import { Composition, continueRender, delayRender } from "remotion";
import { Vox, VoxData } from "./Vox";
import { fontsReady } from "./fonts";
import data from "./data.json";

const handle = delayRender("Loading fonts");
fontsReady.then(() => continueRender(handle));

const D = data as unknown as VoxData;

export const RemotionRoot: React.FC = () => (
  <Composition id="RuqyahVox" component={Vox} durationInFrames={Math.ceil(D.dur * 30)} fps={30} width={1920} height={1080} defaultProps={{ data: D }} />
);
