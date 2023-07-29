#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/07/28 21:35:58 (CST) daisuke>
#

# importing astropy module
import astropy.coordinates
import astropy.time
import astropy.units

# using "DE440" for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('de440')

# units
u_m = astropy.units.m

# time in UTC
t = astropy.time.Time ('2023-08-01T08:00:00', format='isot', scale='utc')

# location of observer: NCU main campus
longitude = '121d11m12s'
latitude  = '+24d58m12s'
height    = 151.6 * u_m
observer = astropy.coordinates.EarthLocation (longitude, latitude, height)

# getting position of the Sun
coord_sun = astropy.coordinates.get_body ('sun', t, location=observer)

# coordinate conversion
ecliptic     = astropy.coordinates.GeocentricMeanEcliptic (obstime=t)
sun_ecliptic = coord_sun.transform_to (ecliptic)

# printing position of the Sun
print (f'# position of the Sun at {t}')
print (f'RA     = {coord_sun.ra:10.6f}, Dec  = {coord_sun.dec:10.6f}')
print (f'lambda = {sun_ecliptic.lon:10.6f}, beta = {sun_ecliptic.lat:10.6f}')
