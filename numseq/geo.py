#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' geo.py
    This module contains three methods:

    square(n):  Returns the square(n^2) of n.

    triangle(n):  Returns the "triangle" of n, which
    is the sum of (1 + 2 + ... n - 1 + n).

    cube(n):  Returns the cube(n^3) of n.
'''
___author___ = 'jontaylor224'

import argparse


def square(n):
    '''Given n, returns the square(n^2) of n.

    Examples:

    >>> square(3)
    9
    >>> square(9)
    81

    '''
    return n**2


def triangle(n):
    '''Given n, returns the triangle of n.
    The triangle of a number is the sum of (n + n-1 + n-2 ... + 2 + 1)

    1:  *   triangle(1) gives 1

    2:  *   triangle(2) gives 3
        **

    3:  *   triangle(3) gives 6
        **
        ***

    6:  *   triangle(6) gives 21
        **
        ***
        ****
        *****
        ******

    Examples:

    >>> triangle(3)
    6
    >>> triangle(9)
    45

    '''
    return sum(range(n))


def cube(n):
    '''Given n, returns the cube (n^3) of n.

    Examples:

    >>> cube(3)
    27
    >>> cube(9)
    729
    '''
    return n**3


def main():
    ''' Provides the square, triangle or cube of a given number'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--square', help='return the square of a number')
    parser.add_argument('--triangle', help='return the triangle of a number')
    parser.add_argument('--cube', help='return the cube of a number')

    args = parser.parse_args()

    if args.square:
        square(args.square)
    elif args.triangle:
        triangle(args.triangle)
    elif args.cube:
        cube(args.cube)


if __name__ == '__main__':
    main()
