from functools import cache


TOTAL_TURNS = 75


def new_stones(stone: str) -> list[str]:
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        size = len(stone) // 2
        return [stone[:size], stone[size:].lstrip("0") or "0"]
    else:
        return [str(int(stone) * 2024)]


@cache
def total_stones(stone: str, total: int) -> int:
    if total == 0:
        return 1
    return sum([total_stones(new_st, total - 1) for new_st in new_stones(stone)])


def main():
    stones = input().split()
    total = sum([total_stones(st, TOTAL_TURNS) for st in stones])
    print(total)


if __name__ == "__main__":
    main()
