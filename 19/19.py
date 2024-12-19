from functools import cache


def parse_input() -> tuple[list[str], list[str]]:
    with open("input.txt", "r") as file:
        patterns = file.readline().strip().split(", ")
        file.readline()
        line = file.readline().strip()
        designs = []
        while line:
            designs.append(line)
            line = file.readline().strip()
    return patterns, designs


def main1() -> int:
    patterns, designs = parse_input()

    @cache
    def is_design_possible(design: str) -> bool:
        if not design:
            return True
        for pattern in patterns:
            if design.startswith(pattern) and is_design_possible(
                design[len(pattern) :]
            ):
                return True
        return False

    return sum(is_design_possible(design) for design in designs)


def main2() -> int:
    patterns, designs = parse_input()

    @cache
    def count_arrangements(design: str) -> bool:
        if not design:
            return 1
        count = 0
        for pattern in patterns:
            if design.startswith(pattern):
                count += count_arrangements(design[len(pattern) :])
        return count

    return sum(count_arrangements(design) for design in designs)


if __name__ == "__main__":
    print(main1())
    print(main2())
