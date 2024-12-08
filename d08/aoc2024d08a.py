from itertools import permutations
import sys
from typing import NamedTuple


class Position(NamedTuple):
    x: int
    y: int


def next_step(p: int, q: int):
    step_size = abs(p - q)
    if p < q:
        return max(p, q) + step_size
    else:
        return min(p, q) - step_size


def next_node(a: Position, b: Position):
    return Position(next_step(a.x, b.x), next_step(a.y, b.y))


def main():
    grid = [l.strip() for l in sys.stdin if l.strip()]

    def within_bounds(p: Position):
        return 0 <= p.x < len(grid[0]) and 0 <= p.y < len(grid)

    def get_char_positions(char: str):
        return [
            Position(x, y)
            for y, row in enumerate(grid)
            for x, c in enumerate(row)
            if c == char
        ]

    antennas_characters = set("".join(grid)) - set(".")
    all_antinodes = set(
        node
        for a in antennas_characters
        for p1, p2 in permutations(get_char_positions(a), 2)
        if within_bounds(node := next_node(p1, p2))
    )

    solution = len(all_antinodes)
    print(solution)


if __name__ == "__main__":
    main()
