#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' fib.py
    Provides n-th number in the Fibonacci sequence.
'''
___author___ = 'jontaylor224'


def fib(n):
    '''Given n, returns the n-th number in the Fibonacci sequence.

    Examples:

    >>> fib(10)
    34
    >>> fib(20)
    4181

    '''
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    import sys
    fib(sys.argv[1])
