import React from "react";
import { Composition, continueRender, delayRender } from "remotion";
import { Vox, VoxData } from "./Vox";
import { Kinetic } from "./Kinetic";
import { Beats } from "./Beats";
import { fontsReady } from "./fonts";
import data from "./data.json";
import dataKinetic from "./data-kinetic.json";
import dataBeats from "./data-beats.json";

const handle = delayRender("Loading fonts");
fontsReady.then(() => continueRender(handle));

const D = data as unknown as VoxData;
const K = dataKinetic as unknown as VoxData;
const B = dataBeats as unknown as VoxData;

export const RemotionRoot: React.FC = () => (
  <>
    <Composition id="RuqyahVox" component={Vox} durationInFrames={Math.ceil(D.dur * 30)} fps={30} width={1920} height={1080} defaultProps={{ data: D }} />
    <Composition id="RuqyahKinetic" component={Kinetic} durationInFrames={Math.ceil(K.dur * 30)} fps={30} width={1920} height={1080} defaultProps={{ data: K }} />
    <Composition id="RuqyahBeats" component={Beats} durationInFrames={Math.ceil(B.dur * 30)} fps={30} width={1920} height={1080} defaultProps={{ data: B }} />
  </>
);
