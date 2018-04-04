import math


def T(a,mu):  # to calculate period of orbit of body
    part1 = ((a**3.0)/mu)**(1.0/2.0)
    T = 2 * 3.14159265359 * part1
    return T

def n(a,mu):  # to calculate n for orbiting body
    N = mu**(1.0/2.0) * a**(-3.0/2.0)
    return N

def m(t, n):  #
    M = n * t
    return M


def r(a, e, E1):
    r = a - a*e*math.cos(E1)
    return r

def v(mu, r, a):
    part1 = (2*mu)/r - (mu)/a
    v = math.sqrt(part1)
    return v

def angF(a, e, r):
    part1 = a -(a*e**2) - r
    part2 = e*r
    part3 =(part1/part2)
    if part3 >1.0:             # a bit of shimmying to get this to work; cosf was equal to a value greater than 1
        part3 =part3 - 0.005
    Phi = math.acos(part3)
    return Phi



