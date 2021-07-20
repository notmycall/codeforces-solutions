n = int(input())
bills = [100, 20, 10, 5, 1]
t = 0
for bill in range(len(bills)):
    t += n // bills[bill] 
    n = n % bills[bill] 
print(t)

# https://codeforces.com/problemset/problem/996/A