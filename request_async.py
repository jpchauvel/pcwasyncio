#!/usr/bin/env python3
import threading
import time
import urllib.request


def read_example() -> None:
    with urllib.request.urlopen("https://example.com") as response:
        print(response.getcode())


if __name__ == "__main__":
    thread_1 = threading.Thread(target=read_example)
    thread_2 = threading.Thread(target=read_example)

    thread_start = time.time()

    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()

    thread_end = time.time()

    print(f"Running with threads took {thread_end - thread_start:.4f} seconds.")
