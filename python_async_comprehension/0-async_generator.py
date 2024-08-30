#!/usr/bin/env python3
"""
Module that contains an async generator
"""
import asyncio
from typing import AsyncGenerator
import random

async def async_generator () -> AsyncGenerator[float, None]:
    """
    Coroutine that just generates 10 awaits via sleep
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
