#!/usr/bin/env python3

from functools import wraps

### function name
def f():
    pass

f1 = f

print('f.__name__ =', f.__name__)
print('f1.__name__ =', f1.__name__)

print()


### simple log decorator
def log(func):
    def wrapper(*args, **kw):
        print('before call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def p():
    print('this is function p()')

p()

# will print 'p.__name__ = wrapper'
print('p.__name__ =', p.__name__)

print()


### correct function name
def log2(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print('before call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log2
def p2():
    print('this is function p2()')

p2()

# will print 'p2.__name__ = p2'
print('p2.__name__ =', p2.__name__)

print()


### support log level
def log3(level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            print('%s - before call %s()' % (level, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log3('DEBUG')
def p3():
    print('this is function p3()')

p3()

print()

### support default level
def log4(arg):
    if isinstance(arg, str):
        return log3(arg)
    return log3('INFO')(arg)

@log4
def p4():
    print('this is function p4()')

@log4('DEBUG')
def p5():
    print('this is function p5()')

p4()
p5()

