n = int(input())
s = input()
l = len(s)
d = []
for i in range(l):
    if i+1 == l:
        break
    elif s[i] == s[i+1]:
        d.append(s[i])
print(len(d))

# https://codeforces.com/problemset/problem/266/A