import re
s = input()
s = s.replace("WUB", " ")
s = re.sub(r'\s\s+',' ', s)
s = s.strip()
print(s)

# https://codeforces.com/problemset/problem/208/A