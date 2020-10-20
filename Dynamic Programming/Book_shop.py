def helper(n,x,prices,pages):
    dp = [[0 for i in range(x+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(x+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif prices[i-1] <= j:
                dp[i][j] = max(pages[i-1] + dp[i-1][j-prices[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][x]

n,x = map(int,raw_input().split())
prices = list(map(int,raw_input().split()))
pages = list(map(int,raw_input().split()))
print(helper(n,x,prices,pages))