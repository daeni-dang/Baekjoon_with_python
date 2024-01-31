N, M = map(int, input().split())

arr = []

def solution(s):
    if len(arr) == M:
        print(' '.join(arr))
        return
    for i in range(s, N + 1):
        if str(i) not in arr:
            arr.append(str(i))
            solution(i + 1)
            arr.pop()

solution(1)