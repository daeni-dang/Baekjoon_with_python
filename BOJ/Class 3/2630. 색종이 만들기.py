import sys
input = sys.stdin.readline

white, blue = 0, 0

def solution(x, y, N):
    global white, blue
    color = board[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if board[i][j] != color:
                solution(x, y, N // 2)
                solution(x, y + N // 2, N // 2)
                solution(x + N // 2, y, N // 2)
                solution(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        white += 1
        return
    else:
        blue += 1
        return

if __name__ == "__main__":
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    solution(0, 0, N)
    print(white)
    print(blue)