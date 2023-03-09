from collections import deque

def check(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
        if diff > 1:
            return False
    return True

def solution(begin, target, words):
    if not target in words:
        return 0
    visited = []
    q = deque([[begin, 0]])
    while q:
        cur, dist = q.popleft()
        print(cur, dist)
        if cur == target:
            return dist
        for word in words:
            if check(cur, word) and word not in visited:
                q.append([word, dist + 1])
                visited.append(word)