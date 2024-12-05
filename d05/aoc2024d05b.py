from itertools import combinations, permutations
import sys
from typing import Sequence


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
        return all((a, b) in ordering_rules for a, b in combinations(page, 2))

    def order(page: Sequence[int]) -> list:
        if len(page) == 1:
            return list(page)

        new_items = {pair for pair in permutations(page, 2) if pair in ordering_rules}
        firsts, seconds = map(set, zip(*new_items))
        items = set(page)
        start = items - seconds
        end = items - firsts
        center = items - start - end
        return list(start) + order(list(center)) + list(end)

    solution = sum(middle(order(p)) for p in pages_to_produce if not is_ordered(p))
    print(solution)


if __name__ == "__main__":
    main()
