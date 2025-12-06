def part1() -> int:
    with open("day5.txt", "r") as f:
        lines = f.readlines()

    intervals = []
    for line in lines:
        if line.strip() == "":
            break

        interval = [int(x) for x in line.strip().split("-")]
        intervals.append(interval)

    idx_to_start_numbers = len(intervals) + 1
    numbers = []
    for line in lines[idx_to_start_numbers:]:
        numbers.append(int(line))

    # Naive solution
    fresh_id_count = 0
    for n in numbers:
        is_fresh = False
        for low, high in intervals:
            if low <= n <= high:
                is_fresh = True
                break
        if is_fresh:
            fresh_id_count += 1

    return fresh_id_count


def part2() -> int:
    with open("day5.txt", "r") as f:
        lines = f.readlines()

    intervals = []
    for line in lines:
        if line.strip() == "":
            break

        interval = [int(x) for x in line.strip().split("-")]
        intervals.append(interval)

    sorted_intervals = sorted(intervals)

    merged_intervals = []
    seen_interval = sorted_intervals[0]
    for i in range(1, len(sorted_intervals)):
        new_interval = sorted_intervals[i]
        if seen_interval[-1] >= new_interval[0]:
            seen_interval[-1] = max(seen_interval[-1], new_interval[-1])
        else:
            merged_intervals.append(seen_interval)
            seen_interval = new_interval
    merged_intervals.append(seen_interval)

    total_fresh = 0
    for low, high in merged_intervals:
        total_fresh += high - low + 1

    return total_fresh


if __name__ == "__main__":
    print("Day 5, Part 1:", part1())
    print("Day 5, Part 2:", part2())
