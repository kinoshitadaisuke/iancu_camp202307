#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/28 18:04:50 (CST) daisuke>
#

# importing astropy module
import astropy.units

# unit of km
u_km = astropy.units.km

# unit of hr
u_hr = astropy.units.hr

# distance
d = 10.0 * u_km

# time
t = 2.5 * u_hr

# speed
v = d / t

# printing speed
print (f'v = {d} / {t}')
print (f'  = {v.value} [{v.unit}]')
