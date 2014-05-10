# -*- coding: utf-8 -*-
# Tarmo Tanilsoo, 2013

from math import sin, cos, sqrt, atan2, asin, pi, floor, degrees as r2d, radians as d2r
def parsecoords(lat,lon):
    la="N"
    if lat < 0: la="S"
    lo="E"
    if lon < 0: lo="W"
    lat=abs(lat)
    lon=abs(lon)
    la_d=int(lat)
    lo_d=int(lon)
    la_m=int((lat-la_d)*60)
    lo_m=int((lon-lo_d)*60)
    la_s=int((((lat-la_d)*60)-la_m)*60)
    lo_s=int((((lon-lo_d)*60)-lo_m)*60)
    string="%d°%d'%d\" %s, %d°%d'%d\" %s" % (la_d, la_m, la_s, la, lo_d, lo_m, lo_s, lo)
    return string
def beamheight(GR,alpha):
    r=6371.0 #Earth radius
    a=d2r(alpha) #Antenna angle in radians
    R=GR/cos(a)
    return R*sin(a)+(R**2)/(2*1.21*r) #WSR-88D height
def beamangle(h,R):
    r=6371.0 #Earth radius
    return r2d(asin(h/R-R/(2*1.21*r)))
def geocoords(azrange,rlat,rlon,zoomlevel):
    R=6371.0
    az=d2r(azrange[0]) #Azimuth in radians
    r=azrange[1]
    rlat=d2r(rlat) #To radians
    lat=asin(sin(rlat)*cos(r/R)+cos(rlat)*sin(r/R)*cos(az))
    lon=rlon+r2d(atan2(sin(az)*sin(r/R)*cos(rlat),cos(r/R)-sin(rlat)*sin(lat)))
    return round(r2d(lat),5),round(lon,5)
def az_range(x,y,zoomlevel):
    angle=180-r2d(atan2(x,y))
    r=sqrt(x**2+y**2)/zoomlevel
    return angle, r
def getcoords(angle,r,zoom=1,center=[1000,1000]):
    ''' Get coords '''
    x=(sin(angle)*r)*zoom
    y=-(cos(angle)*r)*zoom
    return (x+center[0],y+center[1])

def geog2polar(plat,plong,rlat,rlong):
    '''Usage: geog2polar(place latitude, place longitude, radar latitude, radar longitude)'''
    #Distance
    R = 6371
    dLat = d2r(plat-rlat)
    dLon = d2r(plong-rlong)
    plat=d2r(plat) #To radians - radiaanidesse
    rlat=d2r(rlat) #To radians - radiaanidesse
    a = sin(0.5*dLat)**2+cos(rlat)*cos(plat)*sin(0.5*dLon)**2
    c = 2*atan2(sqrt(a),sqrt(1-a))
    d = R*c
    #Bearing
    y = sin(dLon)*cos(plat)
    x = cos(rlat)*sin(plat)-sin(rlat)*cos(plat)*cos(dLon)
    suund = atan2(y,x)
    return d, suund
