DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
XMAS = "XMAS"
MAS_COMBINATIONS = set(
    [
        ("M", "S", "M", "S"),
        ("S", "M", "S", "M"),
        ("M", "M", "S", "S"),
        ("S", "S", "M", "M"),
    ]
)


def count_xmas(grid: list[str], x: int, y: int) -> int:
    count = 0
    n, m = len(grid), len(grid[0])

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        for i in range(1, 4):
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            if grid[nx][ny] != XMAS[i]:
                break
            nx += dx
            ny += dy
        else:
            count += 1

    return count


def is_mas(grid: list[str], x: int, y: int) -> bool:
    n, m = len(grid), len(grid[0])

    if x < 1 or x >= n - 1 or y < 1 or y >= m - 1:
        return False

    return (
        grid[x - 1][y - 1],
        grid[x + 1][y - 1],
        grid[x - 1][y + 1],
        grid[x + 1][y + 1],
    ) in MAS_COMBINATIONS


def main1() -> int:
    with open("input.txt", "r") as file:
        grid: list[str] = [line.strip() for line in file]

    n, m = len(grid), len(grid[0])
    xmas_count = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "X":
                xmas_count += count_xmas(grid, i, j)

    return xmas_count


def main2() -> int:
    with open("input.txt", "r") as file:
        grid: list[str] = [line.strip() for line in file]

    n, m = len(grid), len(grid[0])
    mas_count = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "A":
                mas_count += is_mas(grid, i, j)

    return mas_count


if __name__ == "__main__":
    print(main1())
    print(main2())
