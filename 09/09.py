import bisect


def main1() -> int:
    with open("input.txt", "r") as file:
        disk_map = file.readline().strip()

    layout: list[int] = []
    layout_size = 0
    id_num = 0
    for i, num in enumerate(disk_map):
        if i % 2:
            for _ in range(int(num)):
                layout.append(-1)
        else:
            for _ in range(int(num)):
                layout.append(id_num)
            id_num += 1
            layout_size += int(num)

    start_idx, end_idx = 0, len(layout) - 1
    while start_idx < end_idx - 1:
        if layout[end_idx] == -1:
            end_idx -= 1
        elif layout[start_idx] == -1:
            layout[start_idx] = layout[end_idx]
            end_idx -= 1
            start_idx += 1
        else:
            start_idx += 1

    checksum = sum(i * layout[i] for i in range(layout_size))

    return checksum


def main2() -> int:
    with open("input.txt", "r") as file:
        disk_map = file.readline().strip()

    layout: list[int] = []
    free_spaces: list[tuple[int, int]] = []
    files: list[tuple[int, int, int]] = []
    id_num = 0
    for i, num in enumerate(disk_map):
        if i % 2:
            if int(num) > 0:
                free_spaces.append((len(layout), int(num)))
            for _ in range(int(num)):
                layout.append(-1)
        else:
            if int(num) > 0:
                files.append((id_num, len(layout), int(num)))
            for _ in range(int(num)):
                layout.append(id_num)
            id_num += 1

    files.reverse()
    for file_id, file_idx, size in files:
        for free_idx, free_size in free_spaces:
            if free_idx > file_idx:
                break
            if free_size >= size:
                for i in range(size):
                    layout[free_idx + i] = file_id
                    layout[file_idx + i] = -1
                free_spaces.remove((free_idx, free_size))
                if free_size > size:
                    bisect.insort(free_spaces, (free_idx + size, free_size - size))
                break

    checksum = sum((layout[i] > -1) * i * layout[i] for i in range(len(layout)))

    return checksum


if __name__ == "__main__":
    print(main1())
    print(main2())
