#Problem Link :- https://cses.fi/problemset/task/1068

n = int(raw_input())
print n,
while n != 1:
    if n%2 == 0:
        n = n//2
        print n,
    else:
        n = 3*n + 1
        print n,
