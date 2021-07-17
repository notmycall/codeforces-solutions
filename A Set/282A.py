l = int(input())
x = 0
for i in range(l):
    s = input()
    if "++" in s:
        x += 1
    elif "--" in s:
        x -= 1
print(x)

# https://codeforces.com/problemset/problem/282/A