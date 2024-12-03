import re


def main1() -> int:
    with open("input.txt", "r") as file:
        memory = "".join(file.readlines())

    mul_pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    mul_matches = mul_pattern.findall(memory)

    pairs = [match[4:-1].split(",") for match in mul_matches]
    result = sum([int(pair[0]) * int(pair[1]) for pair in pairs])

    return result


def main2() -> int:
    with open("input.txt", "r") as file:
        memory = "do()" + "".join(file.readlines())

    pattern = r"(do\(\)|don't\(\))|mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, memory)

    result = 0
    curr_do = True
    for match in matches:
        if match[0] == "do()":
            curr_do = True
        elif match[0] == "don't()":
            curr_do = False
        elif curr_do:
            result += int(match[1]) * int(match[2])

    return result


if __name__ == "__main__":
    print(main1())
    print(main2())
