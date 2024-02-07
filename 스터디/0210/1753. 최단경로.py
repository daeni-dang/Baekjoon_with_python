import sys
import heapq
input = sys.stdin.readline

def solution(V, start, graph):
    q = []
    dist = [1e9] * (V + 1)
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        curDist, curNode = heapq.heappop(q)
        for nextNode, nextDist in graph[curNode]:
            if dist[nextNode] < nextDist:
                continue
            if curDist + nextDist < dist[nextNode]:
                dist[nextNode] = curDist + nextDist
                heapq.heappush(q, (curDist + nextDist, nextNode))
    return dist[1:]

def main():
    V, E = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    dist = solution(V, start, graph)
    for d in dist:
        print(d if d != 1e9 else "INF")

if __name__ == "__main__":
    main()