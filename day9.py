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
    # Make it a full loop
    coordinates.append(coordinates[0])

    # Uncomment to show the plot
    # import matplotlib.pyplot as plt
    # x = [c[0] for c in coordinates]
    # x.append(coordinates[0][0])
    # y = [c[1] for c in coordinates]
    # y.append(coordinates[0][1])
    # plt.scatter(x, y, s=1.5)
    # plt.plot(x, y, linewidth=1)
    # plt.savefig("day9.png", dpi=600)

    # We plotted the points
    possible_inside_corners = []
    for i in range(0, len(coordinates) - 1):
        first = coordinates[i]
        second = coordinates[i + 1]
        distance = abs((second[1] - first[1]) + (second[0] - first[0]))
        if distance > 50_000:
            if first[0] > 50_000:
                possible_inside_corners.append(first)
            else:
                possible_inside_corners.append(second)

    def inside_box(c1, c2, c3) -> bool:
        x_min, x_max = min(c1[0], c2[0]), max(c1[0], c2[0])
        y_min, y_max = min(c1[1], c2[1]), max(c1[1], c2[1])
        return (x_min < c3[0] < x_max) and (y_min < c3[1] < y_max)

    max_area = 0
    for inside_corner in possible_inside_corners:
        print("Inside corner:", inside_corner)
        for potential_outside_corner in coordinates[:-1]:
            if (
                (inside_corner[1] > 50_000 and potential_outside_corner[1] <= inside_corner[1])
                or (inside_corner[1] < 50_000 and potential_outside_corner[1] >= inside_corner[1])
            ):
                continue

            if potential_outside_corner[0] >= inside_corner[0]:
                continue

            potential_max_area = (abs(potential_outside_corner[1] - inside_corner[1]) + 1) * (abs(potential_outside_corner[0] - inside_corner[0]) + 1)
            disqualified = False

            for other_coordinate in coordinates[:-1]:
                if inside_box(inside_corner, potential_outside_corner, other_coordinate):
                    disqualified = True
                    break

            if not disqualified:
                max_area = max(max_area, potential_max_area)

    return max_area


if __name__ == "__main__":
    print("Day 9, Part 1:", part1())
    print("Day 9, Part 2:", part2())
