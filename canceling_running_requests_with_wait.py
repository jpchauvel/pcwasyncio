#!/usr/bin/env python3
import asyncio
import logging

from aiohttp import ClientSession

from util import async_timed, fetch_status


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        fetchers: list[asyncio.Task[int]] = [
            asyncio.create_task(coro=fetch_status(session, "python://bad")),
            asyncio.create_task(
                coro=fetch_status(session, "https://example.com", 3)
            ),
            asyncio.create_task(
                coro=fetch_status(session, "https://example.com", 3)
            ),
        ]
        done, pending = await asyncio.wait(
            fetchers, return_when=asyncio.FIRST_EXCEPTION
        )
        print(f"Done task count: {len(done)}")
        print(f"Pending task count: {len(pending)}")
        for done_task in done:
            # result = await don_task will throw an exceptino
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error(
                    "Request got an exception", exc_info=done_task.exception()
                )
        for pending_task in pending:
            pending_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
