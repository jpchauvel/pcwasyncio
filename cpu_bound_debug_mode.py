#!/usr/bin/env python3
import asyncio
from util import async_timed


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter += 1
    return counter


async def main() -> None:
    task_one: asyncio.Task[int] = asyncio.create_task(coro=cpu_bound_work())
    await task_one


if __name__ == "__main__":
    asyncio.run(main(), debug=True)
