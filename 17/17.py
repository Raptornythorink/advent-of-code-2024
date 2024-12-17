def parse_input() -> tuple[int, int, int, list[int]]:
    with open("input.txt") as file:
        reg_a = int(file.readline().strip()[12:])
        reg_b = int(file.readline().strip()[12:])
        reg_c = int(file.readline().strip()[12:])

        file.readline()

        program = [int(x) for x in file.readline().strip()[9:].split(",")]

    return reg_a, reg_b, reg_c, program


def get_combo_operand(literal_operand: int, reg_a: int, reg_b: int, reg_c: int) -> int:
    match literal_operand:
        case 4:
            return reg_a
        case 5:
            return reg_b
        case 6:
            return reg_c
        case 7:
            raise ValueError("Invalid operand")
        case _:
            return literal_operand


def exec_instr(
    opcode: int, literal_operand: int, ip: int, reg_a: int, reg_b: int, reg_c: int
) -> tuple[int, int, int, int, str | None]:
    output = None
    match opcode:
        case 0:
            reg_a //= 2 ** get_combo_operand(literal_operand, reg_a, reg_b, reg_c)
            ip += 2
        case 1:
            reg_b ^= literal_operand
            ip += 2
        case 2:
            reg_b = get_combo_operand(literal_operand, reg_a, reg_b, reg_c) % 8
            ip += 2
        case 3:
            ip = literal_operand if reg_a else ip + 2
        case 4:
            reg_b ^= reg_c
            ip += 2
        case 5:
            output = str(get_combo_operand(literal_operand, reg_a, reg_b, reg_c) % 8)
            ip += 2
        case 6:
            reg_b = reg_a // (
                2 ** get_combo_operand(literal_operand, reg_a, reg_b, reg_c)
            )
            ip += 2
        case 7:
            reg_c = reg_a // (
                2 ** get_combo_operand(literal_operand, reg_a, reg_b, reg_c)
            )
            ip += 2
        case _:
            raise ValueError("Invalid opcode")

    return ip, reg_a, reg_b, reg_c, output


def generate_reg_a(octits: list[int]) -> int:
    return sum(octit * 8 ** (15 - i) for i, octit in enumerate(octits))


def validate_partial_reg_a(
    reg_a: int, k: int, program: list[int], reg_b: int, reg_c: int
) -> bool:
    n = len(program)
    ip = 0
    outputs = []

    while ip < n:
        ip, reg_a, reg_b, reg_c, output = exec_instr(
            program[ip], program[ip + 1], ip, reg_a, reg_b, reg_c
        )
        if output is not None:
            outputs.append(int(output))

    return outputs[-k:] == program[-k:]


def backtrack(
    octits: list[int], depth: int, program: list[int], reg_b: int, reg_c: int
) -> None | list[int]:
    if depth == len(octits):
        return octits

    for candidate in range(8):
        octits[depth] = candidate
        reg_a = generate_reg_a(octits[: depth + 1])

        if validate_partial_reg_a(reg_a, depth + 1, program, reg_b, reg_c):
            result = backtrack(octits, depth + 1, program, reg_b, reg_c)
            if result:
                return result

        octits[depth] = -1

    return None


def main1() -> str:
    reg_a, reg_b, reg_c, program = parse_input()
    n = len(program)

    ip = 0
    outputs = []

    while ip < n:
        ip, reg_a, reg_b, reg_c, output = exec_instr(
            program[ip], program[ip + 1], ip, reg_a, reg_b, reg_c
        )
        if output is not None:
            outputs.append(output)

    return ",".join(outputs)


def main2() -> int:
    _, init_reg_b, init_reg_c, program = parse_input()

    octits = backtrack([-1] * len(program), 0, program, init_reg_b, init_reg_c)

    return generate_reg_a(octits)


if __name__ == "__main__":
    print(main1())
    print(main2())
