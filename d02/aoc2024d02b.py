from itertools import pairwise, starmap
import sys
from typing import Generator


def parse_input() -> Generator[tuple[int, ...], None, None]:
    for line in sys.stdin:
        if not line.strip():
            continue
        yield tuple(map(int, line.strip().split()))


def remove_one(line: tuple[int, ...], i: int):
    return line[:i] + line[i + 1:]


def is_safe(line: tuple[int, ...]):
    def _is_safe(_line):
        increasing = list(_line) == sorted(_line)
        decreasing = list(_line) == sorted(_line, reverse=True)
        diffs = tuple(starmap(lambda l, r: abs(l - r), pairwise(_line)))
        safe_diffs = min(diffs) >= 1 and max(diffs) <= 3
        return (increasing or decreasing) and safe_diffs

    return any(_is_safe(remove_one(line, i)) for i in range(len(line)))


def main():
    solution = sum(map(is_safe, parse_input()))
    print(solution)


if __name__ == "__main__":
    main()
