import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, board):
    answer = 0
    q = deque()
    need = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                q.append([i, j, 0])
            elif board[i][j] == 0:
                need += 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        cx, cy, dist = q.popleft()
        if dist > answer:
            answer = dist
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                need -= 1
                q.append([nx, ny, dist + 1])
    if need == 0:
        return dist
    return -1

def main():
    m, n = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    print(solution(n, m, board))

if __name__ == "__main__":
    main()