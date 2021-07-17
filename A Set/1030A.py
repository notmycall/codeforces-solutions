n = int(input())
a = []
a = [int(x) for x in input().split()]
h = False
for x in range(n):
    if a[x] == 1:
        h = True
if h:
    print("HARD")
else:
    print("EASY")

# https://codeforces.com/problemset/problem/1030/A 