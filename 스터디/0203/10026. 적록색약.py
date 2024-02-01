import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y, board, N, visited, color):
    if x < N and x >= 0 and y < N and y >= 0:
        if not visited[x][y] and color == board[x][y]:
            visited[x][y] = True
            dfs(x + 1, y, board, N, visited, color)
            dfs(x - 1, y, board, N, visited, color)
            dfs(x, y + 1, board, N, visited, color)
            dfs(x, y - 1, board, N, visited, color)
            

def solution(N, board):
    yes, no = 0, 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, board, N, visited, board[i][j])
                yes += 1
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'R':
                board[i][j] = 'G'
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, board, N, visited, board[i][j])
                no += 1
    return yes, no

def main():
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(input().strip()))
    answer = solution(N, board)
    print(answer[0], answer[1])

if __name__ == "__main__":
    main()