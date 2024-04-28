#!/usr/bin/env python3
import asyncio

from util import delay


async def main() -> None:
    task: asyncio.Task[int] = asyncio.create_task(coro=delay(10))
    try:
        result: int = await asyncio.wait_for(
            fut=asyncio.shield(task), timeout=5
        )
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Task took longer than five seconds, it will finish soon!")
        result: int = await task
        print(result)


if __name__ == "__main__":
    asyncio.run(main=main())
