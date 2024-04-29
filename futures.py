#!/usr/bin/env python3
from asyncio import Future

if __name__ == "__main__":
    my_future: Future[int] = Future()
    print(f"Is my future done? {my_future.done()}")
    my_future.set_result(42)
    print(f"Is my future done? {my_future.done()}")
    print(f"What is the result of my_future? {my_future.result()}")
