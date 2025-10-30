# this file lets you grab one simulation frame (no streaming)
from flask import Blueprint, jsonify

def make_blueprint(engine):
    bp = Blueprint("snapshot", __name__)

    @bp.get("")
    def snap():
        return jsonify(engine.step())

    return bp

# this file is just for one-off simulation snapshots
# inside is a single route that returns a JSON frame from engine.step()
