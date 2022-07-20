n = int(input())

melon = [list(map(int, input().split())) for i in range(6)]

maxCol, maxColIdx = 0, 0
maxRow, maxRowIdx = 0, 0

for i in range(len(melon)):
    if melon[i][0] <= 2:
        if melon[i][1] > maxCol:
            maxCol = melon[i][1]
            maxColIdx = i
    else:
        if melon[i][1] > maxRow:
            maxRow = melon[i][1]
            maxRowIdx = i

shortCol = abs(melon[(maxColIdx - 1) % 6][1] - melon[(maxColIdx + 1) % 6][1])
shortRow = abs(melon[(maxRowIdx - 1) % 6][1] - melon[(maxRowIdx + 1) % 6][1])

print(n * ((maxCol * maxRow) - (shortCol * shortRow)))