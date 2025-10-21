from flask import Flask, jsonify, request
from math import sqrt
import numpy as np

app = Flask(__name__)

# simple health check
@app.get("/api/health")
def health():
    return jsonify(status="ok")

# demo: compute a histogram of random speeds (placeholder for sim)
@app.post("/api/histogram")
def histogram():
    body = request.get_json(force=True) or {}
    n = int(body.get("n", 500))
    rng = np.random.default_rng(42)
    v = rng.rayleigh(scale=1.0, size=n)  # rough 2D speed-like
    hist, edges = np.histogram(v, bins=30, range=(0, v.max()))
    return jsonify(
        bins=hist.tolist(),
        edges=edges.tolist()
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
