o = input()
t = input()
a = ''
for i in range(len(o)):
    if o[i] == '1' and t[i] == '1':
        a += '0'
    elif o[i] == '1' or t[i] == '1':
        a += '1'
    else:
        a += '0'
print(a)

# https://codeforces.com/problemset/problem/61/A