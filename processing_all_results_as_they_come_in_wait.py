#!/usr/bin/env python3
import asyncio

from aiohttp import ClientSession

from util import async_timed, fetch_status


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        url = "https://www.example.com"
        pending: set[asyncio.Task[int]] = set(
            [
                asyncio.create_task(fetch_status(session, url, 1)),
                asyncio.create_task(fetch_status(session, url, 5)),
                asyncio.create_task(fetch_status(session, url, 10)),
            ]
        )
        while pending:
            done, pending = await asyncio.wait(
                pending, return_when=asyncio.FIRST_COMPLETED
            )

            print(f"Done task count: {len(done)}")
            print(f"Pending task count: {len(pending)}")
            for done_task in done:
                print(await done_task)


if __name__ == "__main__":
    asyncio.run(main())
