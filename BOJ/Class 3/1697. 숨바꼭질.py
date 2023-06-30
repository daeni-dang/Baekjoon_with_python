from collections import deque

N, K = map(int, input().split())

q = deque([[N, 0]])
visited = [False] * 100001

while q:
    cur, depth = q.popleft()
    if cur == K:
        print(depth)
        break
    for next in (cur - 1, cur + 1, cur * 2):
        if 0 <= next <= 100000 and not visited[next]:
            q.append([next, depth + 1])
            visited[next] = True
