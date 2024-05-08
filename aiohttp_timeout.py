#!/usr/bin/env python3
import asyncio

import aiohttp
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis: aiohttp.ClientTimeout = aiohttp.ClientTimeout(total=0.3)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status


async def main() -> None:
    session_timeout: aiohttp.ClientTimeout = aiohttp.ClientTimeout(
        total=1, connect=0.1
    )
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        await fetch_status(session, "https://example.com")


if __name__ == "__main__":
    asyncio.run(main())
