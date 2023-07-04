import sys
input = sys.stdin.readline

answer = ""
def solution(x, y, N):
    global answer
    color = board[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if board[i][j] != color:
                answer += "("
                solution(x, y, N // 2)
                solution(x, y + N // 2, N // 2)
                solution(x + N // 2, y, N // 2)
                solution(x + N // 2, y + N // 2, N // 2)
                answer += ")"
                return
    answer += str(color)

if __name__ == "__main__":
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, list(input().strip()))))
    
    solution(0, 0, N)
    print(answer)