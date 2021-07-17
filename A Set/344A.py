n = int(input())
m = []
c = 1
for i in range(n):
    m.append(input())
for x in range(n-1):
    if m[x][1] == m[x+1][0]:
        c += 1
print(c)

# https://codeforces.com/problemset/problem/344/A
