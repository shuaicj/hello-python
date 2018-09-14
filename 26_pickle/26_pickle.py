#!/usr/bin/env python3

import pickle

d = {'name': 'shuaicj', 'lang': 'python'}

print(pickle.dumps(d))

print(pickle.loads(pickle.dumps(d)))


path = './dump_file'

with open(path, 'wb') as f:
    pickle.dump(d, f)

with open(path, 'rb') as f:
    print(pickle.load(f))

