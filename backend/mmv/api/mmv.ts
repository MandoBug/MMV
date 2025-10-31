export function openMMVStream(onFrame: (f: any) => void) {
  const es = new EventSource("http://127.0.0.1:5000/api/stream");
  es.onmessage = (e) => onFrame(JSON.parse(e.data));
  return () => es.close();
}

export const start  = () => fetch("http://127.0.0.1:5000/api/control/start", { method: "POST" });
export const pause  = () => fetch("http://127.0.0.1:5000/api/control/pause", { method: "POST" });
export const reset  = (seed?: number) =>
  fetch("http://127.0.0.1:5000/api/control/reset", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(seed!=null ? { seed } : {})
  });
