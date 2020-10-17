# Problem Link :- https://cses.fi/problemset/task/1635

n,x = map(int,raw_input().split())
arr = list(map(int,raw_input().split()))
arr.sort()
dp = [0 for i in range(x+1)]
dp[0] = 1
mod = 1000000007
for j in range(1,x+1):
    for i in range(n):
        if j >= arr[i]:
            dp[j] += (dp[j-arr[i]])%mod
            dp[j] %= mod
print(dp[x])