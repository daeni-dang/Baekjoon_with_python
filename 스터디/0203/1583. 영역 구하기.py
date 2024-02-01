import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y, board, N, M, visited):
    global cnt
    if x < N and x >= 0 and y < M and y >= 0:
        if board[x][y] == 0:
            visited[x][y] = True
            cnt += 1
            board[x][y] = 1
            dfs(x + 1, y, board, N, M, visited)
            dfs(x - 1, y, board, N, M, visited)
            dfs(x, y + 1, board, N, M, visited)
            dfs(x, y - 1, board, N, M, visited)

def solution(N, M, board):
    global cnt
    answer = []
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                dfs(i, j, board, N, M, visited)
                answer.append(cnt)
                cnt = 0
    return sorted(answer)

def main():
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1, x2):
            for j in range(y1, y2):
                board[i][j] = 1
    answer = solution(N, M, board)
    print(len(answer))
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    cnt = 0
    main()