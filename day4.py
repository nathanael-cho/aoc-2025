def part1() -> int:
    with open("day4.txt") as f:
        lines = f.readlines()
        tp_flags = [[(1 if x == "@" else 0) for x in line[:-1]] for line in lines]  # Exclude the new line char

    dim = len(tp_flags)

    total_sum = 0
    for row in range(dim):
        for col in range(dim):
            if not tp_flags[row][col]:
                continue

            current_sum = 0
            for row_delta in [-1, 0, 1]:
                for col_delta in [-1, 0, 1]:
                    if row_delta == 0 and col_delta == 0:
                        continue
                    adj_row = row + row_delta
                    adj_col = col + col_delta
                    if adj_row < 0 or adj_row >= dim or adj_col < 0 or adj_col >= dim:
                        continue
                    current_sum += tp_flags[adj_row][adj_col]

            if current_sum < 4:
                total_sum += 1

    return total_sum


def part2() -> int:
    with open("day4.txt") as f:
        lines = f.readlines()
        tp_flags = [[(1 if x == "@" else 0) for x in line[:-1]] for line in lines]  # Exclude the new line char

    dim = len(tp_flags)

    prev_total_sum = -1
    total_sum = 0
    while prev_total_sum != total_sum:
        prev_total_sum = total_sum

        for row in range(dim):
            for col in range(dim):
                if not tp_flags[row][col]:
                    continue

                current_sum = 0
                for row_delta in [-1, 0, 1]:
                    for col_delta in [-1, 0, 1]:
                        if row_delta == 0 and col_delta == 0:
                            continue
                        adj_row = row + row_delta
                        adj_col = col + col_delta
                        if adj_row < 0 or adj_row >= dim or adj_col < 0 or adj_col >= dim:
                            continue
                        current_sum += tp_flags[adj_row][adj_col]

                if current_sum < 4:
                    total_sum += 1
                    # Remove the toilet paper
                    tp_flags[row][col] = 0

    return total_sum


if __name__ == "__main__":
    print("Day 4, Part 1:", part1())
    print("Day 4, Part 2:", part2())
