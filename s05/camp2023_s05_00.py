#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/28 17:32:34 (CST) daisuke>
#

# importing astropy module
import astropy.constants

# astronomical unit
au = astropy.constants.au

# parsec
pc = astropy.constants.pc

# printing information about constants au and pc
print (f'astronomical unit:')
print (au)
print (f'parsec:')
print (pc)

# printing 1 au and 1 pc in metre
print (f'1 au = {au.value} [{au.unit}]')
print (f'1 pc = {pc.value} [{pc.unit}]')
