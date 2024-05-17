#!/usr/bin/env python3
import asyncio
from typing import Any, Coroutine

from aiohttp import ClientSession

from util import async_timed, fetch_status


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        fetchers: list[Coroutine[Any, Any, int]] = [
            fetch_status(session, "https://example.com", 1),
            fetch_status(session, "https://example.com", 10),
            fetch_status(session, "https://example.com", 10),
        ]
        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.exceptions.TimeoutError:
                print("We got a timeout error!")

        for task in asyncio.tasks.all_tasks():
            print(task)


if __name__ == "__main__":
    asyncio.run(main())
