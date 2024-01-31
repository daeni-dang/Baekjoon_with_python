def dfs(x, y, depth, cost):
    print(x, y)
    global answer
    if depth == 3:
        answer = max(answer, cost)
        print(answer)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, cost + board[nx][ny])
            print("visi", nx, ny, depth)
            visited[nx][ny] = False

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[False] * M for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, 0, board[i][j])
                visited[i][j] = False
    print(answer)