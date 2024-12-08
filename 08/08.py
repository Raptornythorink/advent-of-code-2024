def parse_input() -> tuple[int, int, dict[str, list[tuple[int, int]]]]:
    antennas: dict[str, list[tuple[int, int]]] = {}

    with open("input.txt", "r") as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                if char != ".":
                    if char not in antennas:
                        antennas[char] = []
                    antennas[char].append((i, j))

    return i + 1, j + 1, antennas


def main1() -> int:
    n, m, antennas = parse_input()

    antinodes = set()
    for freq in antennas:
        n_antennas = len(antennas[freq])
        for i in range(n_antennas - 1):
            for j in range(i + 1, n_antennas):
                x1, y1 = antennas[freq][i]
                x2, y2 = antennas[freq][j]

                xa, ya = 2 * x2 - x1, 2 * y2 - y1
                if 0 <= xa < n and 0 <= ya < m:
                    antinodes.add((xa, ya))

                xb, yb = 2 * x1 - x2, 2 * y1 - y2
                if 0 <= xb < n and 0 <= yb < m:
                    antinodes.add((xb, yb))

    return len(antinodes)


def main2() -> int:
    n, m, antennas = parse_input()

    antinodes = set()
    for freq in antennas:
        n_antennas = len(antennas[freq])
        for i in range(n_antennas - 1):
            for j in range(i + 1, n_antennas):
                x1, y1 = antennas[freq][i]
                x2, y2 = antennas[freq][j]
                dx, dy = x2 - x1, y2 - y1

                x, y = x1, y1
                while 0 <= x < n and 0 <= y < m:
                    antinodes.add((x, y))
                    x += dx
                    y += dy

                x, y = x1 - dx, y1 - dy
                while 0 <= x < n and 0 <= y < m:
                    antinodes.add((x, y))
                    x -= dx
                    y -= dy

    return len(antinodes)


if __name__ == "__main__":
    print(main1())
    print(main2())
