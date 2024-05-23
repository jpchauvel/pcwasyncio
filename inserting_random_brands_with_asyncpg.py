#!/usr/bin/env python3
import asyncio
from random import sample

import asyncpg

from util import load_common_words


def generate_brand_names(words: list[str]) -> list[tuple[str]]:
    return [(words[i],) for i in sample(range(1000), 100)]


async def insert_brands(common_words: list[str], connection: asyncpg.Connection) -> None:
    brands: list[tuple[str]] = generate_brand_names(common_words)
    insert_statement: str = "INSERT INTO brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_statement, brands)


async def main() -> None:
    connection: asyncpg.Connection = await asyncpg.connect(
        host="localhost", port=5432, user="postgres", database="products"
    )
    common_words: list[str] = await load_common_words()
    await insert_brands(common_words, connection)
    await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
