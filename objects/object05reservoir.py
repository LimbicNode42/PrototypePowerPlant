import numpy as np

from constants import Constants

class Reservoir:

    # Variables
    # Level 1
    diameter, height = [0.0 for _ in range(2)]
    curvature, capacity, pressure, level = [np.array([]) for _ in range(4)]
    # Level 2
    roughness, thickness, reynolds, coefficient = [0.0 for _ in range(4)]

    # Initialisation
    def __init__(self):


    # Functions
