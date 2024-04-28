#!/usr/bin/env python3
import asyncio

from util import delay


async def main() -> None:
    delay_task: asyncio.Task[int] = asyncio.create_task(coro=delay(2))
    try:
        result: int = await asyncio.wait_for(fut=delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Got a timeout")
        print(f"Was the task cancelled? {delay_task.cancelled()}")


if __name__ == "__main__":
    asyncio.run(main=main())
