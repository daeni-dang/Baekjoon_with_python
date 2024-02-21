import sys
import heapq
input = sys.stdin.readline

def dijkstra(s):
    dist = [1e9] * (N + 1)
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0
    while q:
        curDist, curNode = heapq.heappop(q)
        if curDist > dist[curNode]:
            continue
        for nextNode, nextDist in graph[curNode]:
            if curDist + nextDist < dist[nextNode]:
                dist[nextNode] = curDist + nextDist
                heapq.heappush(q, (curDist + nextDist, nextNode))
    return dist[1:]

def solution():
    answer = 0
    dist = dijkstra(1)
    dist = dijkstra(dist.index(max(dist)) + 1)
    answer = max(answer, max(dist))
    return answer

def main():
    global graph, N
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N):
        s, *arr, _ = list(map(int, input().split()))
        for i in range(0, len(arr), 2):
            graph[s].append((arr[i], arr[i + 1]))
    print(solution())

if __name__ == "__main__":
    graph = []
    N = 0
    main()