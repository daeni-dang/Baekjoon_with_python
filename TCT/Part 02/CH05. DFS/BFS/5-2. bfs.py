from collections import deque

def bfs(graph, start, visited):
    visited[start] = True
    q = deque()
    q.append(start)
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)