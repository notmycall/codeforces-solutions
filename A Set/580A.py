n = int(input())
m = [int(x) for x in input().split()]
c =m[0]
c = 1
h = 1
for i in range(n):
    if i == n-1:
        break
    if m[i] <= m[i+1]:
        c += 1
        if c > h:
            h = c
    else:
        c = 1
print(h)

# https://codeforces.com/problemset/problem/580/A