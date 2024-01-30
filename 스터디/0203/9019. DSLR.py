import sys
from collections import deque
input = sys.stdin.readline

def solution(A, B):
    visited = [False] * 10001
    visited[A] = True
    q = deque([[A, ""]])
    while q:
        cur, op = q.popleft()
        if cur == B:
            return op
        D = (cur * 2) % 10000
        if not visited[D]:
            visited[D] = True
            q.append([D, op + "D"])
        S = (cur - 1) % 10000
        if not visited[S]:
            visited[S] = True
            q.append([S, op + "S"])
        L = 10 * (cur % 1000) + (cur // 1000)
        if not visited[L]:
            visited[L] = True
            q.append([L, op + "L"])
        R = (cur % 10) * 1000 + (cur // 10)
        if not visited[R]:
            visited[R] = True
            q.append([R, op + "R"])

def main():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        print(solution(A, B))

if __name__ == "__main__":
    main()