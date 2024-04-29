#!/usr/bin/env python3
import asyncio
from asyncio import Future


def make_request() -> Future:
    future: Future[int] = Future()
    asyncio.create_task(coro=set_future_value(future))
    return future


async def set_future_value(future) -> None:
    await asyncio.sleep(delay=1)
    future.set_result(42)


async def main() -> None:
    future = make_request()
    print(f"Is the future done? {future.done()}")
    value: int = await future
    print(f"Is the future done? {future.done()}")
    print(value)


if __name__ == "__main__":
    asyncio.run(main())
