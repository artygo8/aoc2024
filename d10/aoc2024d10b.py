import sys

NUMBERS = "0123456789"


def main():
    grid = sys.stdin.read().strip().split("\n")
    positions = {
        c: {
            (x, y)
            for y, row in enumerate(grid)
            for x, cell in enumerate(row)
            if cell == c
        }
        for c in NUMBERS
    }
    neighbors = {
        (x, y): {
            (x, y - 1),
            (x, y + 1),
            (x - 1, y),
            (x + 1, y),
        }
        for y, row in enumerate(grid)
        for x, cell in enumerate(row)
    }

    numbers = iter(NUMBERS)
    trail_starts = [{p} for p in positions[next(numbers)]]
    for c in numbers:
        trail_starts = [
            [neigh for t in ts for neigh in neighbors[t] if neigh in positions[c]]
            for ts in trail_starts
        ]

    solution = sum(map(len, trail_starts))
    print(solution)


if __name__ == "__main__":
    main()
