s = input()
i = "HQ9"
t = False
for c in range(len(s)):
    if s[c] in i:
        t = True
        break
if t:
    print("YES")
else:
    print("NO")

# https://codeforces.com/problemset/problem/133/A