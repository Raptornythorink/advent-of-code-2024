from collections import Counter
from math import prod


def parse_input() -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    with open("input.txt") as file:
        robots_pos = []
        robots_vel = []

        for line in file:
            px, py = map(int, line[2:].split()[0].split(","))
            vx, vy = map(int, line.strip().split("v=")[1].split(","))

            robots_pos.append((px, py))
            robots_vel.append((vx, vy))

        return robots_pos, robots_vel


def main1() -> int:
    robots_pos, robots_vel = parse_input()

    n_robots = len(robots_pos)
    n, m = 101, 103
    nb_iterations = 100

    for _ in range(nb_iterations):
        robots_pos = [
            (
                (robots_pos[i][0] + robots_vel[i][0]) % n,
                (robots_pos[i][1] + robots_vel[i][1]) % m,
            )
            for i in range(n_robots)
        ]

    quadrants = [0] * 4

    for robot_pos in robots_pos:
        if robot_pos[0] < n // 2 and robot_pos[1] < m // 2:
            quadrants[0] += 1
        elif robot_pos[0] < n // 2 and robot_pos[1] > m // 2:
            quadrants[1] += 1
        elif robot_pos[0] > n // 2 and robot_pos[1] < m // 2:
            quadrants[2] += 1
        elif robot_pos[0] > n // 2 and robot_pos[1] > m // 2:
            quadrants[3] += 1

    return prod(quadrants)


def main2() -> int:
    robots_pos, robots_vel = parse_input()

    n_robots = len(robots_pos)
    n, m = 101, 103
    max_line_count, max_line_second = 0, 0
    max_column_count, max_column_second = 0, 0

    for second in range(max(n, m)):
        robots_pos = [
            (
                (robots_pos[i][0] + robots_vel[i][0]) % n,
                (robots_pos[i][1] + robots_vel[i][1]) % m,
            )
            for i in range(n_robots)
        ]

        line_counts = Counter(x for x, _ in robots_pos)
        column_counts = Counter(y for _, y in robots_pos)

        current_max_line_count = max(line_counts.values())
        if current_max_line_count > max_line_count:
            max_line_count = current_max_line_count
            max_line_second = second

        current_max_column_count = max(column_counts.values())
        if current_max_column_count > max_column_count:
            max_column_count = current_max_column_count
            max_column_second = second

    for i in range(n):
        for j in range(m):
            eval_i = i * m + max_column_second
            eval_j = j * n + max_line_second
            if eval_i < eval_j:
                break
            if eval_i == eval_j:
                return eval_i + 1

    return -1


if __name__ == "__main__":
    print(main1())
    print(main2())
