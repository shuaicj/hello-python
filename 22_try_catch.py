#!/usr/bin/env python3

def f(n):
    try:
        x = 4 / n
        print('x =', x)
    except ZeroDivisionError as e:
        print('in except block,', e)
    else:
        print('in else block')
    finally:
        print('in finally block')

f(2)

print()

f(0)
