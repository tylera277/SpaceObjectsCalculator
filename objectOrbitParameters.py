# function that sets certain parameters to the values...
# of a particular object the user has selected

def objectParameters(object):
    import math

    if (object == 'mercury'):
        massBody = 0.0  # mass of this object (kg)
        a = 0.0  # semi-major axis (m)
        e = 0.0  # eccentricity
        I = 0.0  # angle of inclination relative to ecliptic plane (degrees)
        OM = 0.0  # longitude of the ascending node (degrees)
        W = 0.0  # argument of the periapsis (degrees)
    elif (object == 'venus'):
        massBody = 4.8675*10**24
        a = 108.21*10**9
        e = 0.00677672
        I = 3.39
        OM = 76.628
        W = 54.737
    elif (object == 'earth'):
        massBody = 5.972*10**24
        a = 149.60*10**9
        e = 0.01671123
        I = 0.0
        OM = 0.00  # earths orbit is reference frame
        W = 0.0
    elif (object == 'mars'):
        massBody = 6.4185*10**23
        a = 227.9*10**9
        e = 0.0933941
        I = 1.850
        OM = 49.5087
        W = 286.606
    elif (object == 'jupiter'):
        massBody = 1898.19*10**24
        a = 778.231*10**9
        e = 0.04838859
        I = 1.304
        OM = 100.5214
        W = 273.788
    elif (object == 'saturn'):
        massBody = 568.34*10**24
        a = 1433.53*10**9
        e = 0.05386179
        I = 2.485
        OM = 113.619
        W = 340.028
    elif (object == 'uranus'):
        massBody = 86.813*10**24
        a = 2872.46*10**9
        e = 0.04725744
        I = 0.772
        OM = 74.049
        W = 99.459
    elif (object == 'neptune'):
        massBody = 102.413*10**24
        a = 4495.06*10**9
        e = 0.00859048
        I = 1.769
        OM = 131.708
        W = 266.266
    elif (object == 'pluto'):
        massBody = 0.01303*10**24
        a = 5906.38*10**9
        e = 0.2488273
        I = 17.16
        OM = 110.210
        W = 114.228
    elif (object == 'halleys'):  # halley's comet; didn't work in my system
        massBody = 2.2*10**14
        a = 2.667928*10**9
        e = 0.96714
        I = 162.2
                                                            # thank you god for this radians working
    return massBody, a, e, math.radians(I), math.radians(OM), math.radians(W)
