#!/usr/bin/env python3

from enum import Enum, auto, unique

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)
print(isinstance(Color.RED, Color))
print(Color.RED is Color.BLUE)
print(Color.RED is not Color.BLUE)
print(Color.RED == Color.BLUE)
print(Color.RED != Color.BLUE)

for c in Color:
    print(c, end=' ')

print()

@unique
class Color2(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    # try BLUE = 2
