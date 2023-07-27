#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/27 09:55:45 (CST) daisuke>
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
        # if magnitude is brighter than 0.00, then print the data
        if (mag < 0.00):
            print (f'{name:20s} {mag:+5.2f} {colour:+5.2f} {parallax:6.2f}')
