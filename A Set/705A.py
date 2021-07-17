n = int(input())
h, l = 'that I love ', 'that I hate '
s = 'I hate '
if n != 0:
    for i in range(n):
        if i == 0:
            pass
        elif i % 2:
            s += h
        else:
            s += l
s += "it"
print(s)

# https://codeforces.com/problemset/problem/705/A