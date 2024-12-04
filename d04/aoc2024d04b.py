import sys


def is_xmas(grid, x, y):
    def tlbr(i):
        # X00
        # 0X0
        # 00X
        return grid[y + i][x + i]

    def trbl(i):
        # 00X
        # 0X0
        # X00
        return grid[y + i][x + 2 - i]

    def is_mas(word):
        return word in ('MAS', 'SAM')

    try:
        return all(
            is_mas(''.join(fct(i) for i in range(3))) for fct in (tlbr, trbl)
        )
    except IndexError:
        pass

    return False


def main():
    grid = [l.strip() for l in sys.stdin if l.strip()]
    solution = sum(
        is_xmas(grid, i, j)
        for j in range(len(grid))
        for i in range(len(grid[j]))
    )
    print(solution)


if __name__ == "__main__":
    main()
