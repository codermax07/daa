

def fractional_knapsack(n, W, weights, values):
    items = [(values[i], weights[i], values[i] / weights[i]) for i in range(n)]
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0
    for value, weight, ratio in items:
        if W == 0:
            break
        if weight <= W:
            total_value += value
            W -= weight
        else:
            total_value += value * (W / weight)
            W = 0
    return total_value

n = int(input("Enter number of items: "))
W = int(input("Enter knapsack capacity: "))
weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

print("Maximum value:", fractional_knapsack(n, W, weights, values))
