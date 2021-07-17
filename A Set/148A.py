k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

a = [k, l, m, n]

c = 0
for i in range(1, d+1):
    for x in range(4):
        if i % a[x] == 0:
            c += 1
            break
print(c)

# https://codeforces.com/problemset/problem/148/A