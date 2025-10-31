# this is the main entry point for the backend
# it creates the Flask app, enables CORS, initializes the simulation engine,
# and registers all the API routes (control, config, snapshot, stream)

from flask import Flask
from flask_cors import CORS

# import settings and simulation engine
from .mmv.core.settings import settings
from .mmv.sim.engine import SimulationEngine

# import the blueprints
from .mmv.api.control import make_blueprint as control_bp
from .mmv.api.config import make_blueprint as config_bp
from .mmv.api.snapshot import make_blueprint as snapshot_bp
from .mmv.api.stream import make_blueprint as stream_bp


def create_app():
    """App factory — sets up the MMV backend."""
    app = Flask(__name__)

    # enable CORS for frontend requests (React/Vite)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # create a single simulation engine instance
    engine = SimulationEngine(
        N=settings.N,
        L=settings.L,
        dt=settings.DT,
        m=settings.MASS,
        kB=settings.KB,
        seed=settings.SEED,
        bins=settings.HIST_BINS,
    )
    engine.start()

    # register all API blueprints with their routes
    app.register_blueprint(config_bp(engine),  url_prefix="/api/config")
    app.register_blueprint(control_bp(engine), url_prefix="/api/control")
    app.register_blueprint(snapshot_bp(engine),url_prefix="/api/snapshot")
    app.register_blueprint(stream_bp(engine, settings.FPS), url_prefix="/api/stream")

    # small root route for quick sanity check
    @app.get("/")
    def root():
        return {"status": "ok", "message": "MMV backend is running"}

    return app


# run in dev mode with:
# flask --app backend.app:create_app --debug run

# this file is the main startup point for the backend
# inside it, we build the Flask app, attach all API routes, and start the simulation engine
