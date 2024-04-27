#!/usr/bin/env python3
import time
import urllib.request


def read_example() -> None:
    with urllib.request.urlopen("https://example.com") as response:
        print(response.getcode())


if __name__ == "__main__":
    sync_start = time.time()

    read_example()
    read_example()

    sync_end = time.time()

    print(f"Running synchronously took {sync_end - sync_start:.4f} seconds.")
