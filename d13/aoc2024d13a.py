import sys
from dataclasses import dataclass
from math import sqrt
from typing import NamedTuple


@dataclass
class Vector:
    x: int
    y: int

    def divisible_by(self, other: "Vector"):
        if self.x % other.x != 0:
            return False
        return self.y / other.y == self.x / other.x

    def mag(self):
        return sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(other * self.x, other * self.y)

    def __rmul__(self, other):
        return Vector(other * self.x, other * self.y)


class ClawMachine(NamedTuple):
    button_a: Vector
    button_b: Vector
    prize: Vector


def next_claw_machine():
    def _parse_next_line(sep):
        x, y = map(lambda t: int(t.split(sep)[1]), next(sys.stdin).split(",")[-2:])
        return Vector(x, y)

    while True:
        try:
            yield ClawMachine(
                _parse_next_line("+"),
                _parse_next_line("+"),
                _parse_next_line("="),
            )
            next(sys.stdin)  # Skip empty line
        except StopIteration:
            break


def solve(claw_machine: ClawMachine) -> tuple[int, int]:
    for i in range(101):
        left = claw_machine.prize - claw_machine.button_a * i
        if left.divisible_by(claw_machine.button_b):
            j = round(left.mag() / claw_machine.button_b.mag())
            return i * 3, j
    return (0, 0)


def main():
    solution = sum(sum(solve(claw_machine)) for claw_machine in next_claw_machine())
    print(solution)


if __name__ == "__main__":
    main()
