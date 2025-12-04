from __future__ import annotations


class DLLNode:
    def __init__(self, value: int, previous: DLLNode | None, next: DLLNode | None):
        self.value = value
        self.previous = previous
        self.next = next


class Stack:
    def __init__(self):
        self.values: list[DLLNode] = []

    def append(self, node: DLLNode):
        # This is O(1) in Python
        self.values.append(node)

    def pop(self) -> DLLNode | None:
        if not len(self.values):
            return None
        return self.values.pop()
    
    def size(self) -> int:
        return len(self.values)


def day3_solution(packs: list[list[int]], k: int):
    running_sum = 0
    for pack in battery_packs:
        stack = Stack()

        head: DLLNode | None = None
        end: DLLNode | None = None
        for i in range(len(pack) - 1, len(pack) - k - 1, -1):
            value = pack[i]
            new_node = DLLNode(value, None, head)
            if head is not None:
                head.previous = new_node

            head = new_node
            if i == len(pack) - 1:
                end = head
            elif i == len(pack) - 2:
                end.previous = head
            
            if (head.next is not None) and head.value < head.next.value:
                stack.append(head)

        for i in range(len(pack) - k - 1, -1, -1):
            value = pack[i]
            if value < head.value:
                continue

            new_head = DLLNode(value, None, head)
            head.previous = new_head
            head = new_head

            if not stack.size():
                end = end.previous
                end.next = None
            else:
                node_to_remove = stack.pop()
                prev_of_node = node_to_remove.previous
                next_of_node = node_to_remove.next
                if prev_of_node is not None:
                    prev_of_node.next = next_of_node
                    if prev_of_node.value < next_of_node.value:
                        stack.append(prev_of_node)
                next_of_node.previous = prev_of_node

        current_sum = 0
        current_node = head
        while current_node is not None:
            current_sum = current_sum * 10 + current_node.value
            current_node = current_node.next

        running_sum += current_sum

    return running_sum


if __name__ == "__main__":
    with open("day3.txt", "r") as f:
        battery_packs = [[int(x) for x in line.strip()] for line in f.readlines()]

    print("Day 3, Part 1:", day3_solution(battery_packs, 2))
    print("Day 3, Part 2:", day3_solution(battery_packs, 12))
