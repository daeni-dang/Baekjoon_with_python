import sys
from collections import deque
input = sys.stdin.readline

def findSWater(r, c, board):
    sx, sy = 0, 0
    waters = deque()
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'S':
                sx, sy = i, j
            elif board[i][j] == '*':
                waters.append([i, j])
    return sx, sy, waters

def water(r, c, board, waters):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    nextWaters = deque()
    while waters:
        wx, wy = waters.popleft()
        for i in range(4):
            nx = wx + dx[i]
            ny = wy + dy[i]
            if nx >= r or nx < 0 or ny >= c or ny < 0:
                continue
            if board[nx][ny] == '.':
                board[nx][ny] = '*'
                nextWaters.append([nx, ny])
    return nextWaters

def solution(r, c, board):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False] * c for _ in range(r)]
    sx, sy, waters = findSWater(r, c, board)
    befDist = 0
    q = deque([[sx, sy, 0]])
    while q:
        cx, cy, dist = q.popleft()
        if dist != befDist:
            waters = water(r, c, board, waters)
            befDist = dist
        if board[cx][cy] == '*':
            continue
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= r or nx < 0 or ny >= c or ny < 0:
                continue
            if board[nx][ny] == 'D':
                return dist + 1
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if board[nx][ny] == '.':
                q.append([nx, ny, dist + 1])
    return "KAKTUS"

def main():
    r, c = map(int, input().split())
    board = []
    for _ in range(r):
        board.append(list(input().strip()))
    print(solution(r, c, board))

if __name__ == "__main__":
    main()