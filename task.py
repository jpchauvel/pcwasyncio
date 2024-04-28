#!/usr/bin/env python3
import asyncio

from util import delay


async def main() -> None:
    sleep_for_three: asyncio.Task[int] = asyncio.create_task(coro=delay(3))
    print(type(sleep_for_three))
    result: int = await sleep_for_three
    print(result)


if __name__ == "__main__":
    asyncio.run(main=main())
