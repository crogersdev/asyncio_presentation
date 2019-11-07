#!/usr/bin/env python3

import asyncio
import time
from aiohttp import ClientSession

url = 'http://httpbin.org/get'

async def fetch(url):
    session = ClientSession()
    response = await session.get(url)
    response_text = await response.read()
    print(response_text)
    await response.wait_for_close()
    await session.close()

loop = asyncio.get_event_loop()
print(f'reaching out to {url}')
start = time.time()
loop.run_until_complete(fetch(url))
print(f'elapsed: {time.time() - start} seconds')