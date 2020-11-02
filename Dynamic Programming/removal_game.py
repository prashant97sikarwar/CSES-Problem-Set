# Problem Link :- https://cses.fi/problemset/task/1097

def solve(arr,n):
    sm = 0
    for i in range(n):
        sm += arr[i]
    dp = [[0 for i in range(n)] for i in range(n)]
    for left in range(n-1,-1,-1):
        for right in range(left,n):
            if left == right:
                dp[left][right] = arr[left]
            else:
                dp[left][right] = max(arr[left] - dp[left+1][right],arr[right] - dp[left][right-1])
    ans = (sm + dp[0][n-1])/2
    return ans

n = int(raw_input())
arr = list(map(int,raw_input().split()))
print(solve(arr,n))
