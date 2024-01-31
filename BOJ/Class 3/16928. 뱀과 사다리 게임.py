from collections import defaultdict, deque
N, M = map(int, input().split())
s = defaultdict(int)
for _ in range(N + M):
    a, b = map(int, input().split())
    s[a] = b

q = deque([[1, 0]])
visited = [0] * 101
visited[1] = 1
while q:
    cur, dist = q.popleft()
    for i in range(1, 7):
        next = cur + i
        if next > 100:
            break
        if s[next] != 0:
            next = s[next]
        if not visited[next]:
            visited[next] = dist + 1
            q.append([next, dist + 1])
print(visited[100])