def knapsack_greedy(weights, values, capacity):
    n = len(weights)
    ratios = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    ratios.sort(reverse=True)
    total_value = 0
    total_weight = 0
    selected_items = []
    for ratio, weight, value in ratios:
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value
            selected_items.append((weight, value))
    return total_value, selected_items
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
total_value, selected_items = knapsack_greedy(weights, values, capacity)
print("Total value in knapsack:", total_value)
print("Selected items (weight, value):", selected_items)
