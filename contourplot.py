#!/usr/bin/env python

import sys
import math


def GSlocation():
	lat = 34
	lon = -93
	return (lat, lon)

def EarthRadiusAtGS(lat):
	r1 = 6378.137 #km - radius of earth at equator
	r2 = 6356.752 #km - radius of earth at pole
	R = math.sqrt( ( (r1**2 * math.cos(lat))**2 + (r2**2 * math.sin(lat))**2 ) / ( (r1 * math.cos(lat))**2 + (r2 * math.sin(lat))**2 )  )
	return R

def GetArcLength(theta,altitude):
	# Solve the equation:
	# Re*sin(phi) + Re*tan(theta)*cos(phi) = (altitude + Re)*tan(theta)
	Re = EarthRadiusAtGS(GSlocation()[0])
	
	arclength = (math.pi/180) * Re * ( 90 - theta - ((180/math.pi)*(math.acos( ((Re + altitude)*math.sin(theta*math.pi/180))/ Re))) )
	
	return arclength



def main(theta, altitude):
	#theta = 15 #degrees
	#altitude = 600 #km

	print "Arc length for angle theta =", (theta), " and altitude =", (altitude), "km:"
	print (GetArcLength(theta, altitude))

if __name__== "__main__":
	theta = float(sys.argv[1])
	altitude = float(sys.argv[2])
	main(theta, altitude)