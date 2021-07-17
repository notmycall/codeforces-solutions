import string

s = input()
u, l = 0, 0
for c in s:
    if c.isupper():
        u += 1
    else:
        l += 1
if u > l:
    print(s.upper())
else:
    print(s.lower())

# https://codeforces.com/problemset/problem/59/A