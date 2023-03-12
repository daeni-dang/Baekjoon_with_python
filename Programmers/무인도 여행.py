from collections import deque

def bfs(maps, s_idx, visited):
    n = len(maps)
    m = len(maps[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt = int(maps[s_idx[0]][s_idx[1]])
    visited[s_idx[0]][s_idx[1]] = 1
    q = deque([s_idx])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if maps[nx][ny] != "X" and not visited[nx][ny]:
                q.append([nx, ny])
                cnt += int(maps[nx][ny])
                visited[nx][ny] = 1
    return cnt, visited

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and not visited[i][j]:
                cnt, visited = bfs(maps, [i, j], visited)
                if cnt != 0:
                    answer.append(cnt)
                    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer