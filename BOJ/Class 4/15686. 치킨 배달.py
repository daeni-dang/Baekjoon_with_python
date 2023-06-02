import sys
input = sys.stdin.readline

arr = []
answer = 1e9
def back(depth):
    global answer
    if depth == m:
        tmp = 0
        for hx, hy in house:
            findMin = 1e9
            for cx, cy in arr:
                findMin = min(findMin, abs(cx - hx) + abs(cy - hy))
            tmp += findMin
        answer = min(answer, tmp)
        return
    for cx, cy in chicken:
        if (cx, cy) not in arr\
                and (len(arr) == 0 or cx * n + cy > arr[-1][0] * n + arr[-1][1]):
            arr.append((cx, cy))
            back(depth + 1)
            arr.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    chicken = []
    house = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                chicken.append((i, j))
            elif board[i][j] == 1:
                house.append((i, j))

    back(0)
    print(answer)