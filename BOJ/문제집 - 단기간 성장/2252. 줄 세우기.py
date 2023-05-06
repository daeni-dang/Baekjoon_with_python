from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    answer = []
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    
    for i in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        indegree[B] += 1

    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        tmp = q.popleft()
        answer.append(tmp)
        for i in graph[tmp]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    print(" ".join(map(str, answer)))