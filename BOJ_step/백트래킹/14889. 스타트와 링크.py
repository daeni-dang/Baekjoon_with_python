N = int(input())
minimum = 1e9
visited = [False] * N

def solution(idx, depth):
    global minimum
    if depth == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += S[i][j]
                if not visited[i] and not visited[j]:
                    link += S[i][j]
        minimum = min(minimum, abs(start - link))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            solution(i + 1, depth + 1)
            visited[i] = False

S = []
for _ in range(N):
    S.append(list(map(int, input().split())))
solution(0, 0)
print(minimum)
