#!/usr/bin/env python3
'''Task 0 Async. '''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''function to genereate a sequence of 10 numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
