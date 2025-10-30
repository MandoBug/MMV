# this file calculates statistics from the simulation state
# it handles speed magnitudes, temperature, energy histograms, and MB curves
# nothing updates positions here — it's purely for measurement & visualization

import numpy as np

def speeds(v: np.ndarray) -> np.ndarray:
    """Return the speed (magnitude of velocity) of each particle."""
    return np.linalg.norm(v, axis=1)

def temperature(v: np.ndarray, m: float = 1.0, kB: float = 1.0) -> float:
    """
    Compute temperature from particle velocities in 2D.
    For 2D, <½ m v²> = kT  →  T = <½ m v²> / k.
    """
    v2 = (v * v).sum(axis=1)
    mean_ke = 0.5 * m * v2.mean()
    return float(mean_ke / kB)

def histogram(speed: np.ndarray, bins: int, vmax: float):
    """Return histogram counts and bin edges for the speed data."""
    counts, edges = np.histogram(speed, bins=bins, range=(0, vmax))
    return counts, edges

def maxwell_boltzmann_2d(v: np.ndarray, T: float, m: float = 1.0, kB: float = 1.0) -> np.ndarray:
    """
    2D Maxwell–Boltzmann speed distribution (Rayleigh form):
    f(v) ∝ v * exp(-m v² / (2 kT))
    """
    a = m / (kB * T)
    return a * v * np.exp(-0.5 * a * v * v)

# this file is just for calculating measurable stats from the simulation
# inside are helper functions that return speeds, temperature, histograms, and MB distribution data
