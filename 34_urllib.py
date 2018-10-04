#!/usr/bin/env python3

from urllib import request

req = request.Request('https://github.com/shuaicj')
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/69.0.3497.100 Safari/537.36')
with request.urlopen(req) as rsp:
    print(rsp.status, rsp.reason)
    for k, v in rsp.getheaders():
        print('%s: %s' % (k, v))
    print()
    body = rsp.read()
    print(body.decode('utf-8'))
