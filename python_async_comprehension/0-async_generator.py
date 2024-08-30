#!/usr/bin/env python3
"""
Module that contains an async generator
"""
import asyncio
import random

async def async_generator ():
    """Coroutine that just generates 10 awaits via sleep
    """
    for _ in range(0, 9):
        await asyncio.sleep(1)
        random.uniform(0, 10)
