def part1() -> int:
    with open("day7.txt") as f:
        lines = f.readlines()

    s_idx = lines[0].find("S")
    assert s_idx >= 0

    num_rows = len(lines)
    num_cols = len(lines[0])

    col_idx_flags = [0] * num_cols
    col_idx_flags[s_idx] = 1

    num_splits = 0
    for i in range(1, num_rows):  # The first row is just the starter
        line = lines[i]
        for j in range(num_cols):
            if col_idx_flags[j] and line[j] == "^":
                col_idx_flags[j] = 0
                if j > 0:
                    col_idx_flags[j - 1] = 1
                if j < num_cols - 1:
                    col_idx_flags[j + 1] = 1
                num_splits += 1
            # Else, keep col_idx_flag[j] as-is, whether 1 or 0

    return num_splits


def part2() -> int:
    with open("day7.txt") as f:
        lines = f.readlines()

    s_idx = lines[0].find("S")
    assert s_idx >= 0

    num_rows = len(lines)
    num_cols = len(lines[0])

    path_counts = [0] * num_cols
    path_counts[s_idx] = 1

    for i in range(1, num_rows):  # The first row is just the starter
        line = lines[i]
        for j in range(num_cols):
            if path_counts[j] > 0 and line[j] == "^":
                if j > 0:
                    path_counts[j - 1] += path_counts[j]
                if j < num_cols - 1:
                    path_counts[j + 1] += path_counts[j]
                path_counts[j] = 0
            # Else, keep col_idx_flag[j] as-is

    return sum(path_counts)


if __name__ == "__main__":
    print("Day 7, Part 1:", part1())
    print("Day 7, Part 2:", part2())
