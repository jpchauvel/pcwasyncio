#!/usr/bin/env python3
import asyncio
import urllib.request
from typing import Callable, Optional
from http.client import HTTPResponse


def callback(url: str, response: str) -> None:
    print("=================URL======================")
    print(url)
    print("=================Response=================")
    print(response)


async def worker(
    queue: asyncio.Queue, callback: Optional[Callable[[str, str], None]] = None
) -> None:
    while True:
        url: str = await queue.get()
        loop = asyncio.get_running_loop()
        response: HTTPResponse = await loop.run_in_executor(
            None, urllib.request.urlopen, url
        )
        queue.task_done()
        if callback is not None:
            callback(url, response.read().decode("utf-8"))


async def main() -> None:
    queue: asyncio.Queue[str] = asyncio.Queue()
    for i in range(10):
        queue.put_nowait("https://python.org")
        queue.put_nowait("https://python.pe")

    tasks: list[asyncio.Task[None]] = []
    for i in range(4):
        task: asyncio.Task[None] = asyncio.create_task(
            coro=worker(queue=queue, callback=callback)
        )
        tasks.append(task)

    # Wait until the queue is fully processed
    await queue.join()

    for task in tasks:
        task.cancel()

    # Wait until all tasks are cancelled
    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())
