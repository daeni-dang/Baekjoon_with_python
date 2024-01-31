N, M = map(int, input().split())

arr = []

def solution():
    if len(arr) == M:
        print(' '.join(arr))
        return
    for i in range(1, N + 1):
        arr.append(str(i))
        solution()
        arr.pop()

solution()