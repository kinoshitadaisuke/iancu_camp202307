#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/27 17:08:20 (CST) daisuke>
#

# importing numpy module
import numpy

# import matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file name
file_input = 'sunspot.data'

# output file name
file_output = 'camp2023_s02_04.png'

# making empty numpy arrays
array_date    = numpy.array ([], dtype='datetime64')
array_sunspot = numpy.array ([], dtype='int')

# opening file for reading
with open (file_input, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # if line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # splitting line into date and sunspot number
        (date, n_str) = line.split ()
        # converting string into float
        n = int (n_str)
        # appending data to numpy array
        array_date    = numpy.append (array_date, numpy.datetime64 (date))
        array_sunspot = numpy.append (array_sunspot, n)

# making "fig", "canvas", and "ax" objects
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Year')
ax.set_ylabel ('Number of sunspots')

# range
ax.set_ylim (0, 600)

# showing grid
ax.grid ()

# plotting data
ax.plot (array_date, array_sunspot, linestyle='-', linewidth=1, \
         color='orange', label='Number of sunspots')

# making legend
ax.legend ()

# saving plot as a file
fig.savefig (file_output, dpi=225)
