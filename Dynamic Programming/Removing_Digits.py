# Problem Link :- https://cses.fi/problemset/task/1637
n = int(raw_input())
dp = [0 for i in range(n+1)]
for i in range(1,n+1):
    temp = i
    dp[i] = 1000002
    while temp > 0:
        rem = temp%10
        if rem == 0:
            temp = temp//10
            continue
        dp[i] = min(1 + dp[i-rem],dp[i])
        temp = temp//10
print(dp[n])