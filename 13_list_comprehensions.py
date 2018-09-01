#!/usr/bin/env python3

print([x for x in range(10)])

print([x * x for x in range(10)])

print([x * x for x in range(10) if x % 2 == 0])

print([x + y for x in 'ABC' for y in '123'])

print([x + y for x in 'ABC' for y in '123' if x <= 'B' and y <= '2'])

print([k + v + x for k, v in {'A': '1', 'B': '2'}.items() for x in 'mn'])
