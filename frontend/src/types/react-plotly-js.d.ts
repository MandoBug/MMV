declare module 'react-plotly.js' {
  import * as React from 'react';
  import { Layout, Config, Data } from 'plotly.js';

  export interface PlotParams {
    data: Data[];
    layout?: Partial<Layout>;
    config?: Partial<Config>;
    style?: React.CSSProperties;
    className?: string;
    onInitialized?: (figure: { data: Data[]; layout: Partial<Layout> }) => void;
    onUpdate?: (figure: { data: Data[]; layout: Partial<Layout> }) => void;
    useResizeHandler?: boolean;
    divId?: string;
  }

  const Plot: React.FC<PlotParams>;
  export default Plot;
}
