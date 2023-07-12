from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque([[A, '']])
    visited = [False] * 10000
    visited[A] = True
    while q:
        n, op = q.popleft()
        if n == B:
            return op
        num = (n * 2) % 10000
        if not visited[num]:
            q.append([num, op + 'D'])
            visited[num] = True
        num = (n - 1) % 10000
        if not visited[num]:
            q.append([num, op + "S"])
            visited[num] = True
        num = (n // 1000) + (n % 1000) * 10
        if not visited[num]:
            q.append([num, op + "L"])
            visited[num] = True
        num = (n // 10) + (n % 10) * 1000
        if not visited[num]:
            q.append([num, op + "R"])
            visited[num] = True

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        minimum = 1e9
        answer = ""
        A, B = map(int, input().split())
        print(bfs())