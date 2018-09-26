#!/usr/bin/env python3

print(x * x for x in range(3))

print(sum(x * x for x in range(3)))

for x in (x * x for x in range(3)):
    print(x, end=' ')

print()

def g():
    yield 'A'
    yield 'B'
    yield 'C'

print(g())

for x in g():
    print(x, end=' ')

print()
