from functools import cache
import sys


def main():
    grid = [list(line.strip()) for line in sys.stdin if line.strip()]

    @cache
    def neighbors(x, y):
        neighs = []
        if x > 0:
            neighs.append((x - 1, y))
        if x < len(grid[y]) - 1:
            neighs.append((x + 1, y))
        if y > 0:
            neighs.append((x, y - 1))
        if y < len(grid) - 1:
            neighs.append((x, y + 1))
        return neighs

    processed = set()

    def calculate_price(x, y):
        region = {(x, y)}
        to_process = set(region)
        while to_process:
            x, y = to_process.pop()
            if (x, y) in processed:
                continue

            c = grid[y][x]
            for nx, ny in neighbors(x, y):
                if grid[ny][nx] == c:
                    region.add((nx, ny))
                    to_process.add((nx, ny))

            processed.add((x, y))

        area = len(region)
        perimeter = sum(
            [4 - len([n for n in neighbors(x, y) if n in region]) for x, y in region]
        )
        return area * perimeter

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (x, y) in processed:
                continue
            total += calculate_price(x, y)

    print(total)


if __name__ == "__main__":
    main()
