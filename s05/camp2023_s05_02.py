#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/28 17:56:53 (CST) daisuke>
#

# importing astropy module
import astropy.units

# sec
u_sec = astropy.units.second

# 1000 sec
t = 1000.0 * u_sec

# printing time "t"
print (f't = {t.value} [{t.unit}]')
