#!/usr/bin/env python3
import asyncio
from random import randint, sample

import asyncpg

from util import load_common_words


def gen_products(
    common_words: list[str],
    brand_id_start: int,
    brand_id_end: int,
    products_to_create: int,
) -> list[tuple[str, int]]:
    products: list[tuple[str, int]] = []
    for _ in range(products_to_create):
        description: list[str] = [
            common_words[i] for i in sample(range(1000), 10)
        ]
        brand_id = randint(brand_id_start, brand_id_end)
        products.append((" ".join(description), brand_id))
    return products


def gen_skus(
    product_id_start: int, product_id_end: int, skus_to_create: int
) -> list[tuple[int, int, int]]:
    skus: list[tuple[int, int, int]] = []
    for _ in range(skus_to_create):
        product_id = randint(product_id_start, product_id_end)
        size_id = randint(1, 3)
        color_id = randint(1, 2)
        skus.append((product_id, size_id, color_id))
    return skus


async def main() -> None:
    connection: asyncpg.Connection = await asyncpg.connect(
        host="localhost", port=5432, user="postgres", database="products"
    )
    common_words: list[str] = await load_common_words()
    product_tuples: list[tuple[str, int]] = gen_products(
        common_words, 1, 100, 1000
    )
    await connection.executemany("INSERT INTO product VALUES(DEFAULT, $1, $2)", product_tuples)
    sku_tuples: list[tuple[int, int, int]] = gen_skus(1, 1000, 100000)
    await connection.executemany("INSERT INTO sku VALUES(DEFAULT, $1, $2, $3)", sku_tuples)
    await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
