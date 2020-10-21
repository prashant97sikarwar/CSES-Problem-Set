# Problem Link :- https://cses.fi/problemset/task/1746

def solve(n,m,arr):
    dp = [[0 for i in range(m+2)] for i in range(n+1)]
    for i in range(1,n+1):
        for x in range(1,m+1):
            if i == 1:
                if arr[i-1] == 0 or arr[i-1] == x:
                    dp[i][x] = 1
                else:
                    dp[i][x] = 0
            else:
                if arr[i-1] == 0 or arr[i-1] ==  x:
                    dp[i][x] = ((dp[i-1][x-1] + dp[i-1][x])%MOD + dp[i-1][x+1])%MOD
                else:
                    dp[i][x] = 0
    ans = 0
    for x in range(1,m+1):
        ans += (dp[n][x]%MOD)
        ans %= MOD
    return ans

MOD=1000000007
n,m = map(int,raw_input().split())
arr = list(map(int,raw_input().split()))
print(solve(n,m,arr))
