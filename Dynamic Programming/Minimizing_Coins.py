# Problem Link:- https://cses.fi/problemset/task/1634

n,x = map(int,raw_input().split())
arr = list(map(int,raw_input().split()))
dp = [x+1 for i in range(x+1)]
dp[0] = 0
arr.sort()
for i in range(n):
    for j in range(1,x+1):
        if j >= arr[i]:
            dp[j] = min(1 + dp[j-arr[i]],dp[j])
if dp[x] < x + 1:
    print(dp[x])
else:
    print(-1)
    