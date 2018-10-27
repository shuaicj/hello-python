#!/usr/bin/env python3

# pip3 install requests

# see https://github.com/requests/requests

import requests

TIMEOUT = 10 # in seconds

### get
r = requests.get('https://github.com/', timeout=TIMEOUT)

print(r.text)
print('status code:', r.status_code)

### post
# body = {'username': 'shuaicj', 'password': 'secret'}

# r = requests.post('https://somesite.com/login', json=body, timeout=TIMEOUT)

# print('status code:', r.status_code)
