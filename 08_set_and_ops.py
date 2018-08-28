#!/usr/bin/env python3

langs = {'python', 'c', 'java'}

print('langs =', langs)
print('len(langs) =', len(langs))
print('sorted(langs) =', sorted(langs))

print("'python' in langs =", 'python' in langs)
print("'golang' in langs =", 'golang' in langs)
print("'golang' not in langs =", 'golang' not in langs)

langs2 = {'python', 'golang'}
print("langs & langs2 =", langs & langs2)
print("langs | langs2 =", langs | langs2)

langs.add('php')
print("langs.add('php'), langs =", langs)

langs.remove('c')
print("langs.remove('c'), langs =", langs)

