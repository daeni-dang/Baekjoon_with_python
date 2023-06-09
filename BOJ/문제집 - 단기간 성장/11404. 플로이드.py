import sys
input = sys.stdin.readline

def floyd():
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[j][i] + dist[i][k] < dist[j][k]:
                    dist[j][k] = dist[j][i] + dist[i][k]

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    
    dist = [[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        dist[a - 1][b - 1] = min(dist[a - 1][b - 1], c)
    floyd()
    for i in range(n):
        for j in range(n):
            if dist[i][j] == float("inf"):
                dist[i][j] = 0
    [print(' '.join(map(str, d))) for d in dist]