import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = []

for _ in range(N):
    tomato.append(list(map(int, input().split())))

q = deque()
onecnt = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            onecnt += 1
            q.append([i, j, 0])
if onecnt == M * N:
    print(0)
else:
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y, day = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                q.append([nx, ny, day + 1])

    flag = False
    for i in range(N):
        if 0 in tomato[i]:
            print(-1)
            flag = True
            break
    if not flag:
        print(day)