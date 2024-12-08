from itertools import combinations
import sys
from typing import NamedTuple


class Position(NamedTuple):
    x: int
    y: int


def get_antinodes(a: Position, b: Position):
    dx = abs(a.x - b.x)
    dy = abs(a.y - b.y)
    min_x = min(a.x, b.x)
    min_y = min(a.y, b.y)
    max_x = max(a.x, b.x)
    max_y = max(a.y, b.y)
    while True:
        if a.x < b.x and a.y < b.y:
            yield [Position(min_x, min_y), Position(max_x, max_y)]
        else:
            yield [Position(max_x, min_y), Position(min_x, max_y)]
        min_x -= dx
        max_x += dx
        min_y -= dy
        max_y += dy


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

    all_antinodes = set()
    for a in antennas_characters:
        for p1, p2 in combinations(get_antennas_positions(a), 2):
            for pair in get_antinodes(p1, p2):
                new_antinodes = set(an for an in pair if within_bounds(an))
                if not new_antinodes:
                    break
                all_antinodes |= new_antinodes

    solution = len(all_antinodes)
    print(solution)


if __name__ == "__main__":
    main()
