#!/usr/bin/env python3
import asyncio

from util import delay


async def main() -> None:
    long_task: asyncio.Task[int] = asyncio.create_task(coro=delay(10))
    seconds_elapsed = 0
    while not long_task.done():
        print("Task not finished, checking again in a second.")
        await asyncio.sleep(delay=1)
        seconds_elapsed += 1

        if seconds_elapsed == 5:
            long_task.cancel()

    try:
        await long_task
    except asyncio.exceptions.CancelledError:
        print("Our task was cancelled")


if __name__ == "__main__":
    asyncio.run(main=main())
