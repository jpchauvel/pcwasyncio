#!/usr/bin/env python3
import asyncio

from util import delay


async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message() -> str:
    await delay(delay_seconds=1)
    return "Hello world!"


async def main() -> None:
    message: str = await hello_world_message()
    one_plus_one: int = await add_one(number=1)
    print(one_plus_one)
    print(message)


if __name__ == "__main__":
    asyncio.run(main=main())
