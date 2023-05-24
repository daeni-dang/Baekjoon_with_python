from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    n, m = len(arr), len(arr[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited[x][y] = True
    q = deque([[x, y]])
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if visited[nx][ny]:
                continue
            if arr[nx][ny] == 1 and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = True

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        answer = 0
        M, N, K = map(int, input().split())
        arr = [[0] * M for _ in range(N)]
        for _ in range(K):
            x, y = map(int, input().split())
            arr[y][x] = 1
        
        visited = [[False] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 1 and not visited[i][j]:
                    bfs(i, j)
                    answer += 1
        print(answer)