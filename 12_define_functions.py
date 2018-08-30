#!/usr/bin/env python3

def inc(x):
    return x + 1

print('inc(2) =', inc(2))

def do_nothing(x):
    pass

print('do_nothing(2) =', do_nothing(2))

def step(x, y):
    return x + 1, y + 1

print('step(2, 3) =', step(2, 3))

x, y = step(2, 3)
print('x, y = step(2, 3), x =', x, 'y =', y)

def default_args(name, lang='python3', repo='github'):
    return name, lang, repo

print("default_args('hello-python') = ", default_args('hello-python'))
print("default_args('hello-python', 'python') = ", default_args('hello-python', 'python'))
print("default_args('hello-python', repo='gitlib') = ", default_args('hello-python', repo='gitlib'))
print("default_args(name='hello-python', repo='gitlib') = ", default_args(name='hello-python', repo='gitlib'))

def wrong_default_args(a, x=[]):
    x.append(a)
    return x

print('wrong_default_args(1) = ', wrong_default_args(1))
print('wrong_default_args(2) = ', wrong_default_args(2))
print('wrong_default_args(3) = ', wrong_default_args(3))

def right_default_args(a, x=None):
    if x is None:
        x = []
    x.append(a)
    return x

print('right_default_args(1) = ', right_default_args(1))
print('right_default_args(2) = ', right_default_args(2))
print('right_default_args(3) = ', right_default_args(3))

def print_varargs(*n):
    print('varargs n =', n, end=' ')
    for i, m in enumerate(n):
        print('n[%d] = %d' % (i, m), end=' ')
    print()

print_varargs()
print_varargs(2, 2, 2)
print_varargs(*[2, 2, 2])

def print_kwargs(**kw):
    print('kwargs kw =', kw, end=' ')
    for k, v in kw.items():
        print('%s:%s' % (k, v), end=' ')
    print()

print_kwargs()
print_kwargs(name='hello-python', lang='python3')
print_kwargs(**{'name': 'hello-python', 'lang': 'python3'})

def print_kwargs(**kw):
    print('kwargs kw =', kw, end=' ')
    for k, v in kw.items():
        print('%s:%s' % (k, v), end=' ')
    print()

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-2) + fib(n-1)

for n in range(10):
    print('fib(%d) = %d' % (n, fib(n)))

