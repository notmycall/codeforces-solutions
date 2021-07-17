n, h = [int(x) for x in input().split()]
p = []
c = 0
p = [int(x) for x in input().split()]
for i in range(n):
    if p[i] <= h:
        c += 1
    else:
        c += 2
print(c)



# https://codeforces.com/problemset/problem/677/A