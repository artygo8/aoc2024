from itertools import cycle
import sys
from typing import NamedTuple


class Position(NamedTuple):
    x: int
    y: int


def get_direction_wheel():
    return cycle(
        [
            lambda x, y: (x, y - 1),  # up
            lambda x, y: (x + 1, y),  # right
            lambda x, y: (x, y + 1),  # down
            lambda x, y: (x - 1, y),  # left
        ]
    )


def get_visited(grid, start):
    direction_wheel = get_direction_wheel()
    visited = set()
    x, y = start
    go = next(direction_wheel)
    while True:
        position = Position(x, y)
        visited.add(position)
        try:
            _x, _y = go(x, y)
            while grid[_y][_x] == "#":
                go = next(direction_wheel)
                _x, _y = go(x, y)
            x, y = _x, _y
            if x < 0 or y < 0:
                # Python being python, negative indexes are valid...
                # Got stuck on this for a while
                raise IndexError
        except IndexError:
            break
    return visited


def main():
    grid = [l.strip() for l in sys.stdin if l.strip()]
    start = next(
        (x, y) for y, l in enumerate(grid) for x, c in enumerate(l) if c == "^"
    )
    visited = get_visited(grid, start)
    total = len(visited)
    print(total)


if __name__ == "__main__":
    main()
