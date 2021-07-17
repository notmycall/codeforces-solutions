n = int(input())
v = [int(x) for x in input().split()]
a = []
c = 1
for i in range(1, n+1):
    for x in range(n):
        if i == v[x]:
            a.append(x+1)

for i in range(len(a)):
    print(a[i], end= " ")

# https://codeforces.com/problemset/problem/136/A