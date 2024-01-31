import sys
from collections import deque
input = sys.stdin.readline

def findStart(w, h, board):
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                return i, j

def findFire(w, h, board):
    fires = deque()
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fires.append([i, j])
    return fires

def fire(w, h, board, fires):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    nextFires = deque()
    while fires:
        cx, cy = fires.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= h or nx < 0 or ny >= w or ny < 0:
                continue
            if board[nx][ny] == '.':
                board[nx][ny] = '*'
                nextFires.append([nx, ny])
    return nextFires


def solution(w, h, board):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False] * w for _ in range(h)]
    sx, sy = findStart(w, h, board)
    board[sx][sy] = '.'
    fires = findFire(w, h, board)
    q = deque([[sx, sy, 0]])
    befDist = 0
    while q:
        cx, cy, dist = q.popleft()
        if befDist != dist:
            # 불 하나 확산시키기
            fires = fire(w, h, board, fires)
            befDist = dist
        if board[cx][cy] == '*':
            continue
        # 건물 탈출 성공
        if cx == 0 or cy == 0 or cx == h - 1 or cy == w - 1:
            return dist + 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= h or nx < 0 or ny >= w or ny < 0:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if board[nx][ny] == '.':
                q.append([nx, ny, dist + 1])
    return "IMPOSSIBLE"

def main():
    T = int(input())
    for _ in range(T):
        w, h = map(int, input().split())
        board = []
        for _ in range(h):
            board.append(list(input().strip()))
        print(solution(w, h, board))

if __name__ == "__main__":
    main()