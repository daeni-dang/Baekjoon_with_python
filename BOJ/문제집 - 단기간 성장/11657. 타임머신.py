import sys
input = sys.stdin.readline

INF = 1e9

def bellmanFord(start):
    dist[start] = 0
    for i in range(n):
        for a, b, c in edges:
            if dist[a] != INF and dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                if i == n - 1:
                    # 사이클 발생
                    return True
    return False

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append([a, b, c])
    
    dist = [INF] * (n + 1)
    status = bellmanFord(1)
    if status:
        print(-1)
    else:
        for i in range(2, n + 1):
            print(dist[i] if dist[i] != INF else -1)