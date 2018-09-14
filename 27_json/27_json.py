#!/usr/bin/env python3

import json

d = {'name': 'python', 'graceful': True}

print(json.dumps(d))

print(json.loads(json.dumps(d)))


path = './dump_file'

with open(path, 'w') as f:
    json.dump(d, f)

with open(path, 'r') as f:
    print(json.load(f))

