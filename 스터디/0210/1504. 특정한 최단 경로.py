import sys
import heapq
input = sys.stdin.readline

def dijkstra(N, graph, start, end):
    q = []
    dist = [1e9] * (N + 1)
    dist[start] = 0
    heapq.heappush(q, (dist[start], start))
    while q:
        curDist, curNode = heapq.heappop(q)
        if curDist > dist[curNode]:
            continue
        for nextNode, nextDist in graph[curNode]:
            if dist[nextNode] > curDist + nextDist:
                dist[nextNode] = curDist + nextDist
                heapq.heappush(q, (curDist + nextDist, nextNode))
    return dist[end]

def solution(N, graph, v1, v2):
    answer = 0
    dist1 = dijkstra(N, graph, 1, v1)
    dist1 += dijkstra(N, graph, v1, v2)
    dist1 += dijkstra(N, graph, v2, N)
    dist2 = dijkstra(N, graph, 1, v2)
    dist2 += dijkstra(N, graph, v2, v1)
    dist2 += dijkstra(N, graph, v1, N)
    answer = min(dist1, dist2)
    return answer if answer < 1e9 else -1
                
def main():
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    v1, v2 = map(int, input().split())
    print(solution(N, graph, v1, v2))

if __name__ == "__main__":
    main()