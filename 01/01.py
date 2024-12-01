def main1() -> int:
    left_list = []
    right_list = []

    with open("input.txt", "r") as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    left_list.sort()
    right_list.sort()

    distance = sum(abs(left - right) for left, right in zip(left_list, right_list))

    return distance


def main2() -> int:
    left_list = []
    right_list = []

    with open("input.txt", "r") as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    occurences = {left: right_list.count(left) for left in left_list}
    similarity = sum(left * occurences[left] for left in left_list)

    return similarity


if __name__ == "__main__":
    print(main1())
    print(main2())
