v = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
s = input()
pangram = True
for letter in range(len(v)):
    if v[letter] in s.lower():
        continue
    else:
        pangram = False
if pangram:
    print("YES")
else:
    print("NO")

# https://codeforces.com/problemset/problem/520/A