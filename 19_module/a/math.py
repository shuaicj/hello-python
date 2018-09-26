#!/usr/bin/env python3

import m
from a.b import math as bmath

def add(x, y):
    print('a.math.add called')
    return bmath.add(x, y)

def sub(x, y):
    print('a.math.sub called')
    return m.math.sub(x, y)

