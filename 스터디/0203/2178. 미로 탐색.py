import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, board):
    visited = [[False] * m for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([[0, 0, 1]])
    visited[0][0] = True
    while q:
        curX, curY, dist = q.popleft()
        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]
            if nx == n - 1 and ny == m - 1:
                return dist + 1
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if board[nx][ny] == 1:
                q.append([nx, ny, dist + 1])

def main():
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().strip())))
    print(solution(n, m, board))

if __name__ == "__main__":
    main()