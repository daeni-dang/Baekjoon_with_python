import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(graph, start):
    dist = [INF for _ in range(n + 1)]
    dist[start] = 0
    q = []
    heapq.heappush(q, (dist[start], start))
    
    while q:
        curDist, curNode = heapq.heappop(q)
        if dist[curNode] < curDist:
            continue
        for nextDist, nextNode in graph[curNode]:
            newDist = curDist + nextDist
            if newDist < dist[nextNode]:
                dist[nextNode] = newDist
                heapq.heappush(q, (newDist, nextNode))
    return dist

if __name__ == "__main__":
    n, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))
    v1, v2 = map(int, input().split())
    
    
    # 1에서 출발
    dist_1 = dijkstra(graph, 1)
    
    # v1에서 출발
    dist_v1 = dijkstra(graph, v1)
    
    # v2에서 출발
    dist_v2 = dijkstra(graph, v2)
    
    result1 = dist_1[v1] + dist_v1[v2] + dist_v2[n]
    result2 = dist_1[v2] + dist_v2[v1] + dist_v1[n]
    
    answer = min(result1, result2)
    print(answer if answer < INF else -1)