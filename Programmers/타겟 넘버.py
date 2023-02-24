def solution(numbers, target):
    answer = 0
    def dfs(idx, num):
        nonlocal answer
        if idx == len(numbers):
            if num == target:
                answer += 1
            return
        dfs(idx + 1, num + numbers[idx])
        dfs(idx + 1, num - numbers[idx])
    dfs(0, 0)
    return answer