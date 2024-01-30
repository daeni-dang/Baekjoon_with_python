import sys
from collections import deque
input = sys.stdin.readline

def solution(N, K):
    if N == K:
        return 0
    visited = [False] * 200001
    visited[N] = True
    q = deque([[N, 0]])
    while q:
        cur, dist = q.popleft()
        if cur + 1 == K or cur - 1 == K or cur * 2 == K:
            return dist + 1
        if cur + 1 <= 100001 and not visited[cur + 1]:
            visited[cur + 1] = True
            q.append([cur + 1, dist + 1])
        if 0 <= cur - 1 <= 100001 and not visited[cur - 1]:
            visited[cur - 1] = True
            q.append([cur - 1, dist + 1])
        if cur * 2 <= 200001 and not visited[cur *2]:
            visited[cur * 2] = True
            q.append([cur * 2, dist + 1])

def main():
    N, K = map(int, input().split())
    print(solution(N, K))

if __name__ == "__main__":
    main()