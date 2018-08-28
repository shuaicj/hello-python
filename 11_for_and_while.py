#!/usr/bin/env python3

for n in [1, 2, 3, 4, 5]:
    print(n, end=' ')

print()

for n in range(1, 6):
    print(n, end=' ')

print()

n = 0
while True:
    n += 1
    if n > 5:
        break
    print(n, end=' ')

print()

fruits = ['apple', 'banana', 'pear']

for fruit in fruits:
    print(fruit, end=' ')

print()

for i in range(len(fruits)):
    print(i, fruits[i], sep=':', end=' ')

print()

for i, fruit in enumerate(fruits):
    print(i, fruit, sep=':', end=' ')

print()

for n1, n2, n3 in zip([11, 12, 13], [21, 22, 23], [31, 32, 33]):
    print(n1, n2, n3, sep=',', end=' ')

print()

for nn in zip([11, 12, 13], [21, 22, 23], [31, 32, 33]):
    print(nn, end=' ')

print()

d = {'a': 1, 'b': 2, 'c': 3}

for k in d:
    print(k, d[k], sep=':', end=' ')

print()

for k in d.keys():
    print(k, d[k], sep=':', end=' ')

print()

for v in d.values():
    print(v, end=' ')

print()

for k, v in d.items():
    print(k, v, sep=':', end=' ')

print()

for p in d.items():
    print(p, end=' ')

print()

