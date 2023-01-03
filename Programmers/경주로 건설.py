from collections import deque
import math

def solution(board):
    answer = 0
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 우, 하, 좌, 상
    right = bfs(0, 0, board, moves, 0)
    down = bfs(0, 0, board, moves, 1)
    answer = min(right, down)
    return answer

def bfs(x, y, board, moves, d):
    n = len(board)
    q = deque()
    q.append([x, y, 0, d])
    visited = [[math.inf] * n for _ in range(n)]
    visited[0][0] = 0
    while q:
        x, y, cost, prev_d = q.popleft()
        if x == n and y == n:
            break
        for i in range(len(moves)):
            nx = x + moves[i][0]
            ny = y + moves[i][1]
            n_cost = cost + 100 if i == prev_d else cost + 600   # 이전 방향과 현재 방향이 같다면 +100, 다르다면 코너이므로 +600
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 0 and visited[nx][ny] > n_cost:
                q.append([nx, ny, n_cost, i])
                visited[nx][ny] = n_cost

    return visited[n - 1][n - 1]

if __name__ == "__main__":
    board = [[0,0,0],[0,0,0],[0,0,0]]
    print(solution(board))