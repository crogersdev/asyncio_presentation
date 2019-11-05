#!/usr/bin/env python
import requests
import time

def fetch():
    return requests.get('http://httpbin.org/get')

start = time.time()
print(fetch())
print(f'elapsed: {time.time() - start} seconds')