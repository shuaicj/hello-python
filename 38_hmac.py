#!/usr/bin/env python3

import hmac

key = 'mysecret'.encode('utf-8')

hmac_func = hmac.new(key=key, digestmod='md5')

hmac_func.update('this is a long long text'.encode('utf-8'))

print(hmac_func.hexdigest())
