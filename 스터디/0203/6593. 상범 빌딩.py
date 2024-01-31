import sys
from collections import deque
input = sys.stdin.readline

def findStart(l, r, c, building):
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == 'S':
                    return i, j, k

def solution(l, r, c, building):
    dx = [0, 0, 0, 0, 1, -1]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [1, -1, 0, 0, 0, 0]
    sx, sy, sz = findStart(l, r, c, building)
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    
    q = deque([[sx, sy, sz, 0]])
    visited[sx][sy][sz] = True
    while q:
        cx, cy, cz, dist = q.popleft()
        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nz = cz + dz[i]
            if nx >= l or nx < 0 or ny >= r or ny < 0 or nz >= c or nz < 0:
                continue
            if visited[nx][ny][nz]:
                continue
            visited[nx][ny][nz] = True
            if building[nx][ny][nz] == 'E':
                return dist + 1
            if building[nx][ny][nz] == '.':
                q.append([nx, ny, nz, dist + 1])
    return -1

def main():
    while True:
        l, r, c = map(int, input().split())
        if l == 0 and r == 0 and c == 0:
            break
        building = []
        for _ in range(l):
            tmp = []
            for _ in range(r + 1):
                line = list(input().strip())
                if len(line) != 0:
                    tmp.append(line)
            building.append(tmp)
        minute = solution(l, r, c, building)
        if minute == -1:
            print("Trapped!")
        else:
            print("Escaped in", minute, "minute(s).")

if __name__ == "__main__":
    main()