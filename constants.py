import numpy as np

class Constants:

    # Gravity of Earth                                  m/s/s
    gravity     =   9.81

    # Pressure of atmosphere                            kPa
    atmos       =   101,325

    # Density of water                                  kg/m^3
    density     =   1.00

    # Viscosity of water                                kg/m/s
    viscosity   =   0.0091

    # Depth of point below sea level                    m
    depth       =   np.linspace(0, 100, 1001)

    # Hydrostatic Pressure of  water 
    # at various depths                                 kPa
    pressure   =   np.array([])
    for x in depth:
        # Formula used for hydrostatic is P = g * d * rho
        press = gravity * x * density
        pressure = np.append(pressure, [press])