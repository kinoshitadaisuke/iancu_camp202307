#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/28 20:15:21 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.time
import astropy.units

# location of Lulin Observatory
longitude = '120d52m21.5s'
latitude  = '+23d28m10s'

# Time object
t = astropy.time.Time ('2023-08-01T14:00:00', format='isot', scale='utc', \
                       location=(longitude, latitude))

# calculation of local sidereal time
lst = t.sidereal_time ('apparent')

# printing result
print (f'# local sidereal time at Lulin Observatory')
print (f'#  longitude = {longitude}')
print (f'#  latitude  = {latitude}')
print (f'#  time      = {t}')
print (f'LST = {lst}')
