#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/27 13:54:41 (CST) daisuke>
#

# importing numpy module
import numpy

# import matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'camp2023_s02_00.png'

# value of pi
pi = numpy.pi

# data for sine curve
data_x = numpy.linspace (-360.0, +360.0, 10000)
data_y = numpy.sin (data_x / 180.0 * pi)

# making "fig", "canvas", and "ax" objects
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('$x$ [deg]')
ax.set_ylabel ('$\sin (x)$')

# range
ax.set_xlim (-360.0, +360.0)
ax.set_ylim (-1.1, +1.1)

# showing grid
ax.grid ()

# setting ticks
ax.set_xticks (numpy.linspace (-360.0, +360.0, 9))
ax.set_yticks (numpy.linspace (-1.0, +1.0, 5))

# plotting data
ax.plot (data_x, data_y, linestyle='-', linewidth=3, color='blue', \
         label='$f(x) = sin (x)$')

# making legend
ax.legend ()

# saving plot as a file
fig.savefig (file_output, dpi=225)
