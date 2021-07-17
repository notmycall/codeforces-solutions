r = [int(x) for x in input()]
c = 1
for i in range(len(r)):
    if c == 7:
        print("YES")
        break
    elif i+1 == len(r):
        print("NO")
        break
    elif r[i] == r[i+1]:
        c += 1
    else:
        c = 1

# https://codeforces.com/problemset/problem/96/A