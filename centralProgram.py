# Tyler Allen
# Date started : 03/13/2018
# Purpose: main program

from objectOrbitParameters import *  # to get orbital parameters
from orbitFunction import twodOrbitMaker
#import matplotlib.pyplot as plt  # for making the plots of the orbits

orbitingobject = input("Please enter outer object(all lowercase):")
parameter = objectParameters(orbitingobject)  # list which stores orbital parameters

massOrbitingBody = parameter[0]
semimajorAxis = parameter[1]
eccentricity = parameter[2]
I = parameter[3]  # no use for inclination yet



massCentralBody = 1.989*10**30  # assuming this is the sun

twodOrbitMaker(semimajorAxis, eccentricity, massOrbitingBody, massCentralBody)




