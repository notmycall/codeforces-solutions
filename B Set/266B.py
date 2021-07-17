n, t = [int(x) for x in input().split()]
s = list(input()) # Converts it into a string to make replacing values easier
j = False
for i in range(t):
    for x in range(n):
        if j: # Skips if the previous iteration made a switch
            j = False
            continue
        if x+1 >= n: # breaks if x+1 is out of bounds
            break
        elif s[x] == "B" and s[x+1] == "G":
            temp = s[x]
            s[x] = s[x+1]
            s[x+1] = temp
            j = True
print("".join(s))



# https://codeforces.com/problemset/problem/266/B