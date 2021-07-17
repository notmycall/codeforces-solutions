e = [int(x) for x in input().split('+')]
e.sort()
s = str(e[0])
for x in range(1, len(e)):
    s += f"+{e[x]}"
print(s)


# https://codeforces.com/problemset/problem/339/A