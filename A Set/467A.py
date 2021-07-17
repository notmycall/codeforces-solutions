n = int(input())
r = []
for i in range(n):
    r.append([int(x) for x in input().split()])
c = 0
for x in range(len(r)):
    if r[x][1] - r[x][0] >= 2:
        c += 1
print(c)

# https://codeforces.com/problemset/problem/467/A