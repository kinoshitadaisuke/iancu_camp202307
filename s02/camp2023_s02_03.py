#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/27 16:30:12 (CST) daisuke>
#

# importing numpy module
import numpy

# import matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file name
file_input = 'planets.data'

# output file name
file_output = 'camp2023_s02_03.png'

# making empty lists
list_a = []
list_P = []

# opening file for reading
with open (file_input, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # if line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # splitting line into name, semimajor axis, and orbital period
        (name, a_str, P_str) = line.split ()
        # converting string into float
        a = float (a_str)
        P = float (P_str)
        # appending data to list
        list_a.append (a)
        list_P.append (P)

# making "fig", "canvas", and "ax" objects
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Semimajor Axis [au]')
ax.set_ylabel ('Orbital Period [day]')

# logarithmic scale
ax.set_xscale ('log')
ax.set_yscale ('log')

# range
ax.set_xlim (0.1, 100)
ax.set_ylim (10, 10**5)

# showing grid
ax.grid ()

# plotting data
ax.plot (list_a, list_P, linestyle='None', marker='s', markersize=5, \
         color='red', label='planets in solar system')

# making legend
ax.legend ()

# saving plot as a file
fig.savefig (file_output, dpi=225)
