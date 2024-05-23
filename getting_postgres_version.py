#!/usr/bin/env python3
import asyncio

import asyncpg


async def main() -> None:
    connection: asyncpg.Connection = await asyncpg.connect(
        host="localhost", port=5432, user="postgres", database="postgres"
    )
    version: asyncpg.ServerVersion = connection.get_server_version()
    print(f"Connected! Postres version is {version}")
    await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
