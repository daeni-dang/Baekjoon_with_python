n = int(input())

color = [[0] * 100 for _ in range(100)]

for i in range(n):
    x, y = map(int, input().split())
        
    for j in range(y - 1, y + 9):
        for k in range(x - 1, x + 9):
            color[j][k] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if color[i][j] == 1:
            cnt += 1
print(cnt)