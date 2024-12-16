def parse_input() -> list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]:
    machine_configs = []

    with open("input.txt", "r") as file:
        line = file.readline()
        while line:
            A_X = int(line.split("+")[1].split(",")[0])
            A_Y = int(line.split("+")[2])

            line = file.readline()

            B_X = int(line.split("+")[1].split(",")[0])
            B_Y = int(line.split("+")[2])

            line = file.readline()

            P_X = int(line.split("=")[1].split(",")[0])
            P_Y = int(line.split("=")[2])

            machine_configs.append(((A_X, A_Y), (B_X, B_Y), (P_X, P_Y)))

            line = file.readline()
            if not line:
                break
            line = file.readline()

    return machine_configs


def count_tokens(offset: int) -> int:
    machine_configs = parse_input()
    tokens = 0

    for machine_config in machine_configs:
        (A_X, A_Y), (B_X, B_Y), (P_X, P_Y) = machine_config
        matrix = [[A_X, B_X], [A_Y, B_Y]]
        target = [P_X + offset, P_Y + offset]

        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        if det == 0:
            continue

        a = (matrix[1][1] * target[0] - matrix[0][1] * target[1]) / det
        b = (-matrix[1][0] * target[0] + matrix[0][0] * target[1]) / det

        if a < 0 or b < 0:
            continue
        if a.is_integer() and b.is_integer():
            tokens += 3 * int(a) + int(b)

    return tokens


def main1() -> int:
    return count_tokens(0)


def main2() -> int:
    return count_tokens(10000000000000)


if __name__ == "__main__":
    print(main1())
    print(main2())
