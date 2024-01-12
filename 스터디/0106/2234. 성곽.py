import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, graph, visited):
    cnt = 1
    q = deque([[x, y]])
    while q:
        curX, curY = q.popleft()
        for nx, ny in graph[(curX * n + curY)]:
            if not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = True
                q.append([nx, ny])
    return cnt
            
def getSize(graph):
    visited = [[False] * n for _ in range(m)]
    rooms = []
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                rooms.append(bfs(i, j, graph, visited))
    return rooms

def removeWall(graph):
    dx = [0, -1, 0, 1]  # 서, 북, 동, 남
    dy = [-1, 0, 1, 0]
    maxRoom = 0
    for i in range(m):
        for j in range(n):
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if nx >= m or nx < 0 or ny >= n or ny < 0:
                    continue
                if [i + dx[k], j + dy[k]] not in graph[i * n + j]:
                    visited = [[False] * n for _ in range(m)]
                    if not visited[i][j]:
                        visited[i][j] = True
                        graph[i * n + j].append([i + dx[k], j + dy[k]])
                        maxRoom = max(maxRoom, bfs(i, j, graph, visited))
                        graph[i * n + j].pop()
                    del visited
    return maxRoom

def makeGraph(walls):
    dx = [0, -1, 0, 1]  # 서, 북, 동, 남
    dy = [-1, 0, 1, 0]
    graph = [[] for _ in range(n * m)]
    for i in range(m):
        for j in range(n):
            binWall = bin(walls[i][j])[2:].zfill(4)
            for k in range(3, -1, -1):
                nx, ny = i + dx[3 - k], j + dy[3 - k]
                if nx >= m or nx < 0 or ny >= n or ny < 0:
                    continue
                if binWall[k] == "0":
                    graph[(i * n + j)].append([nx, ny])
    return graph

if __name__ == "__main__":
    n, m = map(int, input().split())
    mostBig = 0
    walls = []
    for _ in range(m):
        walls.append(list(map(int, input().split())))
    graph = makeGraph(walls)
    rooms = getSize(graph)
    print(len(rooms))
    print(max(rooms))
    print(removeWall(graph))
