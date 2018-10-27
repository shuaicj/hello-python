#!/usr/bin/env python3

import itertools

print(list(itertools.repeat('X', 4)))

print(list(itertools.takewhile(lambda x: x < 4, [1, 2, 3, 4, 5])))

print(list(itertools.dropwhile(lambda x: x < 4, [1, 2, 3, 4, 5])))

print(list(itertools.chain('ABC', 'DEF')))

print(list(itertools.chain.from_iterable(['ABC', 'DEF'])))

print(list(itertools.islice('ABCDEFG', 2)))
print(list(itertools.islice('ABCDEFG', 2, 4)))
print(list(itertools.islice('ABCDEFG', 2, None)))
print(list(itertools.islice('ABCDEFG', 0, None, 2)))
