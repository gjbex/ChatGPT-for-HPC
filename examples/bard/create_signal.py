#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import numpy as np
import sys

def main():
    arg_parser = argparse.ArgumentParser(description='Create a signal')
    arg_parser.add_argument('--nr-samples', type=int, default=1000,
                            help='number of samples')
    arg_parser.add_argument('--max-time', type=float, default=1.0,
                            help='maximum time')
    arg_parser.add_argument('--freq', nargs='*', type=float,
                            help='frequencies of the signals')
    arg_parser.add_argument('--amp', nargs='*', type=float,
                            help='amplitudes of the signals')
    arg_parser.add_argument('--phase', nargs='*', type=float,
                            help='phases of the signals')
    arg_parser.add_argument('--output', type=str, default='signal.png',
                            help='output file')
    options = arg_parser.parse_args()

    if options.freq is None:
        options.freq = [1.0]
    if options.amp is None:
        options.amp = [1.0]
    if options.phase is None:
        options.phase = [0.0]

    if len(options.freq) != len(options.amp) or \
         len(options.freq) != len(options.phase):
        raise ValueError('Number of frequencies, amplitudes and phases must be equal')

    t = np.linspace(0.0, options.max_time, options.nr_samples)
    y = np.zeros_like(t)
    for f, a, phi in zip(options.freq, options.amp, options.phase):
        y += a * np.sin(2.0*np.pi*f*t + phi)

    plt.plot(t, y)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.savefig(options.output)

if __name__ == '__main__':
    try:    
        main()
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
