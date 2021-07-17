x = int(input())
e = 0

c = 0
while e < x:
    if e + 5 < x:
        e += 5
        c += 1
    else:
        c += 1
        break
print(c)

# https://codeforces.com/problemset/problem/617/A