#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/26 20:29:24 (CST) daisuke>
#

# importing math module
import math

# value of pi
pi = math.pi

# angle in degree
a_deg = 30.0

# angle in radian
a_rad = a_deg / 180.0 * pi

# calculation of sin (30 deg)
sin_a = math.sin (a_rad)

# printing result of calculation
print (f'{a_deg} deg = {a_rad} rad')
print (f'sin ({a_deg} deg) = {sin_a}')
