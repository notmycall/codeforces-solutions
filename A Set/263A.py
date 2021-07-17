row1 = [int(x) for x in input().split()]
row2 = [int(x) for x in input().split()]
row3 = [int(x) for x in input().split()]
row4 = [int(x) for x in input().split()]
row5 = [int(x) for x in input().split()]

matrix = [row1, row2, row3, row4, row5]
onePosition = []
rowCounter = 0
for row in matrix:
    indexCounter = 0
    for value in row:
        if value == 1:
            onePosition.append(rowCounter)
            onePosition.append(indexCounter)
        indexCounter += 1
    rowCounter += 1

midPoint = [2, 2]
print(abs(onePosition[0] - midPoint[0]) + abs(onePosition[1] - midPoint[1]))

# https://codeforces.com/problemset/problem/263/A
