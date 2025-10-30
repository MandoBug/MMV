# this file controls the main simulation logic for MMV
# it updates particle positions over time, handles wall bounces,
# and computes statistics like temperature and histograms each frame.

import numpy as np
from .state import SimState
from .physics import wall_bounce
from .stats import speeds, temperature, histogram, maxwell_boltzmann_2d

class SimulationEngine:
    """
    Core class that manages the molecular simulation.
    It owns the simulation state and updates it step-by-step.
    """

    def __init__(self, N, L, dt, m=1.0, kB=1.0, seed=None, bins=40):
        self.N, self.L, self.dt, self.m, self.kB, self.bins = N, L, dt, m, kB, bins
        self.rng = np.random.default_rng(seed)  # random number generator
        self._running = False                   # is the sim running?
        self.state = self._init_state()         # initial positions & velocities

    def _init_state(self) -> SimState:
        """Initialize positions uniformly and velocities from a normal distribution."""
        x = self.rng.uniform(0, self.L, size=(self.N, 2))
        v = self.rng.normal(0, 1, size=(self.N, 2))
        return SimState(x=x, v=v, t=0.0, L=self.L, m=self.m, kB=self.kB)

    # --- control methods ---
    def reset(self, seed=None):
        """Reinitialize the simulation (optionally with a new random seed)."""
        if seed is not None:
            self.rng = np.random.default_rng(seed)
        self.state = self._init_state()

    def start(self): self._running = True
    def pause(self): self._running = False

    # --- main simulation step ---
    def step(self, substeps=1) -> dict:
        """
        Advance the simulation forward by one frame (or more substeps).
        Returns a dictionary with histogram, MB curve, and summary stats.
        """
        s = self.state
        for _ in range(substeps):
            s.x += self.dt * s.v       # move particles
            wall_bounce(s.x, s.v, s.L) # reflect off walls
            s.t += self.dt             # increment time

        # --- compute physical stats for visualization ---
        spd = speeds(s.v)
        T = temperature(s.v, s.m, s.kB)
        vmax = max(1.0, np.percentile(spd, 99))  # upper limit for histogram

        counts, edges = histogram(spd, self.bins, vmax)
        v_line = np.linspace(0.0, vmax, 200)
        mb_pdf = maxwell_boltzmann_2d(v_line, T, s.m, s.kB)
        mb_pdf = mb_pdf / (mb_pdf.max() or 1.0)  # normalize for overlay

        return {
            "t": s.t,
            "temp": T,
            "energy": float(0.5 * s.m * float((s.v * s.v).sum())),
            "hist": {"counts": counts.tolist(), "bin_edges": edges.tolist()},
            "mb": {"v": v_line.tolist(), "pdf": mb_pdf.tolist()}
        }

# this file is the main simulation controller
# inside is the SimulationEngine class that updates positions, bounces particles,
# and calculates all the data the frontend needs to plot in real time
