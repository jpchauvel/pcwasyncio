#!/usr/bin/env python3
import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1


if __name__ == "__main__":
    function_result: int = add_one(1)
    coroutine_result = coroutine_add_one(1)
    result: int = asyncio.run(coroutine_result)
    print(result)

    print(
        f"Function result is {function_result} and the type is {type(function_result)}"
    )
    print(
        f"Coroutine result is {coroutine_result} and the type is {type(coroutine_result)}"
    )
