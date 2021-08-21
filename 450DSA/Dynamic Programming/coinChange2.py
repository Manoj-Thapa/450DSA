def solve(coins, amount):
    n = len(coins)
    dp = [[0] * (amount + 1) for i in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]


    return dp[n][amount]


coins = [1,2,3]
print(solve(coins, 4))
