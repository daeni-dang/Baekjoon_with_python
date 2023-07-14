from collections import deque

def bfs(i, j, color):
    q = deque([[i, j]])
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if not visited[nx][ny] and board[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append([nx, ny])
        

N = int(input())
board = []
for _ in range(N):
    board.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = [0] * 2
# 적록색약 x
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, board[i][j])
            answer[0] += 1
# 적록색약 o
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j] == "G":
            board[i][j] = "R"
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, board[i][j])
            answer[1] += 1
[print(a, end=" ") for a in answer]
