l = int(input())
s = []
for x in range(l):
    s.append([int(x) for x in input().split()])
m = 0
c = 0
for i in range(l):
    c -= s[i][0]
    c += s[i][1]
    if m < c:
        m = c
print(m)

# https://codeforces.com/problemset/problem/116/A