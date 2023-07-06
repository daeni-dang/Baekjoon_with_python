from collections import deque

def bfs(x, y, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([[x, y]])
    visited[x][y] = True
    cnt = 0
    while q:
        cx, cy = q.popleft()
        cnt += 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny])
    return visited, cnt
        

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

visited = [[False] * N for _ in range(N)]
count = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            visited, cnt = bfs(i, j, visited)
            count.append(cnt)
count.sort()
print(len(count))
for i in count:
    print(i)