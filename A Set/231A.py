l = int(input())
counter = 0
for i in range(l):
    a, b, c = [int(x) for x in input().split()]
    if a + b + c >= 2:
        counter += 1
print(counter)

# https://codeforces.com/problemset/problem/231/A