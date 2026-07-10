#!/usr/bin/env python3
"""
Mosk task runner for the aop agentic workflow example.

Purposefully not completed documented to give the chance for the agents to analyze their own workflow outputs.
"""

import argparse
import hashlib
import random
import sys
import time


def parse_args():
    parser = argparse.ArgumentParser(description="Mock task runner")
    parser.add_argument("--magic", type=float, default=0.0, help="the magic value")
    parser.add_argument("task", type=str, help="the task to execute")
    parser.add_argument("extras", nargs="*", help="additional arguments")
    return parser.parse_args()


def get_sleep_time(task: str) -> float:
    h = int(hashlib.md5(task.encode()).hexdigest(), 16)
    base = (h % 5000) / 1000
    jitter = random.uniform(-0.5, 1.5)
    return max(0.1, base + jitter)


def run_task(task: str, magic: float, extras: list[str]) -> int:
    print(f"executing task {task}")
    sleep_time = get_sleep_time(task)

    if magic > 0 and random.random() < magic:
        print(f"error: {task} failed unexpectedly (magic)", file=sys.stderr)
        return 1

    time.sleep(sleep_time)
    print(f"finished task {task} in {sleep_time:.2f}s")

    if extras:
        print(f"  extra args: {extras}")
    return 0


if __name__ == "__main__":
    args = parse_args()
    random.seed()
    sys.exit(run_task(args.task, args.magic, args.extras))
