from functools import cache
from itertools import product
import sys

# I am definitely not proud of that one...


@cache
def neighbors(x, y):
    return [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ]


def get_cleaned_sides(sides):
    cleaned = set()
    sides = sorted(sides)
    while sides:
        n, current, pos = sides.pop(0)
        if (n, current, pos + 1) not in sides:
            cleaned.add((n, current, pos))
    return cleaned


def calculate_price(region):
    area = len(region)

    vertical = [
        (nx, x, y)
        for x, y in region
        for nx, ny in neighbors(x, y)
        if (nx, ny) not in region and x != nx
    ]

    horizontal = [
        (ny, y, x)
        for x, y in region
        for nx, ny in neighbors(x, y)
        if (nx, ny) not in region and y != ny
    ]

    return area * (
        len(get_cleaned_sides(vertical)) + len(get_cleaned_sides(horizontal))
    )


def main():
    grid = [list(line.strip()) for line in sys.stdin if line.strip()]
    grid_height = len(grid)
    grid_width = len(grid[0])

    processed = set()

    def out_of_bounds(x, y):
        return x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y])

    def get_region(x, y):
        region = set()
        to_process = {(x, y)}
        c = grid[y][x]
        while to_process:
            x, y = to_process.pop()
            if out_of_bounds(x, y) or (x, y) in region or grid[y][x] != c:
                continue
            region.add((x, y))
            for nx, ny in neighbors(x, y):
                to_process.add((nx, ny))
        return region

    total = 0
    for y, x in product(range(grid_height), range(grid_width)):
        if (x, y) in processed:
            continue
        region = get_region(x, y)
        total += calculate_price(region)
        processed.update(region)

    print(total)


if __name__ == "__main__":
    main()
