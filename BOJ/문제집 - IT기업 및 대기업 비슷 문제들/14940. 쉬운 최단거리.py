import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque([[x, y]])
    visited = [[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                visited[i][j] = 0
    visited[x][y] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if visited[nx][ny] == -1 and board[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[cx][cy] + 1
    return visited

def find2():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                return i, j

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    x, y = find2()
    visited = bfs(x, y)
    for v in visited:
        print(*v)