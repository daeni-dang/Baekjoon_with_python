xall = []
yall = []
for i in range(3):
    x, y = map(int, input().split())
    xall.append(x)
    yall.append(y)

result = []
for i in range(3):
    if xall.count(xall[i]) == 1:
        result.append(xall[i])

for i in range(3):
    if yall.count(yall[i]) == 1:
        result.append(yall[i])
print(result[0], result[1])