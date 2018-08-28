#!/usr/bin/env python3

#### nested types in list

# 'list in list' is ok
print([['python', 'php'], 'java'])

# 'tuple in list' is ok
print([('python', 'php'), 'java'])

# 'set in list' is ok
print([{'python', 'php'}, 'java'])

# 'dict in list' is ok
print([{'python': 1, 'php': 2}, 'java'])


#### nested types in tuple

# 'list in tuple' is ok
print((['python', 'php'], 'java'))

# 'tuple in tuple' is ok
print((('python', 'php'), 'java'))

# 'set in tuple' is ok
print(({'python', 'php'}, 'java'))

# 'dict in tuple' is ok
print(({'python': 1, 'php': 2}, 'java'))


#### nested types in set

# 'tuple in set' is ok
print({('python', 'php'), 'java'})

# 'list in set', '(list in tuple) in set' is bad
# TypeError: unhashable type: 'list'
# print({['python', 'php'], 'java'})
# print({('python', ['php']), 'java'})

# 'set in set', '(set in tuple) in set' is bad
# TypeError: unhashable type: 'set'
# print({{'python', 'php'}, 'java'})
# print({('python', {'php'}), 'java'})

# 'dict in set', '(dict in tuple) in set' is bad
# TypeError: unhashable type: 'dict'
# print({{'python': 1, 'php': 2}, 'java'})
# print({('python', {'php': 2}), 'java'})


#### nested types in dict

# 'tuple as dict key' is ok
print({('python', 'php'): 1})

# 'list as dict key', '(list in tuple) as dict key' is bad
# TypeError: unhashable type: 'list'
# print({['python', 'php']: 1})
# print({('python', ['php']): 1})

# 'set as dict key', '(set in tuple) as dict key' is bad
# TypeError: unhashable type: 'set'
# print({{'python', 'php'}: 1})
# print({('python', {'php'}): 1})

# 'dict as dict key', '(dict in tuple) as dict key' is bad
# TypeError: unhashable type: 'dict'
# print({{'python': 1, 'php': 2}: 1})
# print({('python', {'php': 2}): 1})

# 'list as dict value' is ok
print({'lang': ['python', 'php']})

# 'tuple as dict value' is ok
print({'lang': ('python', 'php')})

# 'set as dict value' is ok
print({'lang': {'python', 'php'}})

# 'dict as dict value' is ok
print({'lang': {'python': 1}})

