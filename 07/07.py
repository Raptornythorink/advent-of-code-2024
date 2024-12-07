def parse_input() -> list[tuple[int, list[int]]]:
    with open("input.txt", "r") as file:
        return [
            (int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split())))
            for line in file
        ]


def is_valid_equation1(result: int, operands: list[int]) -> bool:
    n = len(operands)

    def backtrack(index: int, current_value: int) -> bool:
        if index == n:
            return current_value == result
        if current_value > result:
            return False
        if backtrack(index + 1, current_value * operands[index]):
            return True
        if backtrack(index + 1, current_value + operands[index]):
            return True
        return False

    return backtrack(1, operands[0])


def is_valid_equation2(result: int, operands: list[int]) -> bool:
    n = len(operands)

    def backtrack(index: int, current_value: int) -> bool:
        if index == n:
            return current_value == result
        if current_value > result:
            return False
        if backtrack(index + 1, int(str(current_value) + str(operands[index]))):
            return True
        if backtrack(index + 1, current_value * operands[index]):
            return True
        if backtrack(index + 1, current_value + operands[index]):
            return True
        return False

    return backtrack(1, operands[0])


def main1() -> int:
    equations = parse_input()
    return sum(
        result for result, operands in equations if is_valid_equation1(result, operands)
    )


def main2() -> int:
    equations = parse_input()
    return sum(
        result for result, operands in equations if is_valid_equation2(result, operands)
    )


if __name__ == "__main__":
    print(main1())
    print(main2())
