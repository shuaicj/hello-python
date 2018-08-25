#!/usr/bin/env python3

langs = ['python', 'c', 'java']

print('langs =', langs)
print('len(langs) =', len(langs))
print('langs[0] =', langs[0])
print('langs[1] =', langs[1])
print('langs[2] =', langs[2])
print('langs[-1] =', langs[-1])
print('langs[-2] =', langs[-2])
print('langs[-3] =', langs[-3])
print('langs[1:] =', langs[1:])
print('langs[0:-1] =', langs[0:-1])

langs.append('php')
print("langs.append('php'), langs =", langs)

langs.insert(2, 'c++')
print("langs.insert(2, 'c++'), langs =", langs)

langs.pop()
print("langs.pop(), langs =", langs)

langs.pop(2)
print("langs.pop(2), langs =", langs)

langs[1] = 'c++'
print("langs[1] = 'c++', langs =", langs)

mixed_langs = [['python', 'php'], ['c', 'c++'], 'java']
print('mixed_langs =', mixed_langs)

