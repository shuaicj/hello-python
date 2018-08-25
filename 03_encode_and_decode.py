#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("ord('A') =", ord('A'))
print("ord('中') =", ord('中'))

print()

print('chr(65) =', chr(65))
print('chr(20013) =', chr(20013))

print()

print("'ABC'.encode('utf-8') =", 'ABC'.encode('utf-8'))
print("'中文'.encode('utf-8') =", '中文'.encode('utf-8'))

print()

print("b'ABC'.decode('utf-8') =", b'ABC'.decode('utf-8'))
print(r"b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') =", b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print()

print("len('ABC') =", len('ABC'))
print("len('ABC'.encode('utf-8')) =", len('ABC'.encode('utf-8')))
print("len(b'ABC') =", len(b'ABC'))
print("len('中文') =", len('中文'))
print("len('中文'.encode('utf-8')) =", len('中文'.encode('utf-8')))
print(r"len(b'\xe4\xb8\xad\xe6\x96\x87') =", len(b'\xe4\xb8\xad\xe6\x96\x87'))

