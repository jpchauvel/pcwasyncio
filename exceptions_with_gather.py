#!/usr/bin/env python3
import asyncio
from typing import Any, Coroutine

from aiohttp import ClientSession

from util import async_timed, fetch_status


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        urls: list[str] = ["https://example.com", "python://example.com"]
        requests: list[Coroutine[Any, Any, int]] = [
            fetch_status(session, url) for url in urls
        ]
        results: list[int | BaseException] = await asyncio.gather(
            *requests, return_exceptions=True
        )
        exceptions: list[BaseException] = [
            exception
            for exception in results
            if isinstance(exception, BaseException)
        ]
        successful_results: list[int] = [
            result
            for result in results
            if not isinstance(result, BaseException)
        ]
        print(f"All results: {results}")
        print(f"Finished results: {successful_results}")
        print(f"Exceptions: {exceptions}")


if __name__ == "__main__":
    asyncio.run(main())
