# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 14:00:34 2014

@author: Theema
program for Early Earthquake warning system

"""

import math, datetime

def geoDistance(lat1, long1, lat2,long2 ):
    """caluclate geographical distance from
    two latitude, longtitude coordinates based on Haversine formula"""    
    R = 6371 #km
    #degrees negative indicates south/west    
    rLat1 = math.radians(lat1)
    rLong1 = math.radians(long1)
    rLat2 = math.radians(lat2)
    rLong2 = math.radians(long2)
    
    changeLat = rLat1 - rLat2
    changeLong = rLong1 - rLong2
    
    a = math.sin(changeLat/2)**2+math.cos(rLat1)*math.cos(rLat2)*math.sin(changeLong/2)**2
    c = 2*math.atan2(a**0.5,(1-a)**0.5)
    d = R*c 
    return(d)

#testing with fake coordinates
vp = 8#km/s primary wave
vs = 3.45#km/s secondary wave
distanceEtoU= geoDistance( -38.38, 177.5,-43.56,172.56)#distance from user to epicentre

#calculate from third furthest seismogram
tp = datetime.time(21,17,55)#fake time
ts = datetime.time(21,18,12)#fake time
print(ts)
changeTime = ts-tp 
disCovered = (changeTime*vp*vs)/(vp-vs)

disFuture = distanceEtoU-disCovered
timeArrive = disFuture/vp #time in second distance in km, time for wave P to arrive 
