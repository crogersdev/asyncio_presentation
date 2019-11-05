#!/usr/bin/env python

import requests
import sys
import time

num_requests = int(sys.argv[1])

url = 'http://localhost:8080/{}'

start = time.time()
for i in range(num_requests):
    res = requests.get(url.format(i))
    delay = res.headers.get('DELAY')
    d = res.headers.get('DATE')
    print('{}:{} delay {}'.format(d, res.url, delay))

print(f'elapsed: {time.time() - start} seconds')