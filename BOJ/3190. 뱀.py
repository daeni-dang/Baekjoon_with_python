import sys
from collections import deque
input = sys.stdin.readline

def start():
    time = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque([[1, 1, 0]])
    board[1][1] = 3 # 뱀
    snakes = deque([[1, 1]])
    while q:
        curX, curY, curD = q.popleft()
        nx, ny = curX, curY
        while True:
            time += 1
            nx += dx[curD]
            ny += dy[curD]
            if board[nx][ny] == 1 or board[nx][ny] == 3:
                return time
            if board[nx][ny] == 2:
                board[nx][ny] = 3
                snakes.append([nx, ny])
            elif board[nx][ny] == 0:
                board[nx][ny] = 3
                snakes.append([nx, ny])
                tailX, tailY = snakes.popleft()
                board[tailX][tailY] = 0
            if len(rotTimes) > 0 and rotTimes[0][0] == time:
                _, dir = rotTimes.popleft()
                if dir == 'D':
                    q.append([nx, ny, (curD + 1) % 4])
                else:
                    q.append([nx, ny, (curD - 1) % 4])
                break
    return time

if __name__ == "__main__":
    n = int(input())
    board = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(n + 2):
        board[i][0] = 1
        board[0][i] = 1
        board[n + 1][i] = 1
        board[i][n + 1] = 1
    k = int(input())
    for _ in range(k):
        x, y = map(int, input().split())
        board[x][y] = 2 # 사과
    l = int(input())
    rotTimes = deque()
    for _ in range(l):
        s, d = input().split()
        rotTimes.append([int(s), d])
    time = start()
    
    print(time)