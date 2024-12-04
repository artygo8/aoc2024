from itertools import pairwise, starmap
import sys
from typing import Generator


def parse_input() -> Generator[tuple[int, ...], None, None]:
    for line in sys.stdin:
        if not line.strip():
            continue
        yield tuple(map(int, line.strip().split()))


def is_safe(line: tuple[int, ...]):
    increasing = list(line) == sorted(line)
    decreasing = list(line) == sorted(line, reverse=True)
    diffs = tuple(starmap(lambda l, r: abs(l - r), pairwise(line)))
    safe_diffs = min(diffs) >= 1 and max(diffs) <= 3
    return (increasing or decreasing) and safe_diffs


def main():
    solution = sum(map(is_safe, parse_input()))
    print(solution)


if __name__ == "__main__":
    main()
