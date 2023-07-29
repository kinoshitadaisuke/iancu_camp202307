#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/28 20:55:42 (CST) daisuke>
#

# importing astropy module
import astropy.coordinates
import astropy.units

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.degree

# coordinate of Antares
antares_ra = '16:29:24.46'
antares_dec = '-26:25:55.2'

# constructing SkyCoord object
coord_antares = astropy.coordinates.SkyCoord (ra=antares_ra, dec=antares_dec, \
                                              unit=(u_ha, u_deg), \
                                              frame='icrs')

# coordinate in hh:mm:ss and dd:mm:ss format
antares_str = coord_antares.to_string ('hmsdms')
(antares_ra_str, antares_dec_str) = antares_str.split ()

# coordinate conversion
antares_l = coord_antares.galactic.l
antares_b = coord_antares.galactic.b

# printing coordinates of Antares
print (f'Coordinates of Antares in equatorial coordinate system:')
print (f' RA  = {antares_ra_str} = {coord_antares.ra.deg:10.6f} deg')
print (f' Dec = {antares_dec_str} = {coord_antares.dec.deg:10.6f} deg')
print (f'Coordinates of Antares in galactic coordinate system:')
print (f' l   = {antares_l:10.6f}')
print (f' b   = {antares_b:10.6f}')
