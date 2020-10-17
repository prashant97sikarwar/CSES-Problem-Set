# Problem Link :- https://cses.fi/problemset/task/1636

def fun(arr,n,k):
    mod = 1000000007
    arr.sort()
    dp = [0 for i in range(k+1)]
    dp[0] = 1
    for i in range(n):
        for j in range(1,k+1):
            if j >= arr[i]:
                dp[j] += (dp[j-arr[i]]%mod)
                dp[j] %= mod
    return dp[k]


n,k = map(int,raw_input().split())
arr = list(map(int,raw_input().split()))
print(fun(arr,n,k))