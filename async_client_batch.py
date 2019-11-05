#!/usr/bin/env python

import asyncio
from aiohttp import ClientSession
import time
import sys

async def fetch(url, session):
    async with session.get(url) as response:
        resp_bytes = await response.read()
        delay = response.headers.get('DELAY')
        d = response.headers.get('DATE')
        print('{}:{} delay {}'.format(d, url, delay))

        return resp_bytes 

async def run(r):
    url = 'http://localhost:8080/{}'
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        start = time.time()
        for i in range(r):
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)

        print(f'ensuring futures time elapsed: {time.time() - start} seconds')
        
        start = time.time()
        responses = await asyncio.gather(*tasks)
        print(f'await gather tasks time elapsed: {time.time() - start} seconds')
        # you now have all response bodies in this variable
        # we could print them...  but it's the WHOLE text of
        # The Count of Monte Cristo... 
        # print(responses)


num_tasks = int(sys.argv[1])

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(num_tasks))
loop.run_until_complete(future)