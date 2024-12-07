DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIR_ARROWS = {
    ">": 0,
    "v": 1,
    "<": 2,
    "^": 3,
}


def parse_input() -> tuple[set[tuple[int, int]], tuple[int, int], int, int, int]:
    walls = set()
    start_pos = (0, 0)
    start_direction = 0

    with open("input.txt", "r") as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                if char == "#":
                    walls.add((i, j))
                elif char != ".":
                    start_pos = (i, j)
                    start_direction = DIR_ARROWS[char]

    return walls, start_pos, start_direction, i + 1, j + 1


def traverse_grid(walls, start_pos, start_direction, n, m) -> set[tuple[int, int]]:
    pos = start_pos
    direction = start_direction
    visited = set()
    visited.add(pos)

    while True:
        npos = (pos[0] + DIRS[direction][0], pos[1] + DIRS[direction][1])
        if npos in walls:
            direction = (direction + 1) % 4
        elif not (0 <= npos[0] < n and 0 <= npos[1] < m):
            break
        else:
            pos = npos
            visited.add(pos)

    return visited


def calculate_obstructions(walls, start_pos, start_direction, visited, n, m) -> int:
    obstruction_count = 0

    for i, j in visited:
        if (i, j) == start_pos:
            continue

        nwalls = walls | {(i, j)}
        pos = start_pos
        direction = start_direction
        seen_states = set()
        seen_states.add((pos, direction))

        obstruction = False

        while True:
            npos = (pos[0] + DIRS[direction][0], pos[1] + DIRS[direction][1])
            if npos in nwalls:
                direction = (direction + 1) % 4
                seen_states.add((pos, direction))
            elif not (0 <= npos[0] < n and 0 <= npos[1] < m):
                break
            else:
                pos = npos
                if (pos, direction) in seen_states:
                    obstruction = True
                    break
                seen_states.add((pos, direction))

        obstruction_count += obstruction

    return obstruction_count


def main1() -> int:
    walls, start_pos, start_direction, n, m = parse_input()
    visited = traverse_grid(walls, start_pos, start_direction, n, m)
    return len(visited)


def main2() -> int:
    walls, start_pos, start_direction, n, m = parse_input()
    visited = traverse_grid(walls, start_pos, start_direction, n, m)
    return calculate_obstructions(walls, start_pos, start_direction, visited, n, m)


if __name__ == "__main__":
    print(main1())
    print(main2())
