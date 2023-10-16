#!/usr/bin/env python

# Script that reads a CSV file with two columns and performs a regression on the data.
# The first column are the x values and the second column are the y values.
# The following command line arguments are required:
#   -i <input_
#   -r <regression_type>
# The regression types are:
#   - linear
#   - quadratic
#   - cubic
# The regression model output is written to standard output.
# The command line arguments are handled with the argparse module.
# The regression is performed using the scipy module.

import argparse
import numpy as np
from scipy import optimize
from scipy import stats

# define a function that, given the data and the estimated function,
# returns the r-squared value
def r_squared(data, func, popt):
    residuals = data[:,1] - func(data[:,0], *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((data[:,1] - np.mean(data[:,1]))**2)
    return 1 - (ss_res / ss_tot)

# Parse the command line arguments
parser = argparse.ArgumentParser(description='Perform a regression on a CSV file with two columns.')
parser.add_argument('-i', '--input', help='Input CSV file', required=True)
parser.add_argument('-r', '--regression', help='Regression type', required=True,
        choices=['linear', 'quadratic', 'cubic'])
args = parser.parse_args()

# Read the CSV file
data = np.genfromtxt(args.input, delimiter=',')
x = data[:,0]
y = data[:,1]

# Perform the regression
if args.regression == 'linear':
    def func(x, a, b):
        return a + b*x
elif args.regression == 'quadratic':
    def func(x, a, b, c):
        return a + b*x + c*x**2
elif args.regression == 'cubic':
    def func(x, a, b, c, d):
        return a + b*x + c*x**2 + d*x**3

popt, pcov = optimize.curve_fit(func, x, y)

# Print the function
if args.regression == 'linear':
    print(f'y = {popt[0]} + {popt[1]} * x')
elif args.regression == 'quadratic':
    print(f'y = {popt[0]} + {popt[1]} * x + {popt[2]} * x^2')
elif args.regression == 'cubic':
    print(f'y = {popt[0]} + {popt[1]} * x + {popt[2]} * x^2 + {popt[3]} * x^3')

# Compute R^2
print(f'R^2 = {r_squared(data, func, popt)}')
