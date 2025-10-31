// API wrapper for the MMV backend
// provides: openStream(onFrame), start(), pause(), reset(seed?), getSnapshot()

import { url } from "./config";

export function openStream(onFrame: (frame: any) => void) {
  // Server-Sent Events connection to /api/stream
  const es = new EventSource(url("/api/stream"));
  es.onmessage = (e) => {
    try {
      onFrame(JSON.parse(e.data));
    } catch {
      /* ignore malformed frames */
    }
  };
  return () => es.close(); // caller should call this to clean up
}

export const start = () =>
  fetch(url("/api/control/start"), { method: "POST" });

export const pause = () =>
  fetch(url("/api/control/pause"), { method: "POST" });

export const reset = (seed?: number) =>
  fetch(url("/api/control/reset"), {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(seed != null ? { seed } : {}),
  });

export const getSnapshot = () =>
  fetch(url("/api/snapshot")).then((r) => r.json());

/*
purpose: API helper layer for MMV
- openStream(): subscribes to the backend SSE stream and forwards parsed frames
- start/pause/reset(): control the simulation via POST routes
- getSnapshot(): fetch one frame (handy for debug or initial load)

this file is just thin wrappers over the backend endpoints.
inside we keep all fetch/EventSource details in one place for reuse.
*/
