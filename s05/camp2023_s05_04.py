#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/28 18:35:36 (CST) daisuke>
#

# importing astropy module
import astropy.units

# sec
u_sec = astropy.units.second

# hr
u_hr = astropy.units.hour

# t_sec = 5000 sec
t_sec = 5000.0 * u_sec

# conversion of unit
t_hr = t_sec.to (u_hr)

# printing time "t_sec" and "t_hr"
print (f't = {t_sec.value} [{t_sec.unit}]')
print (f'  = {t_hr.value} [{t_hr.unit}]')
