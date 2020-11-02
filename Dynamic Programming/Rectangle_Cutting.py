# problem Link :- https://cses.fi/problemset/task/1744

def solve(a,b):
    MAX = 10000000
    dp = [[0 for i in range(b+1)] for i in range(a+1)]
    for height in range(1,a+1):
        for width in range(1,b+1):
            if height == width:
                dp[height][width] = 0
            else:
                ans = MAX
                for i in range(1,width):
                    ans = min(ans,1 + dp[height][i] + dp[height][width-i])
                for i in range(1,height):
                    ans = min(ans,1 + dp[i][width] + dp[height-i][width])
                dp[height][width] = ans
    return dp[a][b]

a,b = map(int,raw_input().split())
print(solve(a,b))