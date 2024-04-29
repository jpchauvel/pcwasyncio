#!/usr/bin/env python3
import asyncio
from util import async_timed, delay


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter += 1
    return counter


@async_timed()
async def main() -> None:
    task_one: asyncio.Task[int] = asyncio.create_task(coro=cpu_bound_work())
    task_two: asyncio.Task[int] = asyncio.create_task(coro=cpu_bound_work())
    delay_task: asyncio.Task[int] = asyncio.create_task(coro=delay(4))
    await task_one
    await task_two
    await delay_task


if __name__ == "__main__":
    asyncio.run(main())
