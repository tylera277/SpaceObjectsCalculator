# Tyler Allen
# Newton-Rasphons Method of finding roots
# Trying to replicate Newton's Method


# M,e

def newton(M,e):

    import math
    NITER_MAX=300   # number of iterations for NR method
    niter = 1


    epsilon = 1*10**-5
    E=M
    while (niter < NITER_MAX):
        d = E - e * math.sin(E) - M  # the function you're evaluating

        if (math.fabs(d) < epsilon):
            return E
            break


        deltaE = d / (1 - e * math.cos(E))

        E = E - deltaE

        niter = niter + 1


