n, m, a = [int(x) for x in input().split()]
if n % a: 
    w = n//a + 1
else:
    w = n//a
if m % a:
    h = m//a + 1
else:
    h = m//a
print(w*h)

# https://codeforces.com/problemset/problem/1/A