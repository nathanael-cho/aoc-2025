from collections import defaultdict
from dataclasses import dataclass

import pulp


@dataclass
class Diagram:
    target: int
    switches: list[int] | list[list[int]]
    joltages: list[int]


def process_line_into_diagram(line: str, part_two_flag: bool = False) -> Diagram:
    split = line.strip().split(" ")

    target = 0
    for i, c in enumerate(split[0][1:-1]):  # Remove the start and end brackets
        if c == "#":
            target += 2 ** i

    if part_two_flag:
        switches = [
            [int(cs) for cs in section[1:-1].split(",")]
            for section in split[1:-1]
        ]
    else:
        switches = [
            sum([2 ** int(cs) for cs in s[1:-1].split(",") ])
            for s in split[1:-1]
        ]

    joltages = [ int(s) for s in split[-1][1:-1].split(",") ]

    return Diagram(target=target, switches=switches, joltages=joltages)


def part1() -> int:
    with open("day10.txt", "r") as f:
        lines = f.readlines()

    diagrams = [process_line_into_diagram(line) for line in lines]

    total = 0
    for diagram in diagrams:
        target = diagram.target
        switches = diagram.switches

        cur_len = 0
        cur_set = { 0 }
        while target not in cur_set:
            new_set = set()
            for c in cur_set:
                for s in switches:
                    new_set.add(c ^ s)
            cur_set = new_set
            cur_len += 1

        total += cur_len

    return total


def part2() -> int:
    with open("day10.txt", "r") as f:
        lines = f.readlines()

    diagrams = [process_line_into_diagram(line, part_two_flag=True) for line in lines]

    total = 0
    for diagram in diagrams:
        num_switches = len(diagram.switches)

        problem = pulp.LpProblem("Joltages", pulp.LpMinimize)
        x_vars = [pulp.LpVariable(f"x_{i}", cat="Integer", lowBound=0) for i in range(num_switches)]

        for i, joltage in enumerate(diagram.joltages):
            problem += pulp.lpSum(int(i in switch) * x_vars[j] for j, switch in enumerate(diagram.switches)) == joltage

        problem += pulp.lpSum(x_vars)

        problem.solve()

        final_solution = [int(pulp.value(v)) for v in x_vars]

        total += sum(final_solution)

    return total


if __name__ == "__main__":
    print("Day 10, Part 1:", part1())
    print("Day 10, Part 2:", part2())
