from itertools import batched, starmap
from operator import mul


def disk_map_to_file_layout(disk_map):
    if len(disk_map) % 2 != 0:
        disk_map = disk_map + "0"

    res = [
        x
        for idx, (file, free) in enumerate(batched(map(int, disk_map), 2))
        for x in [idx] * file + ["."] * free
    ]
    return res


def find_sublist(l, subl, start=0):
    subl_len = len(subl)
    for idx in range(max(start, 0), len(l)):
        if l[idx : idx + subl_len] == subl:
            return idx
    return -1


def main():
    disk_map = input()
    file_layout = disk_map_to_file_layout(disk_map)

    # memoize the last gap index for each size of gap
    size_gap_indexes = [0] * 10

    i = len(file_layout) - 1
    while i > 0:
        c = file_layout[i]
        if c == ".":
            i -= 1
            continue

        # we have maximum 10 occurrences of the same character
        occur = file_layout[max(0, i - 10) : i + 1].count(c)

        gap = ["."] * occur
        gap_start = find_sublist(file_layout, gap, size_gap_indexes[occur])
        size_gap_indexes[occur] = gap_start
        if -1 < gap_start < i:
            # there is probably a smarter way to do this
            file_layout[gap_start : gap_start + occur] = [c] * occur
            file_layout[i - occur + 1 : i + 1] = gap

        i -= occur

    def safe_mul(a, b):
        if b == ".":
            return 0
        return a * b

    solution = sum(starmap(safe_mul, enumerate(file_layout)))
    print(solution)


if __name__ == "__main__":
    main()
