from heapq import heappush, heappop
from itertools import product
import sys
from typing import TextIO


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


DIRECTIONS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
TURN_COST = 1000
MOVE_COST = 1


def main():
    grid = ROGrid(sys.stdin)

    def look_for(c):
        return next(
            v for v in product(range(grid.width), range(grid.height)) if grid[v] == c
        )

    start = look_for("S")
    end = look_for("E")

    def dijkstra():
        direction = "?"
        queue = [(0, start, direction)]
        distances = {start: 0}
        came_from = {}

        while queue:
            curr_dist, curr, curr_direction = heappop(queue)

            if curr == end:
                return curr_dist

            curr_x, curr_y = curr
            for direction, (dx, dy) in DIRECTIONS.items():
                neighbor = (x, y) = (curr_x + dx, curr_y + dy)

                if (
                    not (0 <= x < grid.width and 0 <= y < grid.height)
                    or grid[neighbor] == "#"
                ):
                    continue

                # 90 degrees rotation costs TURN_COST
                if set([curr_direction, direction]) in [{"^", "v"}, {"<", ">"}]:
                    dist = curr_dist + 2 * TURN_COST + MOVE_COST
                elif len(set([curr_direction, direction])) == 2:
                    dist = curr_dist + TURN_COST + MOVE_COST
                else:
                    dist = curr_dist + MOVE_COST

                if neighbor not in distances or dist < distances[neighbor]:
                    distances[neighbor] = dist
                    came_from[neighbor] = curr
                    heappush(queue, (dist, neighbor, direction))

        return -1

    solution = dijkstra()
    print(solution)


if __name__ == "__main__":
    main()
