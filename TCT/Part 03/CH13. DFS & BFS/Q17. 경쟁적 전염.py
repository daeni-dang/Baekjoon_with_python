import sys
from collections import deque

n, k = map(int, input().split())
graph = []
virus = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))
virus.sort() # 바이러스 번호가 작은 것부터 증식하므로 바이러스 번호로 정렬
q = deque(virus)
s_, x_, y_ = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    v_num, s, x, y = q.popleft()
    if s == s_:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v_num
                q.append((v_num, s + 1, nx, ny))
print(graph[x_ - 1][y_ - 1])