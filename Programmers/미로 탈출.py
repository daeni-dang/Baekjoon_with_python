from collections import deque

def bfs(s_idx, end, maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque([[s_idx[0], s_idx[1], 0]])
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if maps[nx][ny] == "O" and not visited[nx][ny]:
                q.append([nx, ny, dist + 1])
                visited[nx][ny] = 1
            if end != "E" and maps[nx][ny] == "E" and not visited[nx][ny]:
                q.append([nx, ny, dist + 1])
                visited[nx][ny] = 1
            if end != "L" and (maps[nx][ny] == "L" or maps[nx][ny] == "S") and not visited[nx][ny]:
                q.append([nx, ny, dist + 1])
                visited[nx][ny] = 1
            if maps[nx][ny] == end:
                return dist + 1, nx, ny
    return -1, -1, -1

def solution(maps):
    answer = 0
    s_idx = []
    for i, map in enumerate(maps):
        tmp = map.find("S")
        if tmp != -1:
            s_idx = [i, tmp]
    dist, x, y = bfs(s_idx, "L", maps)
    if dist == -1:
        return -1
    dist2, *_ = bfs([x, y], "E", maps)
    if dist2 == -1:
        return -1
    answer = dist + dist2
    return answer