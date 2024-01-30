'''
    참고 : https://data-flower.tistory.com/85
'''

import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, board):
    if n == 1 and m == 1:
        return 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque([[0, 0, 1, 1]])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    while q:
        cx, cy, canBreak, dist = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if nx == n - 1 and ny == m - 1:
                return dist + 1
            if board[nx][ny] == '0' and visited[nx][ny][canBreak] == 0:
                visited[nx][ny][canBreak] = 1
                q.append([nx, ny, canBreak, dist + 1])
            elif board[nx][ny] == '1' and canBreak:
                visited[nx][ny][0] = 0
                q.append([nx, ny, 0, dist + 1])
    return -1

def main():
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(input().strip()))
    print(solution(n, m, board))

if __name__ == "__main__":
    main()