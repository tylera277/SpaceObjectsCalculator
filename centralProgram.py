# Tyler Allen
# Date started : 03/13/2018
# Most recent data : 3/18/2018
# Purpose: main program

from objectOrbitParameters import *  # to get orbital parameters
from orbitFunction import twodOrbitMaker
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from DateConvertedToSeconds import dateConverter
from distanceEarth2Object import distance
import math


#  Below this is used to plot earth's orbit
#  it'll be used each run, so needs to be permanently available
#  (I may come back and make this prettier at some point, not high-priority right now)


#print("Enter your time in military")  # get the time the user is interested in
minute = input("Minute:")
hour = input("Hour:")
day = input("Day of month:")
month = input("Current Month:")
year = input("Current year:")


dateInSeconds = dateConverter(minute,hour,day,month,year)


centerobject = "earth"
parameterEarth = objectParameters(centerobject)  # list which stores orbital parameters

massOrbitingBody = parameterEarth[0]  # unpacking list full of parameters
semimajorAxis = parameterEarth[1]
eccentricity = parameterEarth[2]
inclination = parameterEarth[3]
longOfAscNode = parameterEarth[4]
argPeriapsis = parameterEarth[5]

massCentralBody = 1.989*10**30  # assuming this is the sun

nag1, xEarthLast, yEarthLast, zEarthLast, xEarthPosition, yEarthPosition, zEarthPosition  = twodOrbitMaker(semimajorAxis, eccentricity, massOrbitingBody, massCentralBody, inclination, longOfAscNode, argPeriapsis, dateInSeconds)



############################################################################################################
#  Below this is used to calculate the orbit of user-requested object  #


orbitingobject = input("Please enter orbiting object(lower case pls):")
parameterObject = objectParameters(orbitingobject)  # list which stores orbital parameters

massOrbitingBody = parameterObject[0]  # unpacking list full of parameters
semimajorAxis = parameterObject[1]
eccentricity = parameterObject[2]
inclination = parameterObject[3]
longOfAscNode = parameterObject[4]
argPeriapsis = parameterObject[5]

nag2, xObjectLast, yObjectLast, zObjectLast, xObjectPosition, yObjectPosition, zObjectPosition  = twodOrbitMaker(semimajorAxis, eccentricity, massOrbitingBody, massCentralBody, inclination, longOfAscNode, argPeriapsis, dateInSeconds)


length = distance(xEarthLast,yEarthLast,zEarthLast,xObjectLast,yObjectLast,zObjectLast)


deltaX = xObjectLast
deltaY = yObjectLast
deltaZ = zObjectLast

distance = math.sqrt(deltaX**2 + deltaY**2 + deltaZ**2)
print("distance=",distance/(10**9))


ec= math.radians(23.439292)
Xq = deltaX
Yq = (deltaY * math.cos(ec)) - (deltaZ * math.sin(ec))
Zq = (deltaY * math.sin(ec)) + (deltaZ * math.cos(ec))



fancyE = Xq - xEarthLast
















fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(0, 0, 0, 'yo')  # plot a dot (!) for the sun
ax.scatter(xEarthPosition[nag1 - 1], yEarthPosition[nag1 - 1], zEarthPosition[nag1 - 1], 'yo')
                                # plots the dot on last coordinate point in list of earth
ax.scatter(xEarthPosition, yEarthPosition, zEarthPosition, s=1)
                                # plots the last calculated pos. of earth

ax.scatter(xObjectPosition[nag2 - 1], yObjectPosition[nag2 - 1], zObjectPosition[nag2 - 1], 'yo')
                                # plots the dot on last coordinate point in list of object
ax.scatter(xObjectPosition, yObjectPosition, zObjectPosition, s=1)
                                # plots the last calculated pos. of the object
plt.show()



