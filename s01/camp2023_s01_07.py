#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/27 10:44:06 (CST) daisuke>
#

# name of file to read
file_input = 'stars.data'

# name of file to write
file_output = 'distance.data'

# making an empty dictionary for storing data
dic_star = {}

# opening file for reading
with open (file_input, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # if line stars with "#", then skip
        if (line[0] == '#'):
            continue
        # split line
        (name_str, mag_str, colour_str, parallax_str) = line.split (',')
        # stripping white spaces
        name = name_str.strip ()
        # converting string into float
        mag      = float (mag_str)
        colour   = float (colour_str)
        parallax = float (parallax_str)
        # calculation of distance
        dist_pc = 1.0 / (parallax * 0.001)
        # storing data in a dictionary
        dic_star[name]             = {}
        dic_star[name]['mag']      = mag
        dic_star[name]['colour']   = colour
        dic_star[name]['parallax'] = parallax
        dic_star[name]['distance'] = dist_pc
        
# opening file for writing
with open (file_output, 'w') as fh_out:
    # writing a header
    fh_out.write (f'# name, V-band app. mag, B-V colour index,' \
                  + f' parallax in mas, distance in pc\n')
    # for each star
    for star in dic_star.keys ():
        # writing data into a file
        fh_out.write (f'{star:20s}' \
                      + f' {dic_star[star]["mag"]:+5.2f}' \
                      + f' {dic_star[star]["colour"]:+5.2f}' \
                      + f' {dic_star[star]["parallax"]:7.2f}' \
                      + f' {dic_star[star]["distance"]:7.2f}\n')
