#Problem Link:- https://cses.fi/problemset/task/1069

s = raw_input()
mx = 0
length = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        length += 1
    else:
        mx = max(mx,length)
        length = 1
mx = max(length,mx)
print(mx)