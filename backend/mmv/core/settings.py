# this file defines MMV's default simulation settings
# it stores constants like number of particles, box size, and timestep
# other files will import this so they know what parameters to use

from dataclasses import dataclass
import os

@dataclass
class Settings:
    L: float = float(os.getenv("MMV_L", 1.0))      # box length (default 1.0)
    DT: float = float(os.getenv("MMV_DT", 1e-3))   # timestep for each update
    N: int = int(os.getenv("MMV_N", 800))          # number of molecules
    MASS: float = float(os.getenv("MMV_MASS", 1.0))
    KB: float = float(os.getenv("MMV_KB", 1.0))    # Boltzmann constant (sim units)
    FPS: int = int(os.getenv("MMV_FPS", 20))       # stream frames per second
    HIST_BINS: int = int(os.getenv("MMV_BINS", 40))# histogram resolution
    SEED: int | None = int(os.getenv("MMV_SEED", 0)) if os.getenv("MMV_SEED") else None

settings = Settings()  # create one global instance to import anywhere


# this file is just for configuration values used across the backend
# inside are only default simulation parameters that can be changed later by env vars