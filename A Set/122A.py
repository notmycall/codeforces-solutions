n = int(input()) 

# Gets the lucky numbers and stores them in a list. 
ln = []
v = "01235689"
for i in range(2, n+1):
    l = len(str(i))
    c = 0
    for x in range(l):
        if str(i)[x] not in v:
            c += 1
    if l == c:
        ln.append(int(i))

# If the module of n and the value in ls is 0, then it is divisible
al = False
for y in range(len(ln)):
    if n % ln[y] == 0:
        al = True
        break
if al:
    print("YES")
else:
    print("NO")



# https://codeforces.com/problemset/problem/122/A