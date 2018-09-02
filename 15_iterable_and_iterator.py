#!/usr/bin/env python3

from collections.abc import Iterable, Iterator

def g():
    yield 'A'
    yield 'B'
    yield 'C'

print('isinstance([], Iterable) =', isinstance([], Iterable))
print('isinstance({}, Iterable) =', isinstance({}, Iterable))
print("isinstance('abc', Iterable) =", isinstance('abc', Iterable))
print('isinstance((x for x in range(3)), Iterable) =', isinstance((x for x in range(3)), Iterable))
print('isinstance(g(), Iterable) =', isinstance(g(), Iterable))

print()

print('isinstance([], Iterator) =', isinstance([], Iterator))
print('isinstance({}, Iterator) =', isinstance({}, Iterator))
print("isinstance('abc', Iterator) =", isinstance('abc', Iterator))
print('isinstance((x for x in range(3)), Iterator) =', isinstance((x for x in range(3)), Iterator))
print('isinstance(g(), Iterator) =', isinstance(g(), Iterator))

print()

print('isinstance(iter([]), Iterator) =', isinstance(iter([]), Iterator))
print('isinstance(iter({}), Iterator) =', isinstance(iter({}), Iterator))

