#!/usr/bin/env python3

import asyncio
import time
from aiohttp import ClientSession

async def fetch(url):
    session = ClientSession()
    response = await session.get(url)
    response_text = await response.read()
    print(response_text)
    await response.wait_for_close()
    await session.close()

loop = asyncio.get_event_loop()

start = time.time()
loop.run_until_complete(fetch('http://httpbin.org/get'))
print(f'elapsed: {time.time() - start} seconds')