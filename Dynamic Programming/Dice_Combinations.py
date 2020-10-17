# Problem Link :- https://cses.fi/problemset/task/1633

mod = 1000000007
def fun(n):
    dp  = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        for j in range(1,7):
            if j > i:
                break
            dp[i] += (dp[i-j]%mod)
            dp[i] %=  mod
    return dp[n]%mod
n = int(raw_input())
print(fun(n))