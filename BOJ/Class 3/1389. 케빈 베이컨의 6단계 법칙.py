from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

minimum = 1e9
answer = 0
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    visited[i] = -1
    q = deque([[i, 0]])
    while q:
        cur, dist = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = dist + 1
                q.append([next, dist + 1])

    for j in range(1, N + 1):
        if visited[j] == -1:
            visited[j] = 0
    if sum(visited) < minimum:
        minimum = sum(visited)
        answer = i
print(answer)
