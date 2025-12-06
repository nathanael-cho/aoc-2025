def part1() -> int:
    with open("day6.txt", "r") as f:
        lines = f.readlines()

    operations = []
    for c in lines[-1]:
        if c not in [" ", "\n"]:
            operations.append(c)

    num_problems = len(operations)

    all_numbers = [[] for _ in range(num_problems)]

    for line in lines[:-1]:
        current_idx = 0
        current_number = None
        for c in line:
            if c in [" ", "\n"]:
                if current_number is not None:
                    all_numbers[current_idx].append(current_number)
                    current_idx += 1
                    current_number = None
                continue
            else:
                if current_number is None:
                    current_number = int(c)
                else:
                    current_number = current_number * 10 + int(c)

    final_sum = 0
    for i, op in enumerate(operations):
        match op:
            case "+":
                final_sum += sum(all_numbers[i])
            case "*":
                to_add = 1
                for x in all_numbers[i]:
                    to_add *= x
                final_sum += to_add

    return final_sum


def part2() -> int:
    with open("day6.txt") as f:
        lines = f.readlines()

    num_chars_per_line = len(lines[-1])
    num_lines = len(lines)

    total_sum = 0
    operator = None
    current_answer = None
    for col_idx in range(num_chars_per_line):
        seen_char = False
        current_number = None
        for row_idx in range(num_lines):
            c = lines[row_idx][col_idx]
            if c in [" ", "\n"]:
                continue

            seen_char = True
            if c in ["*", "+"]:
                operator = c
            else:
                if current_number is None:
                    current_number = int(c)
                else:
                    current_number = 10 * current_number + int(c)

        # A full column of spaces means, add current_answer if it exists and clear variables
        if not seen_char:
            if current_answer is not None:  # The edge case would be multiple or leading columns of all spaces
                total_sum += current_answer
            current_answer = None
            operator = None
        else:
            if current_answer is None:
                current_answer = current_number
            else:
                match operator:
                    case "+":
                        current_answer += current_number
                    case "*":
                        current_answer *= current_number

    return total_sum


if __name__ == "__main__":
    print("Day 6, Part 1:", part1())
    print("Day 6, Part 2:", part2())