s = input()
fc = False
c, l = 0, 0

for i in range(len(s)):
    if i == 0:
        if s[i].isupper():
            fc = True
    elif s[i].isupper():
        c += 1
    else:
        l += 1

if fc == True and c == 0 and l == 0:
    print(s.lower())
elif fc == False and c == 0 and l == 0:
    print(s.upper())
elif fc and c >= 1 and l == 0:
    print(s.lower())
elif fc == False and c>= 1 and l == 0:
    print(s[0].upper()+s[1:].lower())
else:
    print(s)

# https://codeforces.com/problemset/problem/131/A