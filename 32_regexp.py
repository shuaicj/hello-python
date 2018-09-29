#!/usr/bin/env python3

import re

result = re.match(r'^([A-Z]+)\s([a-z]+)\s+([0-9]+)$', 'HELLO shuaicj  20180929')

if result:
    print(result.groups())
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))
else:
    print('not matched')

