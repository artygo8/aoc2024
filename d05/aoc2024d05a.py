from itertools import combinations
import sys


def parse_ordering_rules() -> set[tuple]:
    ordering_rules = set()
    for l in sys.stdin:
        if not l.strip():
            break
        ordering_rules.add(tuple(map(int, l.strip().split("|"))))

    return ordering_rules


def parse_pages_to_produce() -> list[tuple]:
    return [tuple(map(int, l.strip().split(","))) for l in sys.stdin]


def middle(lst):
    return lst[len(lst) // 2]


def main():
    ordering_rules = parse_ordering_rules()
    pages_to_produce = parse_pages_to_produce()

    def is_ordered(page):
        return not any((b, a) in ordering_rules for a, b in combinations(page, 2))

    solution = sum(is_ordered(p) * middle(p) for p in pages_to_produce)
    print(solution)


if __name__ == "__main__":
    main()
