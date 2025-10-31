# this file defines endpoints to start, pause, or reset the simulation
from flask import Blueprint, request

def make_blueprint(engine):
    bp = Blueprint("control", __name__)

    @bp.route("/start", methods=["POST", "GET"])
    def start():
        engine.start()
        return ("", 204)

    @bp.route("/pause", methods=["POST", "GET"])
    def pause():
        engine.pause()
        return ("", 204)

    @bp.route("/reset", methods=["POST", "GET"])
    def reset():
        seed = request.json.get("seed") if request.is_json else None
        engine.reset(seed)
        return ("", 204)

    return bp


# this file is just for simulation control routes
# inside are endpoints that call engine.start(), engine.pause(), and engine.reset()
