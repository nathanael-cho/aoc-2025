import math


def num_digits(n: int) -> int:
    count = 0
    current = n
    while current > 0:
        current = current // 10
        count += 1
    return count


def day2_solution(ranges: list[tuple[int, int]], k: int) -> set[int]:
    all_invalid_ids = set()
    for low, high in ranges:
        if low < 10:
            low = 10

        low_digit_count = num_digits(low)
        high_digit_count = num_digits(high)

        # If the low has k * n digits, evaluate to n, and if k * n + l digits for 0 < l < k, evaluate to n + 1
        smallest_interval_to_repeat = (low_digit_count + 1) // k
        # Whether the low has k * n + l digits for 0 <= l < k, evaluate to n
        largest_interval_to_repeat = high_digit_count // k

        smallest_factor = 0
        for _ in range(k):
            smallest_factor = smallest_factor * (10 ** smallest_interval_to_repeat) + 1
        smallest_building_block = math.ceil(low / smallest_factor)
        # To account for no leading zeros
        if smallest_building_block < 10 ** (smallest_interval_to_repeat - 1):
            smallest_building_block = 10 ** (smallest_interval_to_repeat - 1)

        largest_factor = 0
        for _ in range(k):
            largest_factor = largest_factor * (10 ** largest_interval_to_repeat) + 1
        largest_building_block = math.floor(high / largest_factor)
        # To not exceed
        if largest_building_block >= 10 ** largest_interval_to_repeat:
            largest_building_block = 10 ** largest_interval_to_repeat - 1

        if smallest_building_block > largest_building_block:
            continue

        smallest_bb_num_digits = num_digits(smallest_building_block)
        largest_bb_num_digits = num_digits(largest_building_block)
        for i in range(smallest_bb_num_digits, largest_bb_num_digits + 1):
            current_ten = 10 ** i
            start = max(current_ten // 10, smallest_building_block)
            end = min(current_ten - 1, largest_building_block)
            multiplier = 0
            for _ in range(k):
                multiplier = multiplier * (10 ** i) + 1
            for j in range(start, end + 1):
                all_invalid_ids.add(j * multiplier)

    return all_invalid_ids


if __name__ == "__main__":
    with open("day2.txt", "r") as f:
        input = f.readline().strip()
        ranges = [(int(l[0]), int(l[1])) for l in (r.split("-") for r in input.split(","))]

    print("Day 2, Part 1:", sum(day2_solution(ranges, 2)))
    print("Day 2, Part 2:", sum(day2_solution(ranges, 2).union(*(day2_solution(ranges, i) for i in range(3, 10)))))
