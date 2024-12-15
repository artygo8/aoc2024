from dataclasses import dataclass
from itertools import count
import sys


@dataclass(frozen=True)
class Vector:
    x: int
    y: int

    def value(self):
        return self.x + self.y * 100

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, number):
        return Vector(self.x * number, self.y * number)

    def __rmul__(self, number):
        return Vector(self.x * number, self.y * number)


DIRECTIONS = {
    "<": Vector(-1, 0),
    ">": Vector(1, 0),
    "^": Vector(0, -1),
    "v": Vector(0, 1),
}


def parse_grid() -> list[list]:
    grid = []
    for l in sys.stdin:
        if not l.strip():
            break
        grid.append(list(l.strip()))
    return grid


def parse_moves() -> str:
    return "".join(line.strip() for line in sys.stdin)


def main():
    grid = parse_grid()
    moves = parse_moves()

    rp = next(
        Vector(i, j)
        for j, row in enumerate(grid)
        for i, char in enumerate(row)
        if char == "@"
    )
    for move in moves:
        new_rp = DIRECTIONS[move] + rp
        for step in count():
            tp = step * DIRECTIONS[move] + new_rp  # tile position
            tile = grid[tp.y][tp.x]
            if tile == "#":
                break
            if tile == ".":
                grid[rp.y][rp.x], grid[new_rp.y][new_rp.x] = ".", "@"
                rp = new_rp
                if tp != new_rp:
                    grid[tp.y][tp.x] = "O"
                break

    solution = sum(
        Vector(i, j).value()
        for j, row in enumerate(grid)
        for i, char in enumerate(row)
        if char == "O"
    )
    print(solution)


if __name__ == "__main__":
    main()
