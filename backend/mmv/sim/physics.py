# this file defines the physical behavior of the particles
# for now, it only handles wall bounces (perfectly elastic reflections)
# later we can add particle–particle collisions here

import numpy as np

def wall_bounce(x: np.ndarray, v: np.ndarray, L: float) -> None:
    """
    Reflect particles that hit the walls of the box.

    x : (N, 2) array of positions
    v : (N, 2) array of velocities
    L : box length

    If a particle goes past 0 or L, we reflect its position
    and flip the sign of its velocity on that axis.
    """
    for axis in (0, 1):  # x- and y-axes
        # find particles beyond the right/top wall
        over = x[:, axis] > L
        if np.any(over):
            x[over, axis] = 2 * L - x[over, axis]
            v[over, axis] *= -1

        # find particles beyond the left/bottom wall
        under = x[:, axis] < 0
        if np.any(under):
            x[under, axis] = -x[under, axis]
            v[under, axis] *= -1

# this file is just the physics rules for the simulation
# inside is the wall_bounce() function which keeps molecules inside the box by flipping their velocity
