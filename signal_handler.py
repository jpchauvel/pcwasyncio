#!/usr/bin/env python3
import asyncio
import signal
from asyncio import AbstractEventLoop

from util import delay


def cancel_tasks() -> None:
    print("Got a SIGINT")
    tasks: set[asyncio.Task] = asyncio.all_tasks()
    print(f"Cancelling {len(tasks)} task(s).")
    [task.cancel() for task in tasks]


async def main() -> None:
    loop: AbstractEventLoop = asyncio._get_running_loop()
    loop.add_signal_handler(signal.SIGINT, cancel_tasks)
    await delay(10)


if __name__ == "__main__":
    asyncio.run(main())
