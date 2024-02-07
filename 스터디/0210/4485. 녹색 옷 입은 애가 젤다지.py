import sys
import heapq
input = sys.stdin.readline

def solution(N, board):
    q = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dist = [[1e9] * N for _ in range(N)]
    dist[0][0] = board[0][0]
    heapq.heappush(q, (board[0][0], 0, 0))    # dist, x, y
    while q:
        curDist, cx, cy = heapq.heappop(q)
        if curDist > dist[cx][cy]:
            continue
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if dist[nx][ny] > curDist + board[nx][ny]:
                dist[nx][ny] = curDist + board[nx][ny]
                heapq.heappush(q, (curDist + board[nx][ny], nx, ny))
    return dist[N - 1][N - 1]

def main():
    t = 1
    while True:
        N = int(input())
        if N == 0: break
        board = []
        for _ in range(N):
            board.append(list(map(int, input().split())))
        print(f"Problem {t}: {solution(N, board)}")
        t += 1

if __name__ == "__main__":
    main()