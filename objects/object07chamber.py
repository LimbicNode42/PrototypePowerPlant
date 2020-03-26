import numpy as np

from constants import Constants

class Chamber:

    # Variables
    # Level 1
    diameter, height = [0.0 for _ in range(2)]
    capacity, level, pressure = [np.array([]) for _ in range(3)]
    # Level 2
    roughness, thickness, reynolds, coefficient = [0.0 for _ in range(4)]

    # Initialisation
    def __init__(self):


    # Functions
