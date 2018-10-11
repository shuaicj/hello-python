#!/usr/bin/env python3

from collections import deque

q = deque(['a', 'x', 'm', 'y'])

q.append('z')
print(q)

q.pop()
print(q)

q.appendleft('b')
print(q)

q.popleft()
print(q)
