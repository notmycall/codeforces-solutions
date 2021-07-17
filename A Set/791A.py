a, b = [int(x) for x in input().split()]
c = 0
while a <= b:
    a = a*3
    b = b*2
    c += 1
print(c)

# https://codeforces.com/problemset/problem/791/A