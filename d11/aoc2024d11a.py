from functools import cache


TOTAL_TURNS = 25


@cache
def new_stones(stone: str) -> list[str]:
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        size = len(stone) // 2
        return [stone[:size], stone[size:].lstrip("0") or "0"]
    else:
        return [str(int(stone) * 2024)]


def main():
    stones = input().split()
    for turn in range(TOTAL_TURNS):
        stones = [new_st for st in stones for new_st in new_stones(st)]
    solution = len(stones)
    print(solution)


if __name__ == "__main__":
    main()
