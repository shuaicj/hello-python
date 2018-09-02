#!/usr/bin/env python3

from functools import partial

print("int('100') =", int('100'))
print("int('100', base=2) =", int('100', base=2))

int2 =  partial(int, base=2)
print("int2('100') =", int2('100'))

