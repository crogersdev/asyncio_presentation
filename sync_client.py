#!/usr/bin/env python
import requests
import time

url = 'http://httpbin.org/get'

def fetch(url):
    return requests.get(url)

print(f'reaching out to {url}')
start = time.time()
print(fetch(url))
print(f'elapsed time: {time.time() - start} seconds')