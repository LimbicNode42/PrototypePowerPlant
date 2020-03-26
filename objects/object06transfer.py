import numpy as np

from constants import Constants

class Transfer:

    # Variables
    # Level 1
    diameter, height, flow = [0.0 for _ in range(3)]
    curvature, volume, pressure, level = [np.array([]) for _ in range(4)]
    # Level 2
    roughness, thickness, reynolds, coefficient, reduction = [0.0 for _ in range(5)]

    # Initialisation
    def __init__(self):


    # Functions
