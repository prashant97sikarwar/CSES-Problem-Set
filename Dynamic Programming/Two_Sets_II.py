#Problem Link:- https://cses.fi/problemset/task/1093

def solve(n):
    mod = 1000000007
    total = (n*(n+1))/2
    if total%2 == 1:
        return 0
    sm = total//2
    dp = [[0 for i in range(sm+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,sm+1):
            if j >= i:
                dp[i][j] = (dp[i-1][j-i]%mod + dp[i-1][j]%mod)%mod
            else:
                dp[i][j] = (dp[i-1][j])%mod
    return (dp[n][sm] * 500000004)%mod

n = int(raw_input())
print(solve(n))