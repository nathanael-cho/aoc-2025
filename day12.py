from dataclasses import dataclass


piece_sizes = [5, 7, 7, 6, 7, 7]


@dataclass
class Config:
    x_dim: int
    y_dim: int
    counts: list[int]


def part() -> int:
    with open("day12.txt", "r") as f:
        lines = f.readlines()

    configs: list[Config] = []
    for line in lines[30:]:
        dim_str, count_str = line.strip().split(": ")
        x_dim, y_dim = tuple(int(s) for s in dim_str.split("x"))
        counts = [int(s) for s in count_str.split(" ")]
        configs.append(Config(x_dim, y_dim, counts))

    feasible_configs = []
    for config in configs:
        hard_cap = config.x_dim * config.y_dim
        total_of_piece_sizes = sum(piece_sizes[i] * count for i, count in enumerate(config.counts))
        if hard_cap >= total_of_piece_sizes:
            feasible_configs.append(config)

    return len(feasible_configs)


if __name__ == "__main__":
    print("Day 12:", part())
