# function that sets certain parameters to the values...
# of a particular object the user has selected

def objectParameters(object):

    if (object == 'mercury'):
        massBody = 0.0  # mass of this object (kg)
        a = 0.0  # semi-major axis (m)
        e = 0.0  # eccentricity
        I = 0.0  # angle of inclination relative to ecliptic plane (degrees)
    elif (object == 'venus'):
        massBody = 4.8675*10**24
        a = 108.21*10**9
        e = 0.00677672
        I = 3.39
    elif (object == 'earth'):
        massBody = 5.972*10**24
        a = 149.60*10**9
        e = 0.01671123
        I = 0.00
    elif (object == 'mars'):
        massBody = 6.4185*10**23
        a = 227.9*10**9
        e = 0.0933941
        I = 1.850
    elif (object == 'jupiter'):
        massBody = 1898.19*10**24
        a = 778.57*10**9
        e = 0.04838624
        I = 1.304
    elif (object == 'saturn'):
        massBody = 568.34*10**24
        a = 1433.53*10**9
        e = 0.05386179
        I = 2.485
    elif (object == 'uranus'):
        massBody = 86.813*10**24
        a = 2872.46*10**9
        e = 0.04725744
        I = 0.772
    elif (object == 'neptune'):
        massBody = 102.413*10**24
        a = 4495.06*10**9
        e = 0.00859048
        I = 1.769
    elif (object == 'pluto'):
        massBody = 0.01303*10**24
        a = 5906.38*10**9
        e = 0.2488273
        I = 17.16
    elif (object == 'halleys'):  # halley's comet; didn't work
        massBody = 2.2*10**14
        a = 2.667928*10**9
        e = 0.96714
        I = 162.2

    return massBody, a, e, I
