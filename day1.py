def day1_solution(dials: list[tuple[str, int]], part_two_flag: bool = False):
    total_zeros = 0
    previous_state = None  # Gets overwritten immediately
    current_state = 50
    for direction, magnitude in dials:
        previous_state = current_state
        if direction == "L":
            current_state = (current_state - magnitude) % 100
        else:
            current_state = (current_state + magnitude) % 100

        if part_two_flag:
            total_rotation_zeros = abs(magnitude) // 100  # Each 100 guarantees hitting zero
            total_zeros += total_rotation_zeros

            # Now, we figure out if the remainder hits 0
            remaining_magnitude = magnitude - 100 * total_rotation_zeros
            if direction == "L":
                abs_current_state = previous_state - remaining_magnitude
            else:
                abs_current_state = previous_state + remaining_magnitude
            if (previous_state != 0) and (abs_current_state <= 0 or abs_current_state >= 100):
                total_zeros += 1
        else:
            if current_state == 0:
                total_zeros += 1

    return total_zeros


if __name__ == "__main__":
    with open("day1.txt", "r") as f:
        dials = [(line[0], int(line[1:])) for line in f.readlines()]

    print("Day 1, Part 1:", day1_solution(dials, part_two_flag=False))
    print("Day 1, Part 2:", day1_solution(dials, part_two_flag=True))
