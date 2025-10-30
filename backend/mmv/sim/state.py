# this file defines the structure of the simulation state
# it stores particle positions, velocities, time, and constants
# other files (like the physics and engine) will use this class

from dataclasses import dataclass
import numpy as np

@dataclass
class SimState:
    # particle positions (x, y) inside the box
    x: np.ndarray
    # particle velocities (vx, vy)
    v: np.ndarray
    # current simulation time
    t: float
    # simulation constants
    L: float   # box length
    m: float   # particle mass
    kB: float  # Boltzmann constant (simulation units)

# this file is just a data container for the molecules' positions, velocities, and constants
# inside is only the definition of SimState
# good for now