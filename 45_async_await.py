#!/usr/bin/env python3

import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# print(type(main()))
# <class 'coroutine'>

asyncio.run(main())
