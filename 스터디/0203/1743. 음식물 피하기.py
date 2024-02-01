import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y, board, N, M, visited):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if visited[nx][ny]:
            continue
        visited[nx][ny] = True
        if board[nx][ny] == 1:
            cnt += 1
            dfs(nx, ny, board, N, M, visited)

def solution(N, M, board):
    global cnt
    answer = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] != -1:
                visited[i][j] = True
                dfs(i, j, board, N, M, visited)
                answer = max(answer, cnt)
                cnt = 1
    for i in range(N):
        for j in range(M):
            if answer < board[i][j]:
                answer = board[i][j]
    return answer

def main():
    N, M, K = map(int, input().split())
    board = [[-1] * M for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().split())
        board[r - 1][c - 1] = 1
    print(solution(N, M, board))

if __name__ == "__main__":
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 1
    main()