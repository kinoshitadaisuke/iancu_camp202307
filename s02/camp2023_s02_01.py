#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/27 14:37:49 (CST) daisuke>
#

# importing numpy module
import numpy

# import matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'camp2023_s02_01.png'

# data for f(x) = 3 x - 20
fx = numpy.linspace (-10.0, +10.0, 10000)
fy = 3 * fx - 20

# data for g(x) = 3 x
gx = numpy.linspace (-10.0, +10.0, 10000)
gy = 3 * gx

# data for h(x) = 3 x + 20
hx = numpy.linspace (-10.0, +10.0, 10000)
hy = 3 * hx + 20

# making "fig", "canvas", and "ax" objects
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('$x$ [arbitrary unit]')
ax.set_ylabel ('$y$ [arbitrary unit]')

# range
ax.set_xlim (-10.0, +10.0)
ax.set_ylim (-50, +50)

# showing grid
ax.grid ()

# setting ticks
ax.set_xticks (numpy.linspace (-10.0, +10.0, 5))
ax.set_yticks (numpy.linspace (-50.0, +50.0, 11))

# plotting data
ax.plot (fx, fy, linestyle='-', linewidth=3, color='red', \
         label='$f(x) = 3x - 5$')
ax.plot (gx, gy, linestyle='--', linewidth=3, color='green', \
         label='$g(x) = 3x$')
ax.plot (hx, hy, linestyle=':', linewidth=3, color='blue', \
         label='$h(x) = 3x + 5$')

# making legend
ax.legend ()

# saving plot as a file
fig.savefig (file_output, dpi=225)
