#!/usr/bin/env python

# Script to generate a data set consisting of x and y values.
# The x values are nearly equidistantly spaced, but with some
# random noise added. The y values are calculated from the
# x values using a function with some random noise added.
# The function is a quadratic function.
# The noise level for the x and y values are given as command line
# arguments.  The third argument is the name of the file to save the
# plot of the data to.  The command line arguments are processed using the
# argparse module.

import argparse
import matplotlib.pyplot as plt
import numpy as np

# Parse command line arguments
parser = argparse.ArgumentParser(description='Generate a data set.')
parser.add_argument('--x_noise',  type=float, default=0.0, 
        help='noise level for x values')
parser.add_argument('--y_noise', type=float, default=0.0,
        help='noise level for y values')
parser.add_argument('--output', type=argparse.FileType('wb'), required=True,
        help='output file')
parser.add_argument('--seed', type=int, default=1234, help='random seed')
parser.add_argument('--num_points', type=int, default=100, help='number of points')
parser.add_argument('--show_values', action='store_true', help='show values on standard output')
args = parser.parse_args()

# Function to calculate y values from x values
def f(x):
    return 1.0 + 2.0*x + 3.0*x**2

# Generate data set
x = np.linspace(0.0, 20.0, args.num_points)
y = f(x)

# Add noise to x and y values
np.random.seed(args.seed)
x += args.x_noise * np.random.randn(len(x))
y += args.y_noise * np.random.randn(len(y))

# Print data set if requested
if args.show_values:
    for x_value, y_value in zip(x, y):
        print(f'{x_value},{y_value}')

# Plot data set
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.savefig(args.output.name)
