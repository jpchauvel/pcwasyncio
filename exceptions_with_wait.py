#!/usr/bin/env python3
import asyncio
import logging
from typing import Any, Coroutine

from aiohttp import ClientSession

from util import async_timed, fetch_status


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        good_request: Coroutine[Any, Any, int] = fetch_status(
            session, "https://example.com"
        )
        bad_request: Coroutine[Any, Any, int] = fetch_status(
            session, "ptyhon://bad"
        )

        fetchers: list[asyncio.Task[int]] = [
            asyncio.create_task(good_request),
            asyncio.create_task(bad_request),
        ]
        done, pending = await asyncio.wait(fetchers)
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


if __name__ == "__main__":
    asyncio.run(main())
