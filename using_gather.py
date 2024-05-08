#!/usr/bin/env python3
import asyncio
from typing import Any, Coroutine

from aiohttp import ClientSession

from util import async_timed, fetch_status


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        urls: list[str] = ["https://example.com" for _ in range(1000)]
        requests: list[Coroutine[Any, Any, int]] = [
            fetch_status(session, url) for url in urls
        ]
        status_codes: list[int] = await asyncio.gather(*requests)
        print(status_codes)


if __name__ == "__main__":
    asyncio.run(main())
