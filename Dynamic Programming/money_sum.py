#Problem Link :- https://cses.fi/problemset/task/1745

n = int(raw_input())
coins = list(map(int,raw_input().split()))
sm = sum(coins)
dp = [[False for i in range(sm+1)] for i in range(n+1)]
coins.sort()
for i in range(n+1):
    dp[i][0] = True
for i in range(1,sm+1):
    dp[0][i] = False
dp[0][0] = True
for i in range(1,n+1):
    for j in range(1,sm+1):
        if j >= coins[i-1]:
            dp[i][j] = dp[i-1][j-coins[i-1]] or dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]
count = 0
for i in range(1,sm+1):
    if dp[n][i] == True:
        count += 1
print(count)
for i in range(1,sm+1):
    if dp[n][i] == True:
        print i,
    