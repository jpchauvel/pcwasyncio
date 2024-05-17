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
            fetch_status(session, "https://example.com", 1),
            fetch_status(session, "https://example.com", 10),
        ]
        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


if __name__ == "__main__":
    asyncio.run(main())
