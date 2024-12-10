DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def parse_input() -> list[list[int]]:
    grid: list[list[int]] = []
    with open("input.txt", "r") as file:
        for line in file:
            grid.append([int(num) for num in line.strip()])
    return grid


def get_score(grid: list[list[int]], i: int, j: int) -> int:
    n, m = len(grid), len(grid[0])

    curr_height = 0
    reachable = set()
    reachable.add((i, j))

    while curr_height < 9:
        new_reachable = set()
        for x, y in reachable:
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == curr_height + 1:
                    new_reachable.add((nx, ny))
        reachable = new_reachable
        curr_height += 1

    return len(reachable)


def get_rating(grid: list[list[int]], i: int, j: int) -> int:
    n, m = len(grid), len(grid[0])

    parents = {}
    curr_height = 0
    reachable = [set() for _ in range(10)]
    reachable[0].add((i, j))

    while curr_height < 9:
        for x, y in reachable[curr_height]:
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == curr_height + 1:
                    reachable[curr_height + 1].add((nx, ny))
                    if (nx, ny) not in parents:
                        parents[(nx, ny)] = []
                    parents[(nx, ny)].append((x, y))
        curr_height += 1

    rating = 0
    stack = list(reachable[9])
    while stack:
        x, y = stack.pop()
        if (x, y) == (i, j):
            rating += 1
        else:
            stack += parents[(x, y)]

    return rating


def main1() -> int:
    grid = parse_input()
    n, m = len(grid), len(grid[0])
    total_score = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                total_score += get_score(grid, i, j)
    return total_score


def main2() -> int:
    grid = parse_input()
    n, m = len(grid), len(grid[0])
    total_rating = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                total_rating += get_rating(grid, i, j)
    return total_rating


if __name__ == "__main__":
    print(main1())
    print(main2())
