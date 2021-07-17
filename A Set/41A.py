s = input()
t = input()
ri = len(s)-1
reverse = True
for i in range(len(s)):
    if len(s) != len(t):
        reverse = False
        break
    if s[i] == t[ri]:
        ri -= 1
        continue
    else:
        reverse = False
        break

if reverse:
    print("YES")
else:
    print("NO")

# https://codeforces.com/problemset/problem/41/A