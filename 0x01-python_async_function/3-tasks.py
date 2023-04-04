#!/usr/bin/env python3
'''Task3  Async
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''function creates an asynchronous task for wait_random.
    '''
    result = asyncio.create_task(wait_random(max_delay))
    return result
