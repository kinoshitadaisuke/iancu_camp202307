#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/27 15:29:04 (CST) daisuke>
#

# importing numpy module
import numpy

# import matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'camp2023_s02_02.png'

# value of pi
pi = numpy.pi

# value of standard acceleration of gravity in m/sec^2
g = 9.80665

# initial velocity in m/sec
v = 30.0

# initial launch angle in deg
theta_deg = 40.0

# time
t = numpy.linspace (0.0, 10.0, 51)

# (x, y) coordinate of a ball at given time t
x = v * numpy.cos (theta_deg / 180.0 * pi) * t
y = v * numpy.sin (theta_deg / 180.0 * pi) * t - 0.5 * g * t**2

# making "fig", "canvas", and "ax" objects
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('$x$ [m]')
ax.set_ylabel ('$y$ [m]')

# range
ax.set_xlim (0.0, +100.0)
ax.set_ylim (-10.0, +25)

# showing grid
ax.grid ()

# setting ticks
ax.set_xticks (numpy.linspace (0.0, +100.0, 11))
ax.set_yticks (numpy.linspace (-10.0, +25.0, 8))

# plotting data
ax.plot (x, y, linestyle='None', marker='o', markersize=5, \
         color='green', label='trajectory of a ball')

# making legend
ax.legend ()

# saving plot as a file
fig.savefig (file_output, dpi=225)
