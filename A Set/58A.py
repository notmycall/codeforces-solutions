s = input().lower()

h = 'hello'
c = 0
for i in range(len(s)):
    if c == 5:
        break
    elif s[i] == h[c]:
        c += 1
        continue
if c == 5:
    print("YES")
else:
    print("NO")

# https://codeforces.com/problemset/problem/58/A