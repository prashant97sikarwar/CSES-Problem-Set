# Problem Link :- https://cses.fi/problemset/task/1639

def solve(str1,str2):
    n = len(str1)
    m = len(str2)
    dp = [[0 for i in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
      .          dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    return dp[n][m]

str1 = raw_input()
str2 = raw_input()
print(solve(str1,str2))