import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000)

def dfs(x, y, board, N, M):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if board[nx][ny] == 1:
            board[nx][ny] = 0
            dfs(nx, ny, board, N, M)

def bfs(x, y, board, N, M):
    q = deque([[x, y]])
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append([nx, ny])

def solution(N, M, board):
    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                board[i][j] = 0
                # bfs(i, j, board, N, M)
                dfs(i, j, board, N, M)
                answer += 1
    return answer

def main():
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        board = [[0] * M for _ in range(N)]
        for _ in range(K):
            y, x = map(int, input().split())
            board[x][y] = 1
        print(solution(N, M, board))

if __name__ == "__main__":
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    main()