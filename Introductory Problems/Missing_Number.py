#Problem Link :- https://cses.fi/problemset/task/1083

n = int(raw_input())
arr = list(map(int,raw_input().split()))
sm = 0
for i in range(n-1):
    sm += arr[i]
total = n*(n+1)/2
print(total - sm)