# Function which calculates orbital position of planetary objects
# condition where eccentricity is not 1 or extremely close to it


def twodOrbitMaker(semimajorAxis, eccentricity , massOrbitingObject, massCentralBody):


    import math
    import matplotlib.pyplot as plt

    from orbitModule import n, m, r, v, angF, T  # functions needed from orbitModule
    from newtonRasphons import newton  # iterating method needed

    a = semimajorAxis
    e = eccentricity
    mu = (massOrbitingObject + massCentralBody) * (6.67*10**-11)

    t = 0  # starting time for orbit
    steplength = 10000   # chunks of time being considered per run
                     # will most likely have to run at one second when actually calculating off these values


    period = T(a, mu)   # length of orbit (checked to be correct)

    radius = []  # empty lists which will be used later in program
    angle = []
    xPos = []
    yPos = []

    while t < period:
        N = n(a, mu)  # mean angular velocity
        M = m(t, N)  #
        E1 = newton(M, e)  #
        R = r(a, e, E1)
        V = v(mu, R, a)
        f = angF(a, e, R)
        if t > (period / 2.0):  # to bump the
            f = 6.28 - f

        radius.append(R)
        angle.append(f)

        xPos.append(R * math.cos(f))  # calculates the x & y position of body
        yPos.append(R * math.sin(f))


        t += steplength  # increases time by steplength amount

    xMax = max(xPos)
    yMax = max(yPos)

    plt.ylim(-1.1*yMax, 1.1*yMax )  # used to plot bodies on graph once run
    plt.xlim(-1.1*xMax, 1.1*xMax )
    plt.plot(0, 0, 'yo')
    plt.plot(xPos, yPos)
    plt.show()

# Functions which will calculate the distance from earth to object of consideration