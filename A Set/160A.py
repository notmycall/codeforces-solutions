n = input()
c = [int(x) for x in input().split()]
c.sort(reverse=True)
t = sum(c)
x, y = 0, 0 # sum and num of coins taken so far
for i in range(len(c)):
    x += c[i]
    y += 1
    if x > t//2:
        print(y)
        break

# https://codeforces.com/problemset/problem/160/A