#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/28 18:46:53 (CST) daisuke>
#

# importing astropy module
import astropy.units

# GHz
u_GHz = astropy.units.GHz

# mm
u_mm = astropy.units.mm

# spectral
u_spectral = astropy.units.spectral ()

# frequency in GHz
f_GHz = 230.0 * u_GHz

# conversion of unit
wl_mm = f_GHz.to (u_mm, equivalencies=u_spectral)

# printing result
print (f'{f_GHz.value:5.1f} [{f_GHz.unit}]' \
       + f' ==> {wl_mm.value:5.3f} [{wl_mm.unit}]')
