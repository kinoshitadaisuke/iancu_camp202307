#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/28 19:44:50 (CST) daisuke>
#

# importing astropy module
import astropy.time

# date and time in UTC
t_str = '2023-08-01T08:00'

# making Astropy's Time object
t = astropy.time.Time (t_str, format='isot', scale='utc')

# calculating JD corresponding to time "t"
jd = t.jd

# printing result
print (f'{t} (UT) ==> JD {jd}')
