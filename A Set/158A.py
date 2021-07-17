n, k = [int(x) for x in input().split()]
scores = [int(x) for x in input().split()]
counter = 0
for i in range(n):
    if scores[i] >= scores[k-1] and scores[i] != 0:
        counter += 1
print(counter)

# https://codeforces.com/problemset/problem/158/A