import numpy as np

class Constants:

    # Gravity of Earth                                  m/s^2
    gravity     =   9.81

    # Pressure of atmosphere                            kPa
    atmos       =   101,325

    # Density of distilled and salt water               kg/m^3
    unsalted    =   1.00
    salted      =   1.025

    # Depth of point below sea level                    m
    depth       =   np.linspace(0, 100, 1001)

    # Hydrostatic Pressure of both distilled and
    # salted water at various depths                    kPa
    Punsalted   =   np.array([])
    Psalted     =   np.array([])
    for x in depth:
        # Formula used for hydrostatic is P = g * d * rho
        lessDense = gravity * x * unsalted
        moreDense = gravity * x * salted
        Punsalted = np.append(Punsalted,[lessDense])
        Psalted   = np.append(Psalted,[moreDense])