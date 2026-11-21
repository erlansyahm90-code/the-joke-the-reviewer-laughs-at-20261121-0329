#!/usr/bin/env python3
"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (UTF-8, 1-280 characters).
"""
import os

JOKE = "My coding agent writes, reviews, and merges the code — I just provide the laptop and the blame."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
