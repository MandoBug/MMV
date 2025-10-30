# this file defines endpoints to start, pause, or reset the simulation
from flask import Blueprint, request

def make_blueprint(engine):
    bp = Blueprint("control", __name__)

    @bp.post("/start")
    def start():
        engine.start()
        return ("", 204)

    @bp.post("/pause")
    def pause():
        engine.pause()
        return ("", 204)

    @bp.post("/reset")
    def reset():
        seed = None
        if request.is_json:
            seed = request.json.get("seed")
        engine.reset(seed)
        return ("", 204)

    return bp

# this file is just for simulation control routes
# inside are endpoints that call engine.start(), engine.pause(), and engine.reset()
