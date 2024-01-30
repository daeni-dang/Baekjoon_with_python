import sys
from collections import deque
input = sys.stdin.readline

def solution(N, T, G):
    if N == G:
        return 0
    visited = [False] * 100001
    visited[N] = True
    q = deque([[N, 0]])
    while q:
        cur, dist = q.popleft()
        if dist > T:
            return "ANG"
        if cur == G:
            return dist
        if cur + 1 < 100000 and not visited[cur + 1]:
            visited[cur + 1] = True
            q.append([cur + 1, dist + 1])
        if cur > 0 and cur * 2 < 100000:
            cur *= 2
            if len(str(cur)) == 1:
                Bnum = cur - 1
            else:
                Bnum = cur - (10 ** (len(str(cur)) - 1))
            if not visited[Bnum]:
                visited[Bnum] = True
                q.append([Bnum, dist + 1])
    return "ANG"

def main():
    N, T, G = map(int, input().split())
    print(solution(N, T, G))

if __name__ == "__main__":
    main()