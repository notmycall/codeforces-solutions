t = int(input())
n = []
for i in range(t):
    n.append([int(x) for x in input().split()])

a = []
for x in range(t):
    if (n[x][0]) % n[x][1] == 0:
        a.append(0)
    else:
        a.append((n[x][0] // n[x][1] + 1) * n[x][1] - n[x][0]) #### This needs recalculating

for m in a:
    print(m)

# https://codeforces.com/problemset/problem/1328/A