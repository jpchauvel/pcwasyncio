#!/usr/bin/env python3
import asyncio
import socket
from types import TracebackType
from typing import Optional, Type


class ConnectedSocket:
    def __init__(self, server_socket) -> None:
        self._connection: Optional[socket.socket] = None
        self._server_socket = server_socket

    async def __aenter__(self):
        print("Entering context manager, waiting for connection")
        loop: asyncio.AbstractEventLoop = asyncio.get_running_loop()
        connection, _ = await loop.sock_accept(self._server_socket)
        self._connection = connection
        print("Accepted connection")
        return self._connection

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        print("Exiting context manager")
        self._connection.close()
        print("Closed connection")


async def main() -> None:
    loop: asyncio.AbstractEventLoop = asyncio._get_running_loop()
    server_socket: socket.socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address: tuple[str, int] = ("127.0.0.1", 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
    async with ConnectedSocket(server_socket) as connection:
        data = await loop.sock_recv(connection, 1024)
        print(data)


if __name__ == "__main__":
    asyncio.run(main())
