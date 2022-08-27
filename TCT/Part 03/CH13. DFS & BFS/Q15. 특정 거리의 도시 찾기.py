from collections import deque
import sys

def bfs(dist, graph, v):
    answer = []
    q = deque()
    q.append(v)
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if dist[i] == -1:
                dist[i] = dist[cur] + 1
                q.append(i)
    for i in range(len(dist)):
        if dist[i] == k:
            answer.append(i)
    return answer

n, m, k, x = map(int, input().split())
graph = {}
for i in range(n):
    graph[i + 1] = []
for i in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph[tmp[0]].append(tmp[1])

dist = [-1] * (n + 1)
dist[x] = 0
city = bfs(dist, graph, x)
if len(city) == 0:
    print(-1)
else:
    city.sort()
    for i in city:
        sys.stdout.write(str(i)+'\n')