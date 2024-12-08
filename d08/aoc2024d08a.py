from itertools import combinations
import sys
from typing import NamedTuple


class Position(NamedTuple):
    x: int
    y: int


def get_antinodes(a: Position, b: Position):
    dx = abs(a.x - b.x)
    dy = abs(a.y - b.y)
    min_x = min(a.x, b.x) - dx
    min_y = min(a.y, b.y) - dy
    max_x = max(a.x, b.x) + dx
    max_y = max(a.y, b.y) + dy
    if a.x < b.x and a.y < b.y:
        return [Position(min_x, min_y), Position(max_x, max_y)]
    else:
        return [Position(max_x, min_y), Position(min_x, max_y)]


def main():
    grid = [l.strip() for l in sys.stdin if l.strip()]

    def within_bounds(p: Position):
        return 0 <= p.x < len(grid[0]) and 0 <= p.y < len(grid)

    antennas_characters = set("".join(grid)) - set(".")

    def get_antennas_positions(antenna_char: str):
        return [
            Position(x, y)
            for y, row in enumerate(grid)
            for x, c in enumerate(row)
            if c == antenna_char
        ]

    all_antinodes = set(
        an
        for a in antennas_characters
        for p1, p2 in combinations(get_antennas_positions(a), 2)
        for an in get_antinodes(p1, p2)
        if within_bounds(an)
    )

    solution = len(all_antinodes)
    print(solution)


if __name__ == "__main__":
    main()
