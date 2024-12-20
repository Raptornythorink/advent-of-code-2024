DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def parse_input() -> (
    tuple[set[tuple[int, int]], tuple[int, int], tuple[int, int], tuple]
):
    walls = set()
    start = None
    end = None

    with open("input.txt", "r") as file:
        for y, line in enumerate(file):
            for x, char in enumerate(line):
                if char == "#":
                    walls.add((x, y))
                elif char == "S":
                    start = (x, y)
                elif char == "E":
                    end = (x, y)

    return walls, start, end, (y, x)


def get_path(
    walls: set[tuple[int, int]], start: tuple[int, int], end: tuple[int, int]
) -> list[tuple[int, int]]:
    queue = [(start, [start])]
    visited = {start}

    while queue:
        (x, y), path = queue.pop(0)

        if (x, y) == end:
            return path

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in walls and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return []


def get_coords_n_away(
    x: int, y: int, n: int, size: tuple[int, int]
) -> set[tuple[int, int]]:
    coords = set()

    for dx in range(-n, n + 1):
        dy = n - abs(dx)
        for sign in [-1, 1]:
            nx, ny = x + dx, y + dy * sign
            if 0 <= nx < size[1] and 0 <= ny < size[0]:
                coords.add((nx, ny))

    return coords


def get_coords_up_to_n_away(
    x: int, y: int, n: int, size: tuple[int, int]
) -> dict[tuple[int, int], int]:
    coords = {}

    for dist in range(2, n + 1):
        for dx in range(-dist, dist + 1):
            dy = dist - abs(dx)
            for sign in [-1, 1]:
                nx, ny = x + dx, y + dy * sign
                if 0 <= nx < size[1] and 0 <= ny < size[0]:
                    coords[(nx, ny)] = dist

    return coords


def main1() -> int:
    walls, start, end, size = parse_input()
    path = get_path(walls, start, end)

    ref_time = len(path)
    result = 0

    for i in range(ref_time - 100):
        x1, y1 = path[i]
        coords = get_coords_n_away(x1, y1, 2, size)
        for j in range(i + 101, ref_time):
            if path[j] in coords:
                result += 1

    return result


def main2() -> int:
    walls, start, end, size = parse_input()
    path = get_path(walls, start, end)

    ref_time = len(path)
    result = 0

    for i in range(ref_time - 100):
        x1, y1 = path[i]
        coords = get_coords_up_to_n_away(x1, y1, 20, size)
        for j in range(i + 100, ref_time):
            if path[j] in coords and j - i - coords[path[j]] >= 100:
                result += 1

    return result


if __name__ == "__main__":
    print(main1())
    print(main2())
