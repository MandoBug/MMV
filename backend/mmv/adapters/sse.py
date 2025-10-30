# this file provides a helper to stream JSON frames over Server-Sent Events (SSE)
# the frontend can connect using JavaScript's EventSource API to receive live updates

import json
import time
from flask import Response

def sse_stream(frame_iter, fps: int):
    """
    Convert a generator of frames (Python dicts) into an SSE stream response.
    
    frame_iter : callable that yields dict frames
    fps        : how many frames to send per second
    """
    interval = 1.0 / max(1, fps)

    def gen():
        for frame in frame_iter():
            # each SSE message is sent as 'data: <json>\n\n'
            yield f"data: {json.dumps(frame)}\n\n"
            time.sleep(interval)

    return Response(gen(), mimetype="text/event-stream")

# this file is just a utility for sending continuous data to the frontend
# inside is sse_stream(), which wraps a Python generator and streams JSON frames over HTTP
