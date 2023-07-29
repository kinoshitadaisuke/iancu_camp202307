#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/28 20:00:21 (CST) daisuke>
#

# importing astropy module
import astropy.time

# J2000
t_j2000 = astropy.time.Time ('2000-01-01T12:00:00', format='isot', scale='utc')

# today
t_today = astropy.time.Time ('2023-08-01T12:00:00', format='isot', scale='utc')

# time difference between J2000 and today
delta_t = t_today - t_j2000

# printing result
print (f'{t_today} - {t_j2000} = {delta_t} days')
