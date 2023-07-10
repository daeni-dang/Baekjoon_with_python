from collections import deque

def findZero(dist):
    answer = dist
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if arr[i][j][k] == 0:
                    answer = -1
                    return answer
    return answer

if __name__ == "__main__":
    n, m, h = map(int, input().split())
    arr = []
    for _ in range(h):
        tmp = []
        for _ in range(m):
            tmp.append(list(map(int, input().split())))
        arr.append(tmp)
    
    q = deque()
    cnt1 = 0
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if arr[i][j][k] == 1:
                    cnt1 += 1
                    q.append([i, j, k, 0])
    
    if cnt1 == 0:
        print(-1)
    else:
        dx = [0, 0, 1, -1, 0, 0]
        dy = [1, -1, 0, 0, 0, 0]
        dz = [0, 0, 0, 0, 1, -1]
        
        while q:
            z, x, y, dist = q.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if nx >= m or nx < 0 or ny >= n or ny < 0:
                    continue
                if nz >= h or nz < 0:
                    continue
                if arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = 1
                    q.append([nz, nx, ny, dist + 1])

        answer = findZero(dist)
        print(answer)