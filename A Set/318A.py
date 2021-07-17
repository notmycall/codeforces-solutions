''' # Time limit exceeded
n, k = [int(x) for x in input().split()]
o, e = [], []
for i in range(1, n+1):
    if i % 2:
        o.append(i)
    else:
        e.append(i)
l = o + e
print(l[k-1])
''' 

# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9
# 1 3 5 7 
# 2 4 6

n, k = [int(x) for x in input().split()]
m = 0
if n % 2:
    m = (n+1) // 2
else:
    m = n/2 
if k <= m:
    print(k + k-1)
else:
    print(int((k - m) * 2))


# https://codeforces.com/problemset/problem/318/A