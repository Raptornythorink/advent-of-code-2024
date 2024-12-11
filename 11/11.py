from collections import defaultdict
from functools import cache


def parse_input() -> defaultdict[int, int]:
    with open("input.txt", "r") as file:
        stones = [int(num) for num in file.read().strip().split()]
    stones_dict = defaultdict(int)
    for stone in stones:
        stones_dict[stone] += 1
    return stones_dict


@cache
def get_next_stones(stone) -> list[int]:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        half = len(str(stone)) // 2
        return [int(str(stone)[:half]), int(str(stone)[half:])]
    return [2024 * stone]


def count_stones(blinks) -> int:
    stones_dict = parse_input()

    for _ in range(blinks):
        new_stones_dict = defaultdict(int)

        for stone, count in stones_dict.items():
            next_stones = get_next_stones(stone)
            for next_stone in next_stones:
                new_stones_dict[next_stone] += count

        stones_dict = new_stones_dict

    return sum(stones_dict.values())


def main1() -> int:
    return count_stones(25)


def main2() -> int:
    return count_stones(75)


if __name__ == "__main__":
    print(main1())
    print(main2())
