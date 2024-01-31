import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b, graph):
    q = deque([[a, 0]])
    visited = [False] * len(graph)
    while q:
        cur, dist = q.popleft()
        for next in graph[cur]:
            if next == b:
                return dist + 1
            if not visited[next]:
                visited[next] = True
                q.append([next, dist + 1])
    return -1

def main():
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    print(bfs(a, b, graph))

if __name__ == "__main__":
    main()