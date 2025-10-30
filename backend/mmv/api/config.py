# this file handles reading and updating the simulation configuration
from flask import Blueprint, jsonify, request

def make_blueprint(engine):
    bp = Blueprint("config", __name__)

    @bp.get("")
    def get_cfg():
        return jsonify({
            "N": engine.N,
            "L": engine.L,
            "dt": engine.dt,
            "bins": engine.bins
        })

    @bp.put("")
    def put_cfg():
        data = request.get_json() or {}
        engine.N = int(data.get("N", engine.N))
        engine.L = float(data.get("L", engine.L))
        engine.dt = float(data.get("dt", engine.dt))
        engine.bins = int(data.get("bins", engine.bins))
        engine.reset()
        return ("", 204)

    return bp

# this file is just for simulation configuration routes
# inside are endpoints to get or change settings like N, L, dt, and histogram bins
