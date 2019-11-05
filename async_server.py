#!/usr/bin/env python

import asyncio
from datetime import datetime
from aiohttp import web
import random

random.seed(1)

async def hello(request):
    name = request.match_info.get('name', 'foo')
    n = datetime.now().isoformat()
    delay = random.randint(0, 3)
    await asyncio.sleep(delay)
    headers = { 'content_type': 'text/html', 'delay': str(delay) }

    # reminder: opening a file is a blocking operation.
    # consider using asycnio Executor to improve performance
    
    with open('count_of_monte_cristo_full.html', 'rb') as html_body:
        print(f'{n}: {request.path} delay: {delay}')
        response = web.Response(body=html_body.read(), headers=headers)
    return response

app = web.Application()
app.router.add_route('GET', '/{name}', hello)
web.run_app(app)