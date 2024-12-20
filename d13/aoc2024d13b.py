import sys
from typing import NamedTuple


SHIFT = 10000000000000


class Vector(NamedTuple):
    x: int
    y: int


class ClawMachine(NamedTuple):
    button_a: Vector
    button_b: Vector
    prize: Vector


def next_claw_machine():
    def _parse_next_line(sep):
        x, y = map(lambda t: int(t.split(sep)[1]), next(sys.stdin).split(",")[-2:])
        if sep == "=":
            x += SHIFT
            y += SHIFT
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
    p = claw_machine.prize
    a = claw_machine.button_a
    b = claw_machine.button_b
    # Using Cramer's rule or matrix methods:
    # i = (p₁b₂ - b₁p₂)/(a₁b₂ - b₁a₂)
    # j = (a₁p₂ - p₁a₂)/(a₁b₂ - b₁a₂)
    i = (p.x * b.y - b.x * p.y) / (a.x * b.y - b.x * a.y)
    j = (a.x * p.y - p.x * a.y) / (a.x * b.y - b.x * a.y)
    if i.is_integer() and j.is_integer():
        return (int(i) * 3, int(j))
    return (0, 0)


def main():
    solution = sum(sum(solve(claw_machine)) for claw_machine in next_claw_machine())
    print(solution)


if __name__ == "__main__":
    main()
