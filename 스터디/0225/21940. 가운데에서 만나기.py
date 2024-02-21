import sys
input = sys.stdin.readline

def floydWarshall(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i][j] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    

def solution(N, K, cities):
    answer = []
    floydWarshall(N)
    distToEach = [0] * N    # 1번부터 N번 노드까지 오는 데 걸리는 최대 시간
    for i in range(N):
        for city in cities:
            distToEach[i] = max(distToEach[i], dist[city - 1][i] + dist[i][city - 1])
    minValue = 1e9
    for i in range(N):
        if distToEach[i] < minValue:
            minValue = distToEach[i]
    for i in range(N):
        if distToEach[i] == minValue:
            answer.append(i + 1)
    return sorted(answer)
    

def main():
    global dist
    N, M = map(int, input().split())
    dist = [[1e9] * N for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        dist[a - 1][b - 1] = t
    K = int(input())
    cities = list(map(int, input().split()))
    print(' '.join(map(str, solution(N, K, cities))))

if __name__ == "__main__":
    dist = []
    main()