#Problem Link:- https://cses.fi/problemset/task/1094

n = int(raw_input())
arr = list(map(int,raw_input().split()))
sm = 0
for i in range(1,n):
    if arr[i] < arr[i-1]:
        dep = (arr[i-1] - arr[i])
        sm += dep
        arr[i] = arr[i] + dep
print(sm)
    
