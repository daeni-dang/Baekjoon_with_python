from collections import deque
n, m = map(int, input().split())

maze = [list(map(int, input())) for _ in range(n)]
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 상, 하, 좌, 우

def bfs(x, y):
    global answer, n, m
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        if x + 1 == n and y + 1 == m:
            break
        for move in moves:
            new_x = x + move[0]
            new_y = y + move[1]
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                continue
            if maze[new_x][new_y] == 1:
                q.append([new_x, new_y])
                maze[new_x][new_y] = maze[x][y] + 1
    return maze[n - 1][m - 1]

print(bfs(0, 0))