import sys
from typing import NamedTuple
from itertools import count


WIDTH, HEIGHT = (101, 103)


neighbors = {
    (x, y): {
        (x, y - 1),
        (x, y + 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x + 1, y + 1),
    }
    for y in range(HEIGHT)
    for x in range(WIDTH)
}


class Robot(NamedTuple):
    position: tuple[int, int]
    velocity: tuple[int, int]


def position_in_time(robot: Robot, time: int) -> tuple[int, int]:
    return (
        (robot.position[0] + robot.velocity[0] * time) % WIDTH,
        (robot.position[1] + robot.velocity[1] * time) % HEIGHT,
    )


def parse_robots():
    for line in sys.stdin:
        if not line:
            break
        position, velocity = map(
            lambda v: map(int, v.split("=")[-1].split(",")), line.split()
        )
        yield Robot(tuple(position), tuple(velocity))  # type: ignore


def display_positions(positions: set):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            pos_tuple = (x, y)
            if pos_tuple in positions:
                print("#", end="")
            else:
                print(".", end="")
        print()


def neighbors_level(positions: set):
    return (
        sum(1 for p in positions for n in neighbors[p] if n in positions)
        / len(positions)
        / 8
    )


def main():
    robots = [*parse_robots()]

    for total in count():
        future_positions = set(position_in_time(r, total) for r in robots)
        # I expect there are a lot of neighbors to draw a picture
        if neighbors_level(future_positions) > 0.25:
            display_positions(future_positions)
            print(total)
            break


if __name__ == "__main__":
    main()
