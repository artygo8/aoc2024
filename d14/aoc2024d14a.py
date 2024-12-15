import sys
from typing import NamedTuple


WIDTH, HEIGHT = (101, 103)
# WIDTH, HEIGHT = (11, 7)


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


def quadrant(position):
    if position.x < WIDTH // 2:
        if position.y < HEIGHT // 2:
            return 1
        elif position.y > HEIGHT // 2:
            return 3
    elif position.x > WIDTH // 2:
        if position.y < HEIGHT // 2:
            return 2
        elif position.y > HEIGHT // 2:
            return 4
    return 0


def main():
    robots = [r for r in parse_robots()]
    future_positions = [position_in_time(r, 100) for r in robots]
    quadrants = [quadrant(p) for p in future_positions]

    total = 1
    for i in range(1, 5):
        total *= quadrants.count(i)

    print(total)


if __name__ == "__main__":
    main()
