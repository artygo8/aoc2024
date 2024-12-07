import sys
from typing import NamedTuple
from operator import add, mul


class Equation(NamedTuple):
    total: int
    numbers: tuple[int, ...]


def parse_line(line) -> Equation:
    total, _op, numbers = line.partition(": ")
    return Equation(int(total), tuple(map(int, numbers.split())))


def possible_values(numbers: tuple[int, ...]):
    values = set(numbers[:1])
    for n in numbers[1:]:
        values = {operator(v, n) for v in values for operator in (add, mul)}
    return values


def main():
    equations = [parse_line(line) for line in sys.stdin if line.strip()]
    solution = sum(
        eq.total for eq in equations if eq.total in possible_values(eq.numbers)
    )
    print(solution)


if __name__ == "__main__":
    main()
