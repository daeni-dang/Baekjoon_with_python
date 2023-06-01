import sys
input = sys.stdin.readline

def bellmanFord(start):
    dist = [10001] * (n + 1)
    dist[start] = 0
    for i in range(n):
        for s, e, t in edges:
            if dist[e] > t + dist[s]:
                dist[e] = t + dist[s]
                if i == n - 1:
                    return True
    return False

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, m, w = map(int, input().split())
        edges = []
        
        for _ in range(m):
            s, e, t = map(int, input().split())
            edges.append((s, e, t));
            edges.append((e, s, t))
        for _ in range(w):
            s, e, t = map(int, input().split())
            edges.append((s, e, -t))
        if bellmanFord(1): print("YES")
        else: print("NO")