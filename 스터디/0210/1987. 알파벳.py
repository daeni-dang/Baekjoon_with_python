import sys
input = sys.stdin.readline

def dfs(x, y, board, depth, R, C, alps):
    global answer
    answer = max(answer, depth)
    if depth == R * C:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= R or nx < 0 or ny >= C or ny < 0:
            continue
        if alps[ord(board[nx][ny]) - 65] == 0:
            alps[ord(board[nx][ny]) - 65] = 1
            dfs(nx, ny, board, depth + 1, R, C, alps)
            alps[ord(board[nx][ny]) - 65] = 0

def solution(R, C, board):
    alps = [0] * 26
    alps[ord(board[0][0]) - ord('A')] = 1
    dfs(0, 0, board, 1, R, C, alps)
    return answer

def main():
    global visited
    R, C = map(int, input().split())
    board = []
    for _ in range(R):
        board.append(list(input().strip()))
    print(solution(R, C, board))

if __name__ == "__main__":
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    alps = []
    answer = 0
    main()