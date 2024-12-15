MOVES_DICT = {
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    "^": (-1, 0),
}


def parse_input1() -> tuple[
    set[tuple[int, int]],
    set[tuple[int, int]],
    tuple[int, int],
    list[tuple[int, int]],
]:
    walls = set()
    boxes = set()
    start_pos = (0, 0)
    moves = []
    i = 0

    with open("input.txt", "r") as file:
        line = file.readline().strip()
        while line:
            for j, c in enumerate(line):
                if c == "#":
                    walls.add((i, j))
                elif c == "O":
                    boxes.add((i, j))
                elif c == "@":
                    start_pos = (i, j)
            i += 1
            line = file.readline().strip()

        line = file.readline().strip()
        while line:
            for c in line:
                moves.append(MOVES_DICT[c])
            line = file.readline().strip()

    return walls, boxes, start_pos, moves


def parse_input2() -> tuple[
    set[tuple[int, int]],
    set[tuple[int, int]],
    tuple[int, int],
    list[tuple[int, int]],
]:
    walls = set()
    boxes_left = set()
    start_pos = (0, 0)
    moves = []
    i = 0

    with open("input.txt", "r") as file:
        line = file.readline().strip()
        while line:
            for j, c in enumerate(line):
                if c == "#":
                    walls.add((i, 2 * j))
                    walls.add((i, 2 * j + 1))
                elif c == "O":
                    boxes_left.add((i, 2 * j))
                elif c == "@":
                    start_pos = (i, 2 * j)
            i += 1
            line = file.readline().strip()

        line = file.readline().strip()
        while line:
            for c in line:
                moves.append(MOVES_DICT[c])
            line = file.readline().strip()

    return walls, boxes_left, start_pos, moves


def main1() -> int:
    walls, boxes, pos, moves = parse_input1()

    for dy, dx in moves:
        y, x = pos
        new_pos = (y + dy, x + dx)
        if new_pos in boxes:
            k = 1
            while (y + k * dy, x + k * dx) in boxes:
                k += 1
            final_pos = (y + k * dy, x + k * dx)
            if final_pos not in walls:
                boxes.remove(new_pos)
                boxes.add(final_pos)
                pos = new_pos
        elif new_pos not in walls:
            pos = new_pos

    return sum(100 * y + x for y, x in boxes)


def main2() -> int:
    walls, boxes_left, pos, moves = parse_input2()
    for dy, dx in moves:
        y, x = pos
        ny, nx = y + dy, x + dx

        if (ny, nx) in walls:
            continue

        if (ny, nx) not in boxes_left and (ny, nx - 1) not in boxes_left:
            pos = (ny, nx)
            continue

        if not dy:
            is_dir_left = dx == -1
            if (ny, nx - is_dir_left) in boxes_left:
                k = 1
                boxes_ahead = [(ny, nx - is_dir_left)]

                while (ny, nx + 2 * k * dx - is_dir_left) in boxes_left:
                    boxes_ahead.append((y, nx + 2 * k * dx - is_dir_left))
                    k += 1

                if (ny, nx + 2 * k * dx) not in walls:
                    for by, bx in boxes_ahead:
                        boxes_left.remove((by, bx))
                        boxes_left.add((by, bx + dx))
                    pos = (ny, nx)

        else:
            boxes_ahead = []

            if (ny, nx) in boxes_left:
                boxes_ahead.append({(ny, nx)})
            elif (ny, nx - 1) in boxes_left:
                boxes_ahead.append({(ny, nx - 1)})

            possible = True

            while possible and boxes_ahead[-1]:
                next_boxes_ahead = set()

                for by, bx in boxes_ahead[-1]:
                    if (by + dy, bx) in walls or (by + dy, bx + 1) in walls:
                        possible = False
                        break

                    if (by + dy, bx - 1) in boxes_left:
                        next_boxes_ahead.add((by + dy, bx - 1))
                    if (by + dy, bx) in boxes_left:
                        next_boxes_ahead.add((by + dy, bx))
                    if (by + dy, bx + 1) in boxes_left:
                        next_boxes_ahead.add((by + dy, bx + 1))

                boxes_ahead.append(next_boxes_ahead)

            if possible:
                boxes_ahead.reverse()
                for boxes in boxes_ahead:
                    for by, bx in boxes:
                        boxes_left.remove((by, bx))
                        boxes_left.add((by + dy, bx))
                pos = (ny, nx)

    return sum(100 * y + x for y, x in boxes_left)


if __name__ == "__main__":
    print(main1())
    print(main2())
