import sys
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
answer1, answer2, answer3 = 0, 0, 0

def solution(x, y, N):
    global answer1, answer2, answer3

    first = board[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if board[i][j] != first:
                for k in range(3):
                    for l in range(3):
                        solution(x + k * N // 3, y + l * N // 3, N // 3)
                return
    if first == -1:
        answer1 += 1
    elif first == 0:
        answer2 += 1
    else:
        answer3 += 1
solution(0, 0, N)
print(answer1)
print(answer2)
print(answer3)