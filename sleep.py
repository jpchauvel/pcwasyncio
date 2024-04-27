#!/usr/bin/env python3
import asyncio


async def hello_world_message() -> str:
    await asyncio.sleep(delay=1)
    return "Hello world!"


async def main() -> None:
    message: str = await hello_world_message()
    print(message)


if __name__ == "__main__":
    asyncio.run(main=main())
