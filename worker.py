#!/usr/bin/env python3
import asyncio
import urllib.request
from http.client import HTTPResponse
from typing import Awaitable, Callable, Optional

import aiofiles


async def callback(url: str, response: str) -> None:
    async with aiofiles.open("responses.txt", "a", encoding="utf-8") as fd:
        await fd.write(
            f"""
=====================URL==========================
{url}
=====================Response=====================
{response}

"""
        )


async def worker(
    queue: asyncio.Queue,
    callback: Optional[Callable[[str, str], Awaitable[None]]] = None,
) -> None:
    while True:
        url: str = await queue.get()
        loop = asyncio.get_running_loop()
        response: HTTPResponse = await loop.run_in_executor(
            None, urllib.request.urlopen, url
        )
        if callback is not None:
            await callback(url, response.read().decode("utf-8"))
        queue.task_done()


async def main() -> None:
    queue: asyncio.Queue[str] = asyncio.Queue()
    for i in range(10):
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
