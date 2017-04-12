#!/usr/bin/env python
# -*- coding: utf-8 -*-


# filter
def f(x):
    return x % 3 == 0 or x % 5 == 0

print filter(f, range(2, 25))


# map
def cube(x):
    return x*x*x

print map(cube, range(1, 11))


def add(x, y):
    return x + y

seq = range(8)
print map(add, seq, seq)

# reduce
print reduce(add, range(1, 11))     # add(add(add(add(add(add(1, 2), 3), 4), 5), 6), 7) ...


def sum1(seq1):
    def add2(x, y):
        return x + y
    return reduce(add2, seq1, 0)    # 0 indicates the starting value

print sum1(range(1, 11))


# list comprehensions 列表推导式
squares = []
for x in range(10):
    squares.append(x**2)
print squares

new_squares = [x**2 for x in range(10)]
print new_squares

print [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print [num for elem in vec for num in elem]

# contain complex expressions and nested functions
from math import pi
print [str(round(pi, i)) for i in range(1, 6)]

# nested list comprehensions
import pprint

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
    ]
pprint.pprint([[row[i] for row in matrix] for i in range(4)])

# zip function
print zip(*matrix)
