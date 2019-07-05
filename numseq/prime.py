#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' prime.py
    This module contains two methods:

    primes(n):  Returns a list of the prime numbers less than n.

    is_prime(m):  Returns a boolean indicating if m is a prime number.
'''
___author___ = 'jontaylor224'

import argparse
import math


def primes(n):
    ''' Returns a list of all prime numbers less than n.

    Examples:

    >>> primes(40)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    >>> primes(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    '''

    prime_nums = [2]
    for num in range(3, n, 2):
        if all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2)):
            prime_nums.append(num)
    return prime_nums


def is_prime(m):
    ''' Returns a boolean indicating if m is a prime number.

    Examples:

    >>> is_prime(7)
    True
    >>> is_prime(88)
    False
    '''
    if m == 2 or m == 3:
        return True
    if m % 2 == 0 or m % 3 == 0:
        return False

    limit = math.sqrt(m)
    i = 5
    w = 2

    while i <= limit:
        if m % i == 0:
            return False
        i += w
        w = 6 - w

    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--primes', help='return a list of all primes less than n')
    parser.add_argument('--isprime', help='return True if prime, False if not')

    args = parser.parse_args()

    if args.primes:
        primes(args.prime)
    elif args.isprime:
        is_prime(args.isprime)


if __name__ == '__main__':
    main()
