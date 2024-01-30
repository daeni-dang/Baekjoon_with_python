import sys
from collections import deque
input = sys.stdin.readline

def solution(F, S, G, U, D):
    if (S > G and D == 0) or (S < G and U == 0):
        return "use the stairs"
    answer = 0
    if S > G:
        answer += ((S - G) // D)
        G = G + (((S - G) // D) * D)
    else:
        answer += ((G - S) // U)
        S = S + (((G - S) // U) * U)
    if S == G:
        return answer
    visited = [False] * (F + 1)
    q = deque([[S, 0]])
    while q:
        cur, dist = q.popleft()
        up = cur + U
        down = cur - D
        if up == G or down == G:
            return answer + dist + 1
        if up <= F and not visited[up]:
            visited[up] = True
            q.append([up, dist + 1])
        if down > 0 and not visited[down]:
            visited[down] = True
            q.append([down, dist + 1])
    return "use the stairs"

def main():
    F, S, G, U, D = map(int, input().split())
    print(solution(F, S, G, U, D))

if __name__ == "__main__":
    main()