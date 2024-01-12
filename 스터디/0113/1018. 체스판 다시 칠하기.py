import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(input().strip()))
    answer = 1e9
    for i in range(n - 7):
        for j in range(m - 7):
            startWhite, startBlack = 0, 0
            for x in range(8):
                for y in range(8):
                    if (i + x + j + y) % 2 == 0:
                        if board[i + x][j + y] != 'W':
                            startWhite += 1
                        else:
                            startBlack += 1
                    if (i + x + j + y) % 2 == 1:
                        if board[i + x][j + y] != 'B':
                            startWhite += 1
                        else:
                            startBlack += 1
            answer = min(answer, min(startWhite, startBlack))
    print(answer)


if __name__ == "__main__":
    main()