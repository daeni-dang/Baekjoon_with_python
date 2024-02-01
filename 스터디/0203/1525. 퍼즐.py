import sys
from collections import deque
input = sys.stdin.readline

def findBlank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def getCurRight(board):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] - 1 == i * 3 + j:
                cnt += 1
    return cnt

def solution(board):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    sx, sy = findBlank(board)
    q = deque([[sx, sy, 0, board]])
    while q:
        cx, cy, dist, board = q.popleft()
        print(cx, cy)
        # for b in board:
        #     print(b)
        # print()
        if getCurRight(board) == 8:
            return dist
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= 3 or nx < 0 or ny >= 3 or ny < 0:
                continue
            board[nx][ny] = 0
            board[cx][cy] = board[nx][ny]
            q.append([nx, ny, dist + 1, board])
    return -1

def main():
    board = []
    for _ in range(3):
        board.append(list(map(int, input().split())))
    print(solution(board))

if __name__ == "__main__":
    main()