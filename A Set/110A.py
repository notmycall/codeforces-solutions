s = input()
c = 0
for i in range(len(s)):
    if s[i] == "4" or s[i] == "7":
        c += 1
if c == 4 or c == 7:
    print("YES")
else:
    print("NO")

# https://codeforces.com/problemset/problem/110/A