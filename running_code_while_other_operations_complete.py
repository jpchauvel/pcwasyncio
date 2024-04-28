#!/usr/bin/env python3
import asyncio

from util import delay


async def hello_every_second() -> None:
    for i in range(2):
        await asyncio.sleep(delay=1)
        print("I'm running other code while I'm waiting!")


async def main() -> None:
    first_delay: asyncio.Task[int] = asyncio.create_task(coro=delay(3))
    second_delay: asyncio.Task[int] = asyncio.create_task(coro=delay(3))
    await hello_every_second()
    await first_delay
    await second_delay


if __name__ == "__main__":
    asyncio.run(main=main())
