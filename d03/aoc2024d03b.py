import re
import sys


def main():
    pattern = r'mul\((\d+),(\d+)\)|(don\'t\(\)|do\(\))'

    mul_enabled = True
    total = 0
    for a, b, c in re.findall(pattern, sys.stdin.read()):
        if c.startswith("do"):
            mul_enabled = c == "do()"
        elif mul_enabled:
            total += int(a) * int(b)

    print(total)


if __name__ == "__main__":
    main()
