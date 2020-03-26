import numpy as np

from constants import Constants

class Intake:

    # Variables
    # Level 1
    diameter, length, portrusion, mass, flow = [0.0 for _ in range(5)]
    curvature, volume, velocity, pressure = [np.array([]) for _ in range(4)]
    # Level 2
    roughness, thickness, reynolds, coefficient, reduction = [0.0 for _ in range(5)]

    # Initialisation
    def __init__(self):


    # Functions
