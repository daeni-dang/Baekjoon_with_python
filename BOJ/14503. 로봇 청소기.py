import sys
input = sys.stdin.readline

def checkSide(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if board[nx][ny] == 0:
            return True
    return False

def dfs(x, y, d):
    global answer
    if board[x][y] == 0:
        board[x][y] = 2
        answer += 1
    if not checkSide(x, y):
        nd = (d + 2) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if nx < n and nx >= 0 and ny < m and ny >= 0:
            if board[nx][ny] != 1:
                return dfs(nx, ny, d)
            else:
                return
    else:
        for i in range(1, 5):
            nd = (d - i) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if board[nx][ny] == 0:
                return dfs(nx, ny, nd)

if __name__ == "__main__":
    answer = 0
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dfs(r, c, d)
    print(answer)