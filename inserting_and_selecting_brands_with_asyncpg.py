#!/usr/bin/env python3
import asyncio

import asyncpg
from asyncpg import Record


async def main() -> None:
    connection: asyncpg.Connection = await asyncpg.connect(
        host="localhost", port=5432, user="postgres", database="products"
    )
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')");
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')");
    brand_query: str = "SELECT brand_id, brand_name FROM brand"
    results: list[Record] = await connection.fetch(brand_query)
    for brand in results:
        print(f"id: {brand["brand_id"]}, name: {brand["brand_name"]}")
    await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
