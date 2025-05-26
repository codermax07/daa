def lcs(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]

X = input("Enter first string: ")
Y = input("Enter second string: ")

print("Length of LCS:", lcs(X, Y))
