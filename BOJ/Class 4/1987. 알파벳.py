import sys
input = sys.stdin.readline

def dfs(x, y, depth):
    global answer
    answer = max(answer, depth)
    if depth == r * c:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= r or nx < 0 or ny >= c or ny < 0:
            continue
        if alp[ord(board[nx][ny]) - 65] == 0:
            alp[ord(board[nx][ny]) - 65] = 1
            dfs(nx, ny, depth + 1)
            alp[ord(board[nx][ny]) - 65] = 0

if __name__ == "__main__":
    answer = 0
    r, c = map(int, input().split())
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    board = []
    alp = [0] * 26
    for _ in range(r):
        board.append(list(input().strip()))
    alp[ord(board[0][0]) - 65] = 1
    dfs(0, 0, 1)
    print(answer)