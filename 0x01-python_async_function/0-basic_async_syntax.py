#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waiting a random number of seconds.
    '''
    waitTime = random.random() * max_delay
    await asyncio.sleep(waitTime)
    return waitTime
