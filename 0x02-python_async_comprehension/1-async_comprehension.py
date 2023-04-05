#!/usr/bin/env python3
'''Task 1 Async.
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''this function creates a list of 10 numbers using generators.
    '''
    result = [n async for n in async_generator()]
    return result

