n = int(input())
teams = []
for i in range(n):
    teams.append([int(x) for x in input().split()])
c = 0

for t in range(n):
    for x in range(n):
        if t == x:
            continue
        if teams[t][0] == teams[x][1]:
            c += 1
print(c)

# https://codeforces.com/problemset/problem/268/A