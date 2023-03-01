from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    start = [0, 0, 1] # x, y, dist
    queue = deque([start])
    visited[0][0] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(nx >= n or nx < 0 or ny >= m or ny < 0):
                if nx == n - 1 and ny == m - 1:
                    return dist + 1
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append([nx, ny, dist + 1])
                    visited[nx][ny] = True
    return -1