import sys
from collections import deque
input = sys.stdin.readline

def getCurRight(board):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] - 1 == i * 3 + j:
                cnt += 1
    return cnt

def solution(board):
    visited = [[False] * 3 for _ in range(3)]
    q = deque([[0, 0, 0]])
    while q:
        cx, cy, dist = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= 3 or nx < 0 or ny >= 3 or ny < 0:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                board[nx][ny], board[cx][cy] = board[cx][cy], board[nx][ny]
                if getCurRight(board) == 8:
                    return dist
                for b in board:
                    print(b)
                print()
                q.append([nx, ny, dist + 1])
    return -1

def main():
    board = []
    for _ in range(3):
        board.append(list(map(int, input().split())))
    print(solution(board))

if __name__ == "__main__":
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    main()