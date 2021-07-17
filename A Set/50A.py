m, n = [int(x) for x in input().split()]
rowendspot = False
if m % 2:
    rowendspot = True
if rowendspot:
    total = (m // 2) * n + (n // 2)
else:
    total = (m // 2) * n
print(total)

# https://codeforces.com/problemset/problem/50/A