#!/usr/bin/env python3
import asyncio

import asyncpg

from products_schema_sql import (
    COLOR_INSERT,
    CREATE_BRAND_TABLE,
    CREATE_PRODUCT_COLOR_TABLE,
    CREATE_PRODUCT_SIZE_TABLE,
    CREATE_PRODUCT_TABLE,
    CREATE_SKU_TABLE,
    SIZE_INSERT,
)


async def main() -> None:
    connection: asyncpg.Connection = await asyncpg.connect(
        host="localhost", port=5432, user="postgres", database="products"
    )
    statements: list[str] = [
        CREATE_BRAND_TABLE,
        CREATE_PRODUCT_TABLE,
        CREATE_PRODUCT_COLOR_TABLE,
        CREATE_PRODUCT_SIZE_TABLE,
        CREATE_SKU_TABLE,
        COLOR_INSERT,
        SIZE_INSERT,
    ]
    print("Creating the product database...")
    for statement in statements:
        status: str = await connection.execute(statement)
        print(status)
    print("Finished creating the product database!")
    await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
