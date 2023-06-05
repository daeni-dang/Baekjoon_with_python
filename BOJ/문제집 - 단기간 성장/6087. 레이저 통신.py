from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    answer = 0
    visited = [[0] * w for _ in range(h)]
    visited[x][y] = 1
    # 오, 왼, 아, 위
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = deque([[x, y, 0]])
    while q:
        answer += 1
        cx, cy, dist = q.popleft()
        for i in range(4):
            nx = cx
            ny = cy
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx >= h or nx < 0 or ny >= w or ny < 0:
                    break
                if board[nx][ny] == "*":
                    break
                if not visited[nx][ny] and board[nx][ny] == "C":
                    return dist
                if board[nx][ny] == "." and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx, ny, dist + 1])
    
    return answer

def findStart():
    for i in range(h):
        for j in range(w):
            if board[i][j] == "C":
                return [i, j]

if __name__ == "__main__":
    w, h = map(int, input().split())
    board = []
    for _ in range(h):
        board.append(list(input().strip()))
    start = findStart()
    answer = bfs(start[0], start[1])
    print(answer)