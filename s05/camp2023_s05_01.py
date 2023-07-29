#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/28 17:37:19 (CST) daisuke>
#

# importing astropy module
import astropy.constants

# solar mass
M_sun = astropy.constants.M_sun

# solar radius
R_sun = astropy.constants.R_sun

# printing 1 au and 1 pc in metre
print (f'1 M_sun = {M_sun.value} +/- {M_sun.uncertainty} [{M_sun.unit}]')
print (f'1 R_sun = {R_sun.value} +/- {R_sun.uncertainty} [{R_sun.unit}]')
