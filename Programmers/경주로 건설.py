from collections import deque

def solution(board):
    answer = 0
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    board = bfs(0, 0, board, moves)
    print(board)
    return answer

def bfs(x, y, board, moves):
    n = len(board)
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        if x >= n and y >= n:
            break
        for m in moves:
            nx = x + m[0]
            ny = y + m[1]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if board[nx][ny] == 0:
                    q.append([nx, ny])
                    board[nx][ny] = board[x][y] + 1
    return board