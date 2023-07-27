#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/27 10:08:30 (CST) daisuke>
#

# name of file to read
file_input = 'stars.data'

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
        # printing result if distance is less than 20 pc
        if (dist_pc < 20.0):
            print (f'{name:20s} {mag:+5.2f} {colour:+5.2f} {parallax:6.2f}' \
                   + f' {dist_pc:4.1f}')
