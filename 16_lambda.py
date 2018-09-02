#!/usr/bin/env python3

print(lambda x: x * x)

print(list(map(lambda x: x * x, [0, 1, 2])))

print(list(filter(lambda x: x % 2 == 0, [0, 1, 2])))

print(list(sorted(['A', 'b', 'C'])))
print(list(sorted(['A', 'b', 'C'], key=str.lower)))
print(list(sorted(['A', 'b', 'C'], key=lambda x: x.lower())))
