#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/28 20:45:03 (CST) daisuke>
#

# importing astropy module
import astropy.coordinates
import astropy.units

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.degree

# coordinate of Vega
vega_ra  = '18:36:56.34'
vega_dec = '+38:47:01.3'

# constructing SkyCoord object
coord_vega = astropy.coordinates.SkyCoord (ra=vega_ra, dec=vega_dec, \
                                           unit=(u_ha, u_deg), \
                                           frame='icrs')

# coordinate in sexagesimal format
vega_str = coord_vega.to_string ('hmsdms')
(vega_ra_str, vega_dec_str) = vega_str.split ()

# printing coordinates of Vega
print (f'Coordinates of Vega:')
print (f' RA  = {vega_ra_str} = {coord_vega.ra.deg:10.6f} deg')
print (f' Dec = {vega_dec_str} = {coord_vega.dec.deg:10.6f} deg')
