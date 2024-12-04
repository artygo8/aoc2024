import sys


def parse_input() -> tuple[tuple, ...]:
    # Returns the two columns as tuples of integers
    lc, rc = zip(*[map(int, l.strip().split()) for l in sys.stdin if l.strip()])
    return lc, rc


def main():
    solution = sum(abs(l - r) for l, r in zip(*map(sorted, parse_input())))
    print(solution)


if __name__ == "__main__":
    main()
