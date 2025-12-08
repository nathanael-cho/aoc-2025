def calc_distance(first: tuple[int, int, int], second: tuple[int, int, int]) -> int:
    # No need to square root
    return sum((first[i] - second[i]) ** 2 for i in range(3))


class GraphNode:
    def __init__(self, id: int, coordinate: tuple[int, int, int]):
        self.id = id
        self.coordinate = coordinate
        self.distances: dict[int, int] = {}
        self.min_distance: int | None = None
        self.closest_node: GraphNode | None = None


class Graph:
    def __init__(self):
        self.nodes: dict[int, GraphNode] = {}
        self.node_id_to_set_id = {}
        self.set_id_to_node_ids = {}
        self.next_set_id = 0
        self.num_sets = 0
        self.last_xs = None

    def add_coordinate(self, new_coordinate: tuple[int, int, int]):
        new_idx = max(self.nodes.keys()) + 1 if len(self.nodes) else 0

        new_node = GraphNode(new_idx, new_coordinate)

        new_min_distance = None
        new_closest_node = None
        for other_idx in self.nodes.keys():
            other_node = self.nodes[other_idx]
            other_coordinate = other_node.coordinate

            distance = calc_distance(new_coordinate, other_coordinate)

            new_node.distances[other_idx] = distance
            other_node.distances[new_idx] = distance

            if new_min_distance is None or distance <= new_min_distance:
                new_min_distance = distance
                new_closest_node = other_node

            if other_node.min_distance is None or distance <= other_node.min_distance:
                other_node.min_distance = distance
                other_node.closest_node = new_node

        new_node.min_distance = new_min_distance
        new_node.closest_node = new_closest_node

        self.nodes[new_idx] = new_node

        self.num_sets += 1


    def merge_closest(self):
        cur_keys = list(self.nodes.keys())

        # Find the overall minimum distance in the graph in O(n) time
        ovr_min_distance = None
        ovr_min_node = None
        for i in cur_keys:
            cur_node = self.nodes[i]
            if ovr_min_distance is None or cur_node.min_distance < ovr_min_distance:
                ovr_min_distance = cur_node.min_distance
                ovr_min_node = cur_node

        # Get the two nodes that make up that distance
        min_node_one = ovr_min_node
        min_node_two = ovr_min_node.closest_node

        self.last_xs = (min_node_one.coordinate[0], min_node_two.coordinate[0])

        # Delete edge between these two nodes
        del min_node_one.distances[min_node_two.id]
        del min_node_two.distances[min_node_one.id]

        # Re-calculate minimum edges for these two nodes
        for node in [min_node_one, min_node_two]:
            new_min_distance = None
            new_closest_node = None
            for neighbor_id in node.distances.keys():
                if new_min_distance is None or  node.distances[neighbor_id] <= new_min_distance:
                    new_min_distance = node.distances[neighbor_id]
                    new_closest_node = self.nodes[neighbor_id]
            node.min_distance = new_min_distance
            node.closest_node = new_closest_node

        # Add these two nodes to a set
        if min_node_one.id in self.node_id_to_set_id and min_node_two.id in self.node_id_to_set_id:
            set_id_one = self.node_id_to_set_id[min_node_one.id]
            set_id_two = self.node_id_to_set_id[min_node_two.id]
            if set_id_one == set_id_two:
                pass
            else:  # Move everything from set two to set one
                second_set = self.set_id_to_node_ids[set_id_two]
                for node_id in second_set:
                    self.node_id_to_set_id[node_id] = set_id_one
                    self.set_id_to_node_ids[set_id_one].update(self.set_id_to_node_ids[set_id_two])
                del self.set_id_to_node_ids[set_id_two]
                self.num_sets -= 1
        elif min_node_one.id in self.node_id_to_set_id:
            set_id = self.node_id_to_set_id[min_node_one.id]
            self.node_id_to_set_id[min_node_two.id] = set_id
            self.set_id_to_node_ids[set_id].add(min_node_two.id)
            self.num_sets -= 1
        elif min_node_two.id in self.node_id_to_set_id:
            set_id = self.node_id_to_set_id[min_node_two.id]
            self.node_id_to_set_id[min_node_one.id] = set_id
            self.set_id_to_node_ids[set_id].add(min_node_one.id)
            self.num_sets -= 1
        else:
            set_id = self.next_set_id
            self.next_set_id += 1
            self.node_id_to_set_id[min_node_one.id] = set_id
            self.node_id_to_set_id[min_node_two.id] = set_id
            self.set_id_to_node_ids[set_id] = {min_node_one.id, min_node_two.id}
            self.num_sets -= 1

    def get_cluster_sizes(self) -> list[int]:
        self.set_id_to_node_ids
        return [len(self.set_id_to_node_ids[i]) for i in self.set_id_to_node_ids]


def part1() -> int:
    with open("day8.txt", "r") as f:
        lines = f.readlines()

    graph = Graph()

    coordinates = [tuple(int(x) for x in line.strip().split(",")) for line in lines]

    for coordinate in coordinates:
        graph.add_coordinate(coordinate)

    for _ in range(1000):
        graph.merge_closest()

    sorted_cluster_sizes = sorted(graph.get_cluster_sizes(), reverse=True)

    to_return = 1
    for size in sorted_cluster_sizes[:3]:
        to_return *= size

    return to_return


def part2() -> int:
    with open("day8.txt", "r") as f:
        lines = f.readlines()

    graph = Graph()

    coordinates = [tuple(int(x) for x in line.strip().split(",")) for line in lines]

    for coordinate in coordinates:
        graph.add_coordinate(coordinate)

    while graph.num_sets > 1:
        graph.merge_closest()

    return graph.last_xs[0] * graph.last_xs[1]


if __name__ == "__main__":
    print("Day 8, Part 1:", part1())
    print("Day 8, Part 2:", part2())
