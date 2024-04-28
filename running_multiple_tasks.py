#!/usr/bin/env python3
import asyncio

from util import delay


async def main() -> None:
    sleep_for_three: asyncio.Task = asyncio.create_task(coro=delay(3))
    sleep_again: asyncio.Task = asyncio.create_task(coro=delay(3))
    sleep_once_more: asyncio.Task = asyncio.create_task(coro=delay(3))

    await sleep_for_three
    await sleep_again
    await sleep_once_more


if __name__ == "__main__":
    asyncio.run(main=main())
