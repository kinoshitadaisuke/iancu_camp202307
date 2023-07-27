#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/27 18:39:40 (CST) daisuke>
#

# importing numpy module
import numpy

# import matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'camp2023_s02_05.png'

# mean and standard deviation of Gaussian distribution
mean   = 100.0
stddev = 10.0

# number of random number to be generated
n = 10**6

# generating random numbers
rng = numpy.random.default_rng ()
dist = rng.normal (loc=mean, scale=stddev, size=n)

# bins for histogram
bin_min   = 50.0
bin_max   = 150.0
bin_width = 2.0
bin_n     = int ( (bin_max - bin_min) / bin_width ) + 1
bins      = numpy.linspace (bin_min, bin_max, bin_n)

# making "fig", "canvas", and "ax" objects
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Value [arbitrary unit]')
ax.set_ylabel ('Number')

# showing grid
ax.grid ()

# plotting data
ax.hist (dist, bins=bins, histtype='bar', \
         edgecolor='black', linewidth=0.3, align='mid', \
         label='Gaussian distribution')

# making legend
ax.legend ()

# saving plot as a file
fig.savefig (file_output, dpi=225)
