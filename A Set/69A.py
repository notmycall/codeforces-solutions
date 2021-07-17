n = int(input())
v = []
for i in range(n):
    y = [int(x) for x in input().split()]
    v.append(y)
    
t = 0
a, b, c = 0, 0, 0
for i in range(len(v)):
    a += v[i][0]
    b += v[i][1]
    c += v[i][2]

if a == 0 and b == 0 and c == 0:
    print("YES")
else:
    print("NO")

# https://codeforces.com/problemset/problem/69/A


