import sys
input = sys.stdin.readline

def dfs(x, y, board, N, visited):
    global cnt
    if x < N and x >= 0 and y < N and y >= 0:
        if not visited[x][y] and board[x][y] == 1:
            visited[x][y] = True
            cnt += 1
            board[x][y] = 0
            dfs(x + 1, y, board, N, visited)
            dfs(x - 1, y, board, N, visited)
            dfs(x, y + 1, board, N, visited)
            dfs(x, y - 1, board, N, visited)

def solution(N, board):
    global cnt
    visited = [[False] * N for _ in range(N)]
    answer = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                dfs(i, j, board, N, visited)
                answer.append(cnt)
                cnt = 0
    return sorted(answer)

def main():
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, list(input().strip()))))
    answer = solution(N, board)
    print(len(answer))
    [print(ans) for ans in answer]

if __name__ == "__main__":
    cnt = 0
    main()