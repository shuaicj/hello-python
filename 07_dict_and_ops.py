#!/usr/bin/env python3

langs = {'python': 100, 'c': 110, 'java': 120}

print('langs =', langs)
print('len(langs) =', len(langs))
print('sorted(langs) =', sorted(langs))

print("langs['python'] =", langs['python'])
print("langs.get('python') =", langs.get('python'))

# KeyError!
# print("langs['golang'] =", langs['golang'])
# print("langs.get('golang') =", langs.get('golang'))

print("langs.get('golang', 80) =", langs.get('golang', 80))

print("'python' in langs =", 'python' in langs)
print("'golang' in langs =", 'golang' in langs)
print("'golang' not in langs =", 'golang' not in langs)

langs['python'] = 90
print("langs['python'] = 90, langs =", langs)

del langs['c']
print("del langs['c'], langs =", langs)

