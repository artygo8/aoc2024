from itertools import count, permutations
import sys
from typing import NamedTuple


class Position(NamedTuple):
    x: int
    y: int


def next_steps(p: int, q: int):
    step_size = abs(p - q)
    for step in count(0, step=step_size):
        if p < q:
            yield max(p, q) + step
        else:
            yield min(p, q) - step


def main():
    grid = [l.strip() for l in sys.stdin if l.strip()]

    def within_bounds(p: Position):
        return 0 <= p.x < len(grid[0]) and 0 <= p.y < len(grid)

    def get_antinodes(a: Position, b: Position):
        for p, q in zip(next_steps(a.x, b.x), next_steps(a.y, b.y)):
            pos = Position(p, q)
            if not within_bounds(pos):
                break
            yield pos

    def get_char_positions(char: str):
        return [
            Position(x, y)
            for y, row in enumerate(grid)
            for x, c in enumerate(row)
            if c == char
        ]

    antennas_characters = set("".join(grid)) - set(".")
    all_antinodes = {
        an
        for a in antennas_characters
        for p1, p2 in permutations(get_char_positions(a), 2)
        for an in get_antinodes(p1, p2)
    }

    solution = len(all_antinodes)
    print(solution)


if __name__ == "__main__":
    main()
