N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
tmp = []

def solution(depth):
    if depth == M:
        print(' '.join(map(str, tmp)))
        return
    for i in range(N):
        if arr[i] not in tmp:
            tmp.append(arr[i])
            solution(depth + 1)
            tmp.pop()

solution(0)