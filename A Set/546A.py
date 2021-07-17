k, h, w = [int(x) for x in input().split()]
t = 0
for i in range(w):
    t += k * (i+1)

if t - h < 0:
    print(0)
else:
    print(abs(h-t))

# https://codeforces.com/problemset/problem/546/A