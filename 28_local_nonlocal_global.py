#!/usr/bin/env python3

x = 'I am global'

def f():
    x = 'I am nonlocal'
    def test_local():
        x = 'I am local'
        print('In test_local, x =', x)
    def test_nonlocal():
        nonlocal x
        x = 'I am nonlocal v1'
        print('In test_nonlocal, x =', x)
    def test_global():
        global x
        x = 'I am global v1'
        print('In test_global, x =', x)
    test_local()
    print('After test_local(), x =', x)
    test_nonlocal()
    print('After test_nonlocal(), x =', x)
    test_global()
    print('After test_global(), x =', x)

f()
print('In global, x =', x)
