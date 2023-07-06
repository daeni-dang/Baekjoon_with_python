import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
visited = [False] * (N + 1)
visited[1] = True

while q:
    cur = q.popleft()
    for next in graph[cur]:
        if not visited[next]:
            visited[next] = True
            q.append(next)
cnt = 0
for i in range(2, N + 1):
    if visited[i]:
        cnt += 1
print(cnt)