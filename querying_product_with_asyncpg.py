#!/usr/bin/env python3
import asyncio
from typing import Any, Coroutine

import asyncpg

product_query = """
SELECT
p.product_id,
p.product_name,
p.brand_id,
s.sku_id,
pc.product_color_name,
ps.product_size_name
FROM product AS p
JOIN sku AS s on s.product_id = p.product_id
JOIN product_color AS pc on pc.product_color_id = s.product_color_id
JOIN product_size AS ps on ps.product_size_id = s.product_size_id
WHERE p.product_id = 100;
"""


async def main() -> None:
    connection: asyncpg.Connection = await asyncpg.connect(
        host="localhost", port=5432, user="postgres", database="products"
    )
    print("Creating the product database...")
    queries: list[Coroutine[Any, Any, str]] = [
        connection.execute(product_query),
        connection.execute(product_query),
    ]
    results: list[str] = await asyncio.gather(*queries)


if __name__ == "__main__":
    asyncio.run(main())
