s = input()
newString = ''
for char in range(len(s)):
    if s[char].lower() in "aoyeui":
        pass
    else:
        newString += f".{s[char].lower()}"
print(newString)

# https://codeforces.com/problemset/problem/118/A