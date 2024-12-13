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


def main():
    disk_map = input()
    file_layout = disk_map_to_file_layout(disk_map)
    try:
        for i in range(len(file_layout)):
            while file_layout[i] == ".":
                file_layout[i] = file_layout.pop(-1)
    except IndexError:
        pass
    solution = sum(starmap(mul, enumerate(file_layout)))
    print(solution)


if __name__ == "__main__":
    main()
