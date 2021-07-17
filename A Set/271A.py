def isDistinct(n):
    n = str(n)
    d = []
    for i in range(len(n)):
        if n[i] not in d:
            d.append(n[i])
        else:
            return False
    return True

n = int(input())+1
while not isDistinct(n):
    n += 1
print(n)

# https://codeforces.com/problemset/problem/271/A