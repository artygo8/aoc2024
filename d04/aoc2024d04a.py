import sys


def get_words(grid, x, y):
    def go_down(i):
        return grid[y + i][x]
    
    def go_right(i):
        return grid[y][x + i]

    def go_down_right(i):
        return grid[y + i][x + i]

    def go_down_left(i):
        if i > x:
            raise IndexError
        return grid[y + i][x - i]

    words = []
    for f in (go_down, go_right, go_down_right, go_down_left):
        try:
            word = "".join(f(i) for i in range(4))
        except IndexError:
            continue

        words.append(word)
        words.append(word[::-1])

    return words


def main():
    grid = [l.strip() for l in sys.stdin if l.strip()]
    solution = sum(
        get_words(grid, i, j).count('XMAS')
        for j in range(len(grid))
        for i in range(len(grid[j]))
    )
    print(solution)


if __name__ == "__main__":
    main()
