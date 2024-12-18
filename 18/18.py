from collections import deque


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def parse_input() -> list[tuple[int, int]]:
    with open("input.txt", "r") as file:
        return [tuple(map(int, line.strip().split(","))) for line in file]


def shortest_path(corrupted: set[tuple[int, int]], size: int) -> int:

    queue = deque([(0, 0, 0)])
    visited = set()
    visited.add((0, 0))

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == (size - 1, size - 1):
            return dist

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < size
                and 0 <= ny < size
                and (nx, ny) not in corrupted
                and (nx, ny) not in visited
            ):
                queue.append((nx, ny, dist + 1))
                visited.add((nx, ny))

    return -1


def main1() -> int:
    falling_bytes = parse_input()

    size = 71
    n_falling_bytes = 1024
    corrupted = set(falling_bytes[:n_falling_bytes])

    return shortest_path(corrupted, size)


def main2() -> str:
    falling_bytes = parse_input()

    size = 71
    n_falling_bytes = len(falling_bytes)
    corrupted = set(falling_bytes)

    while shortest_path(corrupted, size) == -1:
        n_falling_bytes -= 1
        corrupted.remove(falling_bytes[n_falling_bytes])

    return f"{falling_bytes[n_falling_bytes][0]},{falling_bytes[n_falling_bytes][1]}"


if __name__ == "__main__":
    print(main1())
    print(main2())
