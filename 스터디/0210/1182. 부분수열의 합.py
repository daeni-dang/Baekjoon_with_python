import sys
input = sys.stdin.readline

def back(sums, depth, N, S, nums):
    global answer
    if len(arr) > 0 and sum(arr) == S:
        answer += 1
    if depth == N:
        return
    for i in range(depth, N):
        arr.append(nums[i])
        back(sums + nums[i], i + 1, N, S, nums)
        arr.pop()

def solution(N, S, nums):
    global answer
    back(0, 0, N, S, nums)
    return answer

def main():
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solution(N, S, nums))

if __name__ == "__main__":
    arr = []
    answer = 0
    main()