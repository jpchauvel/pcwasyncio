#!/usr/bin/env python3
import asyncio
import logging
import signal
import socket
from asyncio import AbstractEventLoop
from typing import Optional

echo_tasks: list[asyncio.Task[None]] = []
loop: Optional[AbstractEventLoop] = None


class GracefulExit(SystemExit):
    pass


async def echo(connection: socket.socket, loop: AbstractEventLoop) -> None:
    try:
        while data := await loop.sock_recv(connection, 1024):
            if data == b"boom\r\n":
                raise Exception("Unexpected network error")
            await loop.sock_sendall(connection, data)
    except Exception as err:
        logging.exception(err)
    finally:
        connection.close()


async def connection_listener(
    server_socket: socket.socket, loop: AbstractEventLoop
) -> None:
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Got a connection from {address}")
        echo_task: asyncio.Task[None] = asyncio.create_task(
            echo(connection, loop)
        )
        echo_tasks.append(echo_task)


def shutdown():
    raise GracefulExit()


async def close_echo_tasks(echo_tasks: list[asyncio.Task[None]]) -> None:
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            pass


async def main() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    for signame in {"SIGINT", "SIGTERM"}:
        loop.add_signal_handler(getattr(signal, signame), shutdown)

    await connection_listener(server_socket, asyncio.get_running_loop())


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(main())
    except GracefulExit:
        loop.run_until_complete(close_echo_tasks(echo_tasks))
    finally:
        loop.close()
