#!/usr/bin/env python3

import os

print(__file__)

print(os.path.abspath(__file__))

print(os.path.basename(__file__))

print(os.path.dirname(__file__))

print(os.path.split(__file__))

print(os.path.splitext(__file__))

print(os.path.exists(__file__))

print(os.path.getsize(__file__))

print(os.path.isdir(__file__))

print(os.path.join(os.path.dirname(__file__), 'shuaicj', 'python'))

print([d for d in os.listdir('.') if os.path.isdir(d)])

for root, dirs, files in os.walk('.'):
    print((root, dirs, files))
