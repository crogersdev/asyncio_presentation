#!/usr/bin/env python3

import asyncio
import time
from aiohttp import ClientSession

async def fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response_text = await response.read()
            print(response_text)

loop = asyncio.get_event_loop()

start = time.time()
loop.run_until_complete(fetch('http://httpbin.org/get'))
print(f'elapsed: {time.time() - start} seconds')