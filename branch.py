class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

class Node:
    def __init__(self, level, current_weight, current_value):
        self.level = level
        self.current_weight = current_weight
        self.current_value = current_value

def knapsack_branch_and_bound(items, capacity):
    items.sort(key=lambda item: item.ratio, reverse=True)

    def bound(node, current_weight, current_value, level):
        if current_weight >= capacity:
            return 0
        bound_value = current_value
        total_weight = current_weight
        i = level
        while i < len(items) and total_weight + items[i].weight <= capacity:
            total_weight += items[i].weight
            bound_value += items[i].value
            i += 1
        if i < len(items):
            bound_value += (capacity - total_weight) * items[i].ratio
        return bound_value

    def branch_and_bound_helper(node):
        nonlocal max_value
        level = node.level
        current_weight = node.current_weight
        current_value = node.current_value
        if current_weight > capacity:
            return
        if level == len(items):
            if current_value > max_value:
                max_value = current_value
            return
        if bound(node, current_weight, current_value, level) <= max_value:
            return

        # Exclude the item at the current level
        branch_and_bound_helper(Node(level + 1, current_weight, current_value))

        # Include the item at the current level
        current_weight += items[level].weight
        current_value += items[level].value
        branch_and_bound_helper(Node(level + 1, current_weight, current_value))

    max_value = 0
    branch_and_bound_helper(Node(level=0, current_weight=0, current_value=0))
    return max_value

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    items = []
    for i in range(n):
        weight, value = map(int, input(f"Enter weight and value for item {i + 1}: ").split())
        items.append(Item(weight, value))

    capacity = int(input("Enter the knapsack capacity: "))
    
    max_value = knapsack_branch_and_bound(items, capacity)
    print("Maximum value for the 0-1 Knapsack problem:", max_value)
