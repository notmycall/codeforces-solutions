n, k = [int(x) for x in input().split()]

for i in range(k):
    if str(n)[-1]  == "0":
        n  = int(n / 10)
    else:
        n -= 1
print(n)

# https://codeforces.com/problemset/problem/977/A