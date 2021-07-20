n, m = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]
p.sort()
s = []

if m-n == 0:
    print(p[-1]-p[0])
else:
    for i in range(m-n+1):
        s.append(p[n-1+i]-p[i])
    s.sort()
    print(s[0])

# https://codeforces.com/problemset/problem/337/A