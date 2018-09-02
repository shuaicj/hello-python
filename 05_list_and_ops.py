#!/usr/bin/env python3

langs = ['python', 'c', 'java']

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

langs.append('php')
print("langs.append('php'), langs =", langs)

langs.insert(2, 'c++')
print("langs.insert(2, 'c++'), langs =", langs)

langs.pop()
print("langs.pop(), langs =", langs)

langs.pop(2)
print("langs.pop(2), langs =", langs)

del langs[1]
print("del langs[1], langs =", langs)

langs[1] = 'c++'
print("langs[1] = 'c++', langs =", langs)

