s = input()
s = s[1:-1]
v = []
for c in s:
    if c == ',' or c.isspace():
        pass
    else:
        v.append(c)
v = set(v)
print(len(v))

# https://codeforces.com/problemset/problem/443/A