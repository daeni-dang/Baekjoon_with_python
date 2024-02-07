import sys
import heapq
input = sys.stdin.readline

def solution(N, graph, start, end):
    q = []
    heapq.heappush(q, (0, start))
    dist = [1e9] * (N + 1)
    dist[start] = 0
    while q:
        curDist, curNode = heapq.heappop(q)
        if curDist > dist[curNode]:
            continue
        for nextNode, nextDist in graph[curNode]:
            if curDist + nextDist < dist[nextNode]:
                dist[nextNode] = curDist + nextDist
                heapq.heappush(q, (curDist + nextDist, nextNode))
    return dist[end]

def main():
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    start, end = map(int, input().split())
    print(solution(N, graph, start, end))

if __name__ == "__main__":
    main()