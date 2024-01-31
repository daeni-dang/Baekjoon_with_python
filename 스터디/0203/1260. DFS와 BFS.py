import sys
from collections import deque
input = sys.stdin.readline

def dfs(v, graph, visited):
    print(v, end=" ")
    for next in graph[v]:
        if not visited[next]:
            visited[next] = True
            dfs(next, graph, visited)

def bfs(v, graph):
    visited = [False] * len(graph)
    q = deque([v])
    visited[v] = True
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

def main():
    n, m, v = map(int, input().split())
    graph = [set() for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    for i in range(n + 1):
        graph[i] = sorted(list(graph[i]))
    visited = [False] * (n + 1)
    visited[v] = True
    dfs(v, graph, visited)
    print()
    bfs(v, graph)

if __name__ == "__main__":
    main()