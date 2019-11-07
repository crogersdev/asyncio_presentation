#!/usr/bin/env python3

import asyncio
import time
from aiohttp import ClientSession

url = 'http://httpbin.org/get'

async def fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response_text = await response.read()
            print(response_text)

loop = asyncio.get_event_loop()
print(f'reaching out to {url}')
start = time.time()
loop.run_until_complete(fetch(url))
print(f'elapsed time: {time.time() - start} seconds')