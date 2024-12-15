from collections import defaultdict


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIAGONALS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
CONVEX_CORNERS = [(DIRECTIONS[i], DIRECTIONS[(i + 1) % 4]) for i in range(4)]
CONCAV_CORNERS = [(CONVEX_CORNERS[i], DIAGONALS[i]) for i in range(4)]


def parse_input() -> defaultdict[str, set[tuple[int, int]]]:
    with open("input.txt", "r") as file:
        plot = [list(line.strip()) for line in file]
    n, m = len(plot), len(plot[0])
    plants_dict = defaultdict(set)
    for i in range(n):
        for j in range(m):
            plants_dict[plot[i][j]].add((i, j))
    return plants_dict


def get_plant_regions(plants: set[tuple[int, int]]) -> list[set[tuple[int, int]]]:
    regions = []
    visited = set()

    for plant in plants:
        if plant in visited:
            continue

        region = set()
        stack = [plant]

        while stack:
            i, j = stack.pop()

            if (i, j) in visited:
                continue

            visited.add((i, j))
            region.add((i, j))

            for di, dj in DIRECTIONS:
                if (i + di, j + dj) in plants:
                    stack.append((i + di, j + dj))

        regions.append(region)

    return regions


def get_area(region: set[tuple[int, int]]) -> int:
    return len(region)


def get_perimeter(region: set[tuple[int, int]]) -> int:
    perimeter = 0
    for i, j in region:
        for di, dj in DIRECTIONS:
            if (i + di, j + dj) not in region:
                perimeter += 1
    return perimeter


def get_sides(region: set[tuple[int, int]]) -> int:
    sides = 0
    for i, j in region:
        for (di1, dj1), (di2, dj2) in CONVEX_CORNERS:
            if (i + di1, j + dj1) not in region and (i + di2, j + dj2) not in region:
                sides += 1

        for ((di1, dj1), (di2, dj2)), (di3, dj3) in CONCAV_CORNERS:
            if (
                (i + di1, j + dj1) in region
                and (i + di2, j + dj2) in region
                and not (i + di3, j + dj3) in region
            ):
                sides += 1
    return sides


def main1() -> int:
    plants_dict = parse_input()
    total_price = 0

    for plant in plants_dict:
        regions = get_plant_regions(plants_dict[plant])

        for region in regions:
            area = get_area(region)
            perimeter = get_perimeter(region)
            total_price += area * perimeter

    return total_price


def main2() -> int:
    plants_dict = parse_input()
    total_price = 0

    for plant in plants_dict:
        regions = get_plant_regions(plants_dict[plant])

        for region in regions:
            area = get_area(region)
            sides = get_sides(region)
            total_price += area * sides

    return total_price


if __name__ == "__main__":
    print(main1())
    print(main2())
