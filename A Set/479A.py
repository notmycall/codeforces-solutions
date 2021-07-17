a = int(input())
b = int(input())
c = int(input())
n = [a, b, c]
v = []
v.append((a+b)*c)
v.append(a + (b*c))
v.append(a * (b+c))
v.append(a * b * c)
v.append(a + b + c)
v.sort()
print(v[-1])

# https://codeforces.com/problemset/problem/479/A

