from collections import defaultdict


def paths_from_to(key1: str, key2: str, key_map: dict[str, list[str]]) -> int:
    paths = { key1: 1 }
    out_paths = 0
    while len(paths) > 0:
        next_paths = defaultdict(int)
        for main_key, path_count in paths.items():
            next_keys = key_map[main_key]
            for next_key in next_keys:
                if next_key == key2:
                    out_paths += path_count
                else:
                    next_paths[next_key] += path_count
        paths = next_paths
    return out_paths


def part1() -> int:
    with open("day11.txt") as f:
        lines = f.readlines()

    key_map = defaultdict(list)
    for line in lines:
        main_key, other_keys_str = line.strip().split(": ")
        other_keys = other_keys_str.split(" ")
        for other_key in other_keys:
            key_map[main_key].append(other_key)

    return paths_from_to("you", "out", key_map)


def part2() -> int:
    with open("day11.txt") as f:
        lines = f.readlines()

    key_map = defaultdict(list)
    for line in lines:
        main_key, other_keys_str = line.strip().split(": ")
        other_keys = other_keys_str.split(" ")
        for other_key in other_keys:
            key_map[main_key].append(other_key)

    return (
        (paths_from_to("svr", "dac", key_map) * paths_from_to("dac", "fft", key_map) * paths_from_to("fft", "out", key_map))
        + (paths_from_to("svr", "fft", key_map) * paths_from_to("fft", "dac", key_map) * paths_from_to("dac", "out", key_map))
    )


if __name__ == "__main__":
    print("Day 11, Part 1:", part1())
    print("Day 11, Part 2:", part2())
