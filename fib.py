#!/usr/bin/env python3

import asyncio
import sys
import time

def sync_fib(n):
    if n <= 1:
        return n
    else:
        return sync_fib(n - 1) + sync_fib(n - 2)

async def async_fib(n):
    if n <= 1:
        return 1
    else:
        return await async_fib(n - 1) + await async_fib(n - 2)

if __name__ == '__main__':

    sync_async_switch = sys.argv[1]
    fib_num = int(sys.argv[2])

    if sync_async_switch == 'sync':
        start = time.time()
        sync_fib(fib_num)
        print(f'elapsed: {time.time() - start} seconds')

    elif sync_async_switch == 'async':
        loop = asyncio.get_event_loop()
        start = time.time()
        loop.run_until_complete(async_fib(fib_num))
        print(f'elapsed: {time.time() - start} seconds')


    else:
        print('specify async or sync please')
