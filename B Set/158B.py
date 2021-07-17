n = int(input())
g = [int(x) for x in input().split()]
g.sort(reverse=True)
r = 0
oneFreeSpace, twoRiders, singleRider = 0, 0, 0
for c in range(n):
    if g[c] == 4:
        r += 1
    elif g[c] == 3:
        r += 1
        oneFreeSpace += 1
    elif g[c] == 2:
        twoRiders += 1
    else:
        singleRider += 1

while oneFreeSpace > 0 and singleRider > 0: # Filling up cars that have a single seat available
    singleRider -= 1
    oneFreeSpace -= 1

t = (twoRiders * 2) + singleRider # Filling up cars with remaining groups of two and one. 

if t == 0:
    pass
elif t <= 4:
    r += 1
    t = 0
else:
    while t >= 4:
        r += 1
        t -= 4 
    if t != 0:
        r += 1
        t = 1

print(r)
    
# https://codeforces.com/problemset/problem/158/B

