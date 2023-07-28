#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/07/28 14:59:06 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# constructing parser object
desc   = 'visualising data using Matplotlib'
parser = argparse.ArgumentParser (description=desc)

# adding arguments
parser.add_argument ('-c', default='red', \
                     help='colour of data points (default: red)')
parser.add_argument ('-m', default='o', \
                     help='marker type (default: o)')
parser.add_argument ('-r', type=float, default=225.0, \
                     help='resolution in DPI (default: 225)')
parser.add_argument ('-s', type=float, default=1, \
                     help='marker size (default: 1)')
parser.add_argument ('-i', default='input.data', \
                     help='input file name (default: input.data)')
parser.add_argument ('-o', default='output.png', \
                     help='output file name (default: output.png)')

# parsing arguments
args = parser.parse_args ()

# input parameters
colour      = args.c
markertype  = args.m
markersize  = args.s
resolution  = args.r
file_input  = args.i
file_output = args.o

# making pathlib objects
path_input  = pathlib.Path (file_input)
path_output = pathlib.Path (file_output)

# input file must exist
if not (path_input.exists ()):
    # printing message
    print (f'ERROR: input data file {file_input} does not exist!')
    # stopping script
    sys.exit (0)

# output file must be either EPS, PDF, PNG, or PS
if not ( (path_output.suffix == '.eps') \
         or (path_output.suffix == '.pdf') \
         or (path_output.suffix == '.png') \
         or (path_output.suffix == '.ps') ):
    # printing error message
    print (f'ERROR: output file must be either EPS, PDF, PNG, or PS!')
    # stopping script
    sys.exit (0)

# making empty numpy arrays
data_x = numpy.array ([])
data_y = numpy.array ([])

# opening file for reading
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # if line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # splitting line into "x" and "y"
        (x_str, y_str) = line.split ()
        # converting string into float
        try:
            # converting x_str into float
            x = float (x_str)
        except:
            # if fails, then stop the script
            print (f'ERROR: cannot convert "{x_str}" into float.')
            print (f'ERROR: something is wrong.')
            print (f'ERROR: exiting...')
            sys.exit (0)
        try:
            # converting y_str into float
            y = float (y_str)
        except:
            # if fails, then stop the script
            print (f'ERROR: cannot convert "{y_str}" into float.')
            print (f'ERROR: something is wrong.')
            print (f'ERROR: exiting...')
            sys.exit (0)
        # appending data into numpy arrays
        data_x = numpy.append (data_x, x)
        data_y = numpy.append (data_y, y)

# printing data
for i in range (len (data_x)):
    print (f'(x_{i:02d}, y_{i:02d}) = ({data_x[i]:8.3f}, {data_y[i]:8.3f})')

#
# making plot using Matplotlib
#
    
# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('X [arbitrary unit]')
ax.set_ylabel ('Y [arbitrary unit]')

# plotting data
ax.plot (data_x, data_y, linestyle='None', \
         marker=markertype, markersize=markersize, \
         color=colour, label=f'data in "{file_input}"')

# legend
ax.legend ()

# saving file
fig.savefig (file_output, dpi=resolution)
