def is_safe(report: list[int]) -> bool:
    n = len(report)
    sorted_report = sorted(report)
    if sorted_report == report:
        for i in range(n - 1):
            if not (1 <= report[i + 1] - report[i] <= 3):
                return False
        return True
    elif sorted_report == report[::-1]:
        for i in range(n - 1):
            if not (1 <= report[i] - report[i + 1] <= 3):
                return False
        return True
    return False


def main1() -> int:
    reports = []
    with open("input.txt", "r") as file:
        for line in file:
            reports.append(list(map(int, line.split())))

    total_safe_reports = 0
    for report in reports:
        if is_safe(report):
            total_safe_reports += 1

    return total_safe_reports


def main2() -> int:
    reports = []
    with open("input.txt", "r") as file:
        for line in file:
            reports.append(list(map(int, line.split())))

    total_safe_reports = 0
    for report in reports:
        if is_safe(report):
            total_safe_reports += 1
        else:
            n = len(report)
            for i in range(n):
                tweaked_report = report[:i] + report[i + 1 :]
                if is_safe(tweaked_report):
                    total_safe_reports += 1
                    break

    return total_safe_reports


if __name__ == "__main__":
    print(main1())
    print(main2())
