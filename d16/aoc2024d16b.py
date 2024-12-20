from heapq import heappush, heappop
from itertools import product
import sys
from typing import TextIO
from collections import defaultdict


DIRECTIONS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
TURN_COST = 1000
MOVE_COST = 1


class ROGrid:
    def __init__(self, stream: TextIO):
        self.data = [l.strip() for l in stream if l.strip()]
        self.width = len(self.data[0])
        self.height = len(self.data)

    def __getitem__(self, key):
        if not isinstance(key, tuple):
            raise TypeError("Grid indices must be tuples")
        x, y = key
        return self.data[y][x]


def find_all_shortest_paths(grid, start, end):
    # distances[(pos, direction)] = cost
    distances = defaultdict(lambda: float("inf"))

    # paths[(pos, direction)] = list of paths reaching this state
    paths = defaultdict(list)

    # Initialize with start position
    initial_dir = "?"  # Dummy direction
    initial_state = (start, initial_dir)
    distances[initial_state] = 0
    paths[initial_state] = [[start]]

    queue = [(0, *initial_state)]

    while queue:
        curr_dist, curr, curr_direction = heappop(queue)
        curr_state = (curr, curr_direction)

        if curr_dist > distances[curr_state]:
            continue

        curr_x, curr_y = curr
        for direction, (dx, dy) in DIRECTIONS.items():
            neighbor = (x, y) = (curr_x + dx, curr_y + dy)

            if (
                not (0 <= x < grid.width and 0 <= y < grid.height)
                or grid[neighbor] == "#"
            ):
                continue

            # Calculate new distance based on turn cost
            if set([curr_direction, direction]) in [{"^", "v"}, {"<", ">"}]:
                new_dist = curr_dist + 2 * TURN_COST + MOVE_COST
            elif len(set([curr_direction, direction])) == 2:
                new_dist = curr_dist + TURN_COST + MOVE_COST
            else:
                new_dist = curr_dist + MOVE_COST

            new_state = (neighbor, direction)

            if new_dist > distances[new_state]:
                continue

            if new_dist < distances[new_state]:
                # Found a better path, clear existing paths
                paths[new_state] = []
                distances[new_state] = new_dist
                heappush(queue, (new_dist, neighbor, direction))

            # Add all possible paths to this state
            for p in paths[curr_state]:
                paths[new_state].append(p + [neighbor])

    end_paths = []
    min_dist = float("inf")

    for direction in DIRECTIONS:
        state = (end, direction)
        if distances[state] < min_dist:
            min_dist = distances[state]
            end_paths = paths[state]
        elif distances[state] == min_dist:
            end_paths.extend(paths[state])

    return min_dist, end_paths


def main():
    grid = ROGrid(sys.stdin)

    def look_for(c):
        return next(
            v for v in product(range(grid.width), range(grid.height)) if grid[v] == c
        )

    start = look_for("S")
    end = look_for("E")

    min_dist, all_paths = find_all_shortest_paths(grid, start, end)
    solution = len(set(v for p in all_paths for v in p))
    print(solution)


if __name__ == "__main__":
    main()
