#!/usr/bin/env python3
import asyncio

from aiohttp import ClientSession

from util import async_timed, fetch_status


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        url = "https://example.com"
        fetchers : set[asyncio.Task[int]] = set([ 
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url, 3)),
        ])
        done, pending = await asyncio.wait(fetchers, timeout=1)

        print(f"Done task count: {len(done)}")
        print(f"Pending task count: {len(pending)}")
        for done_task in done:
            result: int = await done_task
            print(result)
        for pending_task in pending:
            pending_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
