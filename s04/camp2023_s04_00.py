#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/28 14:51:02 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing scipy module
import scipy.stats

# constructing parser object
desc   = 'generating a synthetic data for a straight line'
parser = argparse.ArgumentParser (description=desc)

# adding arguments
parser.add_argument ('-a', type=float, default=1.0, \
                     help='slope of straight line (default: 1.0)')
parser.add_argument ('-b', type=float, default=0.0, \
                     help='y-intercept of straight line (default: 0.0)')
parser.add_argument ('-n', type=int, default=11, \
                     help='number of data points to generate (default: 11)')
parser.add_argument ('-s', type=float, default=0.5, \
                     help='stddev of noise (default: 1.0)')
parser.add_argument ('-x0', type=float, default=0.0, \
                     help='start of x value (default: 0.0)')
parser.add_argument ('-x1', type=float, default=10.0, \
                     help='end of x value (default: 10.0)')
parser.add_argument ('-o', default='sample.data', \
                     help='output file name (default: sample.data)')

# parsing arguments
args = parser.parse_args ()

# input parameters
a           = args.a
b           = args.b
n           = args.n
stddev      = args.s
x0          = args.x0
x1          = args.x1
file_output = args.o

# making pathlib object
path_output = pathlib.Path (file_output)

# existence check of output file
if (path_output.exists ()):
    # printing message
    print (f'ERROR: file "{file_output}" exists!')
    # stop the script
    sys.exit (0)

# function for a line
def line (x, a, b):
    # line
    y = a * x + b
    # returning y
    return y

# synthetic data for least-squares method
data_x = numpy.linspace (x0, x1, n)
data_y = line (data_x, a, b)

# generating random numbers
err = scipy.stats.norm.rvs (loc=0.0, scale=stddev, size=n)

# adding errors to y values
data_y += err

# opening file for writing
with open (file_output, 'w') as fh:
    # writing header
    fh.write (f'#\n')
    fh.write (f'# synthetic data\n')
    fh.write (f'#\n')
    fh.write (f'#  input parameters\n')
    fh.write (f'#   a           = {a}\n')
    fh.write (f'#   b           = {b}\n')
    fh.write (f'#   n           = {n}\n')
    fh.write (f'#   s           = {stddev}\n')
    fh.write (f'#   x0          = {x0}\n')
    fh.write (f'#   x1          = {x1}\n')
    fh.write (f'#   output file = {file_output}\n')
    fh.write (f'#\n')
    # for each x and y
    for i in range (len (data_x)):
        # writing generated synthetic data into file
        fh.write (f'{data_x[i]:8.3f}    {data_y[i]:8.3f}\n')
