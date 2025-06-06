def knapsack_01(n, W, weights, values):
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]

n = int(input("Enter number of items: "))
W = int(input("Enter capacity: "))
weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

print("Maximum value:", knapsack_01(n, W, weights, values))
