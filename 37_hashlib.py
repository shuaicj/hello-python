#!/usr/bin/env python3

import hashlib

md5 = hashlib.md5()
md5.update('this is a long long text'.encode('utf-8'))
print(md5.hexdigest())
