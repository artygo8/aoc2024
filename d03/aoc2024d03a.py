import re
import sys


def main():
    pattern = r'mul\((\d+),(\d+)\)'
    solution = sum(
        int(a) * int(b) for a, b in re.findall(pattern, sys.stdin.read())
    )
    print(solution)


if __name__ == "__main__":
    main()
