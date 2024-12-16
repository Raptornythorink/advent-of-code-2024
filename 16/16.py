from sys import setrecursionlimit

setrecursionlimit(10**4)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
TURNS = {0: (3, 1), 1: (0, 2), 2: (1, 3), 3: (2, 0)}


def parse_input() -> tuple[set[tuple[int, int]], tuple[int, int], tuple[int, int]]:
    walls = set()
    start_pos = (0, 0)
    end_pos = (0, 0)

    with open("input.txt", "r") as file:
        for i, line in enumerate(file):
            for j, c in enumerate(line.strip()):
                if c == "#":
                    walls.add((i, j))
                elif c == "S":
                    start_pos = (i, j)
                elif c == "E":
                    end_pos = (i, j)

    return walls, start_pos, end_pos


def find_all_paths(
    walls: set[tuple[int, int]],
    start: tuple[int, int],
    end: tuple[int, int],
) -> list[list[tuple[int, int]]]:
    memo = {}

    def dfs(
        current: tuple[int, int],
        path: list[tuple[int, int]],
        direction: int,
        current_score: int,
    ) -> None:
        if current == end:
            paths.append(path[:])
            return

        if (current, direction) in memo and memo[(current, direction)] < current_score:
            return

        memo[(current, direction)] = current_score

        for d in [direction, *TURNS[direction]]:
            dx, dy = DIRECTIONS[d]
            neighbor = (current[0] + dx, current[1] + dy)
            if neighbor not in visited and neighbor not in walls:
                visited.add(neighbor)
                path.append(neighbor)
                dfs(neighbor, path, d, current_score + (1 if direction == d else 1000))
                path.pop()
                visited.remove(neighbor)

    paths = []
    visited = {start}
    initial_direction = 0
    dfs(start, [start], initial_direction, 0)

    return paths


def get_path_score(path: list[tuple[int, int]]) -> int:
    turns = 0
    if path[1][1] != path[0][1] + 1:
        turns = 1
    for i in range(1, len(path) - 1):
        dx1, dy1 = path[i][0] - path[i - 1][0], path[i][1] - path[i - 1][1]
        dx2, dy2 = path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1]
        if dx1 * dy2 != dx2 * dy1:
            turns += 1
    return 1000 * turns + len(path) - 1


def main1() -> int:
    walls, start_pos, end_pos = parse_input()

    paths = find_all_paths(walls, start_pos, end_pos)

    return min(get_path_score(path) for path in paths)


def main2() -> int:
    walls, start_pos, end_pos = parse_input()

    paths = find_all_paths(walls, start_pos, end_pos)

    best_score = float("inf")
    best_score_paths = []
    for path in paths:
        score = get_path_score(path)
        if score < best_score:
            best_score = score
            best_score_paths = [path]
        elif score == best_score:
            best_score_paths.append(path)

    best_sits = set()
    for path in best_score_paths:
        best_sits.update(path)

    return len(best_sits)


if __name__ == "__main__":
    print(main1())
    print(main2())
