# Function which calculates orbital position of planetary objects
# condition where eccentricity is not 1 or extremely close to it


def twodOrbitMaker(semimajorAxis, eccentricity , massOrbitingObject, massCentralBody, inclination, longOfAscNode, argPeriapsis,dateInSeconds):


    import math

    from orbitModule import n, m, r, v, angF, T  # functions needed from orbitModule
    from newtonRasphons import newton  # iterating method needed

    a = semimajorAxis
    e = eccentricity
    mu = (massOrbitingObject + massCentralBody) * (6.67*10**-11)
    i = inclination
    OM = longOfAscNode
    W = argPeriapsis

    t = 0  # starting time for orbit
    steplength = 100000   # chunks of time being considered per run
                     # will most likely have to run at one second when actually calculating off these values


    period = T(a, mu)   # length of orbit (checked to be correct)

    if (dateInSeconds > period):
        runTime = dateInSeconds % period
    elif (dateInSeconds <= period):
        runTime = period




    radius = []  # empty lists which will be used later in program
    angle = []
    xPos = []
    yPos = []
    zPos = []

    while t < runTime:
        N = n(a, mu)  # mean angular velocity
        M = m(t, N)  #
        E1 = newton(M, e)  #
        R = r(a, e, E1)
        V = v(mu, R, a)
        f = angF(a, e, R)
        if t > (period / 2.0):  # to get a full period
            f = 6.28 - f

        radius.append(R)
        angle.append(f)
                                                                # calculates the x & y & z position of body
        xPos.append(R * (math.cos(OM)*math.cos(W+f) - math.sin(OM)*math.sin(W+f)*math.cos(i)))
        yPos.append(R * (math.sin(OM)*math.cos(W+f) + math.cos(OM)*math.sin(W+f)*math.cos(i)))
        zPos.append(R * math.sin(W+f) * math.sin(i))




        t += steplength  # increases time by steplength amount


    nag = len(xPos)
    xLast = xPos[len(xPos)-1]  # used to mark the last coordinates of the objects path
    yLast = yPos[len(yPos)-1]
    zLast = zPos[len(zPos)-1]

    return nag,xLast, yLast, zLast, xPos, yPos, zPos

