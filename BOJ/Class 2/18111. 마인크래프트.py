import sys
input = sys.stdin.readline
    
if __name__ == "__main__":
    N, M, B = map(int, input().split())
    maxH, minH = 0, float("inf")
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))
        maxH = max(maxH, max(board[i]))
        minH = min(minH, min(board[i]))
    
    minCost, minHeight = float("inf"), 0
    for h in range(minH, maxH + 1):
        cost = 0
        up, down = 0, 0
        for i in range(N):
            for j in range(M):
                if board[i][j] > h:
                    down += board[i][j] - h
                else:
                    up += h - board[i][j]
        if up > down + B:
            continue
        cost = down * 2 + up
        if cost <= minCost:
            minCost = cost
            minHeight = h

    print(minCost, minHeight)