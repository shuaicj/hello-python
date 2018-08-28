#!/usr/bin/env python3

langs = ('python', 'c', 'java')

print('langs =', langs)
print('len(langs) =', len(langs))
print('sorted(langs) =', sorted(langs))
print('langs[0] =', langs[0])
print('langs[1] =', langs[1])
print('langs[2] =', langs[2])
print('langs[-1] =', langs[-1])
print('langs[-2] =', langs[-2])
print('langs[-3] =', langs[-3])
print('langs[1:] =', langs[1:])
print('langs[0:-1] =', langs[0:-1])

print("'python' in langs =", 'python' in langs)
print("'golang' in langs =", 'golang' in langs)
print("'golang' not in langs =", 'golang' not in langs)

x, y, z = langs
print('x, y, z = langs, x =', x)
print('x, y, z = langs, y =', y)
print('x, y, z = langs, z =', z)

empty_tuple = ()
print('empty_tuple =', empty_tuple)

size_1_tuple = ('python',)
print('size_1_tuple =', size_1_tuple)

size_1_tuple_bad = ('python')
print('size_1_tuple_bad =', size_1_tuple_bad)
