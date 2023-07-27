from collections import deque

def bfs(x, y):
    q = deque([x])
    visited = [False] * N
    visited[x] = True
    while q:
        cx = q.popleft()
        for nx in graph[cx]:
            if nx == y:
                return True
            if not visited[nx]:
                q.append(nx)
                visited[nx] = True
    return False

N = int(input())

graph = [[] for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            graph[i].append(j)

answer = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if bfs(i, j):
            answer[i][j] = 1
for i in answer:
    print(' '.join(map(str, i)))