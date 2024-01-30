import sys
from collections import deque
input = sys.stdin.readline

def solution(l, sx, sy, tx, ty):
    if sx == tx and sy == ty:
        return 0
    # 왼쪽 위 이동부터 시계방향
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    visited = [[False] * l for _ in range(l)]
    visited[sx][sy] = True
    q = deque([[sx, sy, 0]])
    while q:
        cx, cy, dist = q.popleft()
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= l or nx < 0 or ny >= l or ny < 0:
                continue
            if nx == tx and ny == ty:
                return dist + 1
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            q.append([nx, ny, dist + 1])
    

def main():
    T = int(input())
    for _ in range(T):
        l = int(input())
        sx, sy = map(int, input().split())
        tx, ty = map(int, input().split())
        print(solution(l, sx, sy, tx, ty))

if __name__ == "__main__":
    main()