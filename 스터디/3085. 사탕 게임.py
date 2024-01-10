import sys
input = sys.stdin.readline

def calculate(board, n):
    cnt = 0
    for i in range(n):
        befRight = board[i][0]
        befDown = board[0][i]
        tmpRight, tmpDown = 0, 0
        for j in range(n):
            if board[i][j] != befRight:
                befRight = board[i][j]
                cnt = max(cnt, tmpRight)
                tmpRight = 0
            tmpRight += 1
        cnt = max(cnt, tmpRight)
        for j in range(n):
            if board[j][i] != befDown:
                befDown = board[j][i]
                cnt = max(cnt, tmpDown)
                tmpDown = 0
            tmpDown += 1
        cnt = max(cnt, tmpDown)
    return cnt

def main():
    answer = 0
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(input().strip()))
    for i in range(n):
        for j in range(n - 1):
            if i != n - 1:
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                answer = max(answer, calculate(board, n))
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            answer = max(answer, calculate(board, n))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
    print(answer)

if __name__ == "__main__":
    main()