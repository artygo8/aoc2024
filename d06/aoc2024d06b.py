from itertools import cycle
import sys
from typing import Callable, NamedTuple


class LoopDetected(Exception):
    pass


class Position(NamedTuple):
    x: int
    y: int
    direction: Callable | None = None


def get_direction_wheel():
    return cycle(
        [
            lambda x, y: (x, y - 1),  # up
            lambda x, y: (x + 1, y),  # right
            lambda x, y: (x, y + 1),  # down
            lambda x, y: (x - 1, y),  # left
        ]
    )


def get_visited(
    grid: list[str],
    start: tuple[int, int],
    extra_obstruction: tuple[int, int] | None = None,
):
    direction_wheel = get_direction_wheel()
    visited = set()
    x, y = start
    go = next(direction_wheel)
    while True:
        position = Position(x, y, go)
        if position in visited:
            raise LoopDetected

        visited.add(position)
        try:
            _x, _y = go(x, y)
            while grid[_y][_x] == "#" or (_x, _y) == extra_obstruction:
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


def is_loop(
    grid: list[str],
    start: tuple[int, int],
    obstruction: tuple[int, int],
):
    try:
        get_visited(grid, start, extra_obstruction=obstruction)
    except LoopDetected:
        return True
    return False


def main():
    grid = [l.strip() for l in sys.stdin if l.strip()]
    start = next(
        (x, y) for y, l in enumerate(grid) for x, c in enumerate(l) if c == "^"
    )
    possible_obstructions = {
        (v.x, v.y) for v in get_visited(grid, start) if (v.x, v.y) != start
    }
    solution = sum(is_loop(grid, start, o) for o in possible_obstructions)
    print(solution)


if __name__ == "__main__":
    main()
