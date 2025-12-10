def part1() -> int:
    with open("day9.txt") as f:
        lines = f.readlines()

    coordinates = [tuple(int(n) for n in line.strip().split(",")) for line in lines]

    max_area = 0
    for i in range(len(coordinates)):
        x_i = coordinates[i][0]
        y_i = coordinates[i][1]
        for j in range(i + 1, len(coordinates)):
            x_j = coordinates[j][0]
            y_j = coordinates[j][1]
            max_area = max(max_area, (abs(y_j - y_i) + 1) * (abs(x_j - x_i) + 1))

    return max_area


def part2() -> int:
    with open("day9.txt") as f:
        lines = f.readlines()

    coordinates = [tuple(int(n) for n in line.strip().split(",")) for line in lines]

    max_area = 0
    for i in range(len(coordinates)):
        x_i = coordinates[i][0]
        y_i = coordinates[i][1]
        for j in range(i + 1, len(coordinates)):
            x_j = coordinates[j][0]
            y_j = coordinates[j][1]

            potential_max_area = (abs(y_j - y_i) + 1) * (abs(x_j - x_i) + 1)

            max_area = max(max_area, potential_max_area)


    for i in range(2, len(coordinates)):
        if (coordinates[i][0] == coordinates[i - 1][0] == coordinates[i - 2][0]):
            print(coordinates[i], coordinates[i - 1], coordinates[i - 2])
        if (coordinates[i][1] == coordinates[i - 1][1] == coordinates[i - 2][1]):
            print(coordinates[i], coordinates[i - 1], coordinates[i - 2])

    coordinate_to_idx = {coordinate: i for i, coordinate in enumerate(coordinates)}

    print(len(coordinates))
    print(max(c[0] for c in coordinates) - min(c[0] for c in coordinates))
    # print(max(c[0] for c in coordinates))
    print(max(c[1] for c in coordinates) - min(c[1] for c in coordinates))
    # print(max(c[1] for c in coordinates))

    return 0


if __name__ == "__main__":
    print("Day 9, Part 1:", part1())
    print("Day 9, Part 2:", part2())
