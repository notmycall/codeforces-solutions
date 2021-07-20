n = int(input())
a = [int(x) for x in input().split()]
min, min_index = 101, 0
max, max_index = 0, 0
for index, value in enumerate(a):
    if min >= value:
        min = value
        min_index = index
        
    if max < value:
        max = value
        max_index = index

sorted = a[:]
sorted.sort()
if sorted[0] == a[max_index] and sorted[-1] == a[min_index]:
    print(0)
elif max_index < min_index:
    print(max_index + n-1-min_index)
else:
    print(max_index + n-2-min_index) # -1 move as two two of the moves can be made as one

# https://codeforces.com/problemset/problem/144/A