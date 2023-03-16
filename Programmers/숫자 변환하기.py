from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    memo = [0] * (y + 1)
    q = deque([x])
    while q:
        cur = q.popleft()
        if cur + n <= y and memo[cur + n] == 0:
            memo[cur + n] = memo[cur] + 1
            q.append(cur + n)
        if cur * 2 <= y and memo[cur * 2] == 0:
            memo[cur * 2] = memo[cur] + 1
            q.append(cur * 2)
        if cur * 3 <= y and memo[cur * 3] == 0:
            memo[cur * 3] = memo[cur] + 1
            q.append(cur * 3)
    if memo[y] == 0:
        return -1
    return memo[y]