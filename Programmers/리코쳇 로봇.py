from collections import deque

def getRGpoint(board):
    R = []
    G = []
    cnt = 0
    for i, col in enumerate(board):
        findR = col.find("R")
        findG = col.find("G")
        if findR != -1:
            R = [i, findR]
            cnt += 1
        if findG != -1:
            G = [i, findG]
            cnt += 1
        if cnt == 2:
            break
    return R, G

def solution(board):
    answer = 0
    R, G = getRGpoint(board)
    
    n, m = len(board), len(board[0])
    cnt = [[10001] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    cnt[R[0]][R[1]] = 0
    visited[R[0]][R[1]] = 1
    q = deque([R])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx >= n or ny >= m or nx < 0 or ny < 0:
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                if board[nx][ny] == "D":
                    nx -= dx[i]
                    ny -= dy[i]
                    break
            
            if visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            q.append([nx, ny])
            cnt[nx][ny] = min(cnt[nx][ny], cnt[x][y] + 1)
            if board[nx][ny] == "G":
                return cnt[nx][ny]
    
    return -1