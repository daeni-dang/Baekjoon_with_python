import sys

n, m = map(int, input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int, sys.stdin.readline().split())))
temp = [[0] * m for _ in range(n)]
result = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def dfs(wall):
    global result
    if wall == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        count = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    count += 1
        result = max(result, count)
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall += 1
                dfs(wall)
                lab[i][j] = 0
                wall -= 1
                
dfs(0)
print(result)