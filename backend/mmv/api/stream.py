# this file streams live simulation frames to the frontend
# it uses the sse_stream() function to continuously send JSON data

from flask import Blueprint
from ..adapters.sse import sse_stream

def make_blueprint(engine, fps: int):
    bp = Blueprint("stream", __name__)

    @bp.get("")
    def stream():
        def frames():
            while True:
                if engine._running:
                    yield engine.step()
                else:
                    # send minimal heartbeat so frontend knows connection is alive
                    yield {"t": engine.state.t}
        return sse_stream(frames, fps=fps)

    return bp

# this file is just for live streaming the simulation
# inside is the /stream endpoint that sends continuous frame data to the frontend
