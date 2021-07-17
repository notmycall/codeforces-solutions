n = int(input())
x = [int(x) for x in input().split()]
y  = [int(y) for y in input().split()]

v = x[1:] + y[1:]
v.sort()
c = 0
for i in range(len(v)):
    if v[i] == c+1:
        c += 1
if c == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")


# https://codeforces.com/problemset/problem/469/A