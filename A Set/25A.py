n = int(input())
m = [int(x) for x in input().split()]

e, o = [], []
for i in range(n):
    if m[i] % 2:
        o.append(i+1)
    else:
        e.append(i+1)
if len(e) == 1:
    print(e[0])
else:
    print(o[0])

# https://codeforces.com/problemset/problem/25/A