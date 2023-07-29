#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/29 11:28:27 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy array
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg
import matplotlib.animation

# initialising a parser
desc   = 'creating plots'
parser = argparse.ArgumentParser (description=desc)

# adding arguments
parser.add_argument ('-i', '--input', default='test.data', \
                     help='input data file name')
parser.add_argument ('-o', '--output', default='test', \
                     help='output file prefix')
parser.add_argument ('-r', '--resolution', type=int, default=225, \
                     help='resolution of output file (default: 225 dpi)')

# parsing arguments
args = parser.parse_args ()

# parameters
file_input    = args.input
output_prefix = args.output
resolution    = args.resolution

# check of existence of input data file
path_input = pathlib.Path (file_input)
if not (path_input.exists ()):
    # printing message
    print (f'ERROR: data file "{file_input}" does not exist!')
    # stopping script
    sys.exit (0)

# making empty numpy arrays for storing data
array_t = numpy.array ([])
array_x = numpy.array ([])
array_y = numpy.array ([])
    
# opening data file for reading
with open (file_input, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # skipping line if line starts with '#'
        if (line[0] == '#'):
            fields = line.split ()
            if (len (fields) > 6):
                if (fields[1] == 'mass'):
                    Mstar = float (fields[6])
            if (len (fields) > 10):
                if (fields[7] == 'x0'):
                    x0 = float (fields[9])
                if (fields[7] == 'y0'):
                    y0 = float (fields[9])
                if (fields[7] == 'vx0'):
                    vx0 = float (fields[9])
                if (fields[7] == 'vy0'):
                    vy0 = float (fields[9])
            continue
        # splitting data
        (t_str, x_str, y_str) = line.split ()
        # converting string into float
        t = float (t_str)
        x = float (x_str)
        y = float (y_str)
        # appending data to numpy arrays
        array_t = numpy.append (array_t, t)
        array_x = numpy.append (array_x, x)
        array_y = numpy.append (array_y, y)

# finding minimum and maximum values of x and y values
x_min = numpy.min (array_x)
x_max = numpy.max (array_x)
y_min = numpy.min (array_y)
y_max = numpy.max (array_y)

# determining range to plot
list_minmax = [abs (x_min), abs (x_max), abs (y_min), abs (y_max)]
coord_max = sorted (list_minmax)[-1] * 1.1

# making plots
for i in range ( len (array_t) ):
    # output file name
    file_output = f'{output_prefix}_{i:08d}.png'
    
    #
    # plotting using Matplotlib
    #
    
    # making objects "fig" and "ax"
    fig    = matplotlib.figure.Figure ()
    canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
    ax     = fig.add_subplot (111)

    # axes
    ax.set_title ('Planetary Motion')
    ax.set_xlabel ('X [au]')
    ax.set_ylabel ('Y [au]')
    ax.set_xlim (coord_max * -1, coord_max)
    ax.set_ylim (coord_max * -1, coord_max)
    ax.set_aspect ('equal')

    # plotting a star
    ax.plot (0.0, 0.0, \
             linestyle='None', marker='o', markersize=10, \
             color='orange', label='star')

    # plotting a planet
    ax.plot (array_x[i], array_y[i], \
             linestyle='None', marker='o', markersize=5, \
             color='blue', label='planet')

    # labels
    text_time    = f"Time: %8.2f year" % (array_t[i])
    text_initial = f"Initial conditions"
    text_mass    = f"mass of star = {Mstar:5.2f} solar mass"
    text_iq      = f"(qx0, qy0) = ({x0:+5.2f} au, {y0:+5.2f} au)"
    text_iv      = f"(vx0, vy0) = ({vx0:+5.2f} au/yr, {vy0:+5.2f} au/yr)"
    ax.text (0.03, 0.95, text_time, transform=ax.transAxes)
    ax.text (0.03, 0.18, text_initial, transform=ax.transAxes)
    ax.text (0.05, 0.13, text_mass, transform=ax.transAxes)
    ax.text (0.05, 0.08, text_iq, transform=ax.transAxes)
    ax.text (0.05, 0.03, text_iv, transform=ax.transAxes)
    ax.legend ()

    # saving the figure to a file
    fig.savefig (file_output, dpi=resolution)
