#!/usr/bin/env python3
import asyncio

from aiohttp import ClientSession

from util import async_timed, fetch_status


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        fetchers: list[asyncio.Task[int]] = [
            asyncio.create_task(fetch_status(session, "https://example.com")),
            asyncio.create_task(fetch_status(session, "https://example.com")),
        ]
        done, pending = await asyncio.wait(fetchers)
        print(f"Done task count: {len(done)}")
        print(f"Pending task count: {len(pending)}")
        for done_task in done:
            result: int = await done_task
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
