def helper(mat,n):
    mod = 1000000007
    if mat[n-1][n-1] == '*':
        return 0
    dp = [[0 for i in range(n)] for i in range(n)]
    dp[n-1][n-1] = 1
    for i in range(n-2,-1,-1):
        if mat[i][n-1] == '*':
            dp[i][n-1] = 0
        else:
            dp[i][n-1] += dp[i+1][n-1]
    for i in range(n-2,-1,-1):
        if mat[n-1][i] == '*':
            dp[n-1][i] = 0
        else:
            dp[n-1][i] += dp[n-1][i+1]
    for i in range(n-2,-1,-1):
        for j in range(n-2,-1,-1):
            if mat[i][j] == '.':
                dp[i][j] = dp[i+1][j]  + dp[i][j+1]
            else:
                dp[i][j] = 0
    return dp[0][0]%mod
    
    
    
n = int(raw_input())
mat = []
for i in range(n):
    s = raw_input()
    mat.append(s)
print(helper(mat,n))