from collections import defaultdict


def parse_input() -> tuple[dict[int, set[int]], list[list[int]]]:
    preds = defaultdict(set)
    updates = []

    with open("input.txt", "r") as file:
        line = file.readline().strip()
        while line:
            page1, page2 = map(int, line.split("|"))
            preds[page2].add(page1)
            line = file.readline().strip()

        line = file.readline().strip()
        while line:
            updates.append(list(map(int, line.split(","))))
            line = file.readline().strip()

    return preds, updates


def main1() -> int:
    preds, updates = parse_input()

    middle_page_sum = 0

    for pages in updates:
        pages_set = set(pages)
        update_preds = defaultdict(set)

        for page in pages:
            for pred in preds[page]:
                if pred in pages_set:
                    update_preds[page].add(pred)

        n = len(pages)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if pages[j] in update_preds[pages[i]]:
                    break
            else:
                continue
            break
        else:
            middle_page_sum += pages[n // 2]

    return middle_page_sum


def main2() -> int:
    preds, updates = parse_input()

    middle_page_sum = 0

    for pages in updates:
        pages_set = set(pages)
        update_preds = defaultdict(set)

        for page in pages:
            for pred in preds[page]:
                if pred in pages_set:
                    update_preds[page].add(pred)

        n = len(pages)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if pages[j] in update_preds[pages[i]]:
                    break
            else:
                continue
            break
        else:
            continue
        for page in pages:
            if len(update_preds[page]) == n // 2:
                middle_page_sum += page
                break

    return middle_page_sum


if __name__ == "__main__":
    print(main1())
    print(main2())
