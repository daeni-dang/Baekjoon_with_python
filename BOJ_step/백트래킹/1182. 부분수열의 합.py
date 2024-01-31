from collections import deque

N, S = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
arr = []

def solution(n, idx):
    global answer
    if len(arr) > 0 and sum(arr) == S:
        answer += 1
    if idx == N:
        return
    for i in range(idx, N):
        arr.append(nums[i])
        solution(n + nums[i], i + 1)
        arr.pop()

solution(0, 0)
print(answer)