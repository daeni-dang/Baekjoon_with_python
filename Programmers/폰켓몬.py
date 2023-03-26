def solution(nums):
    answer = 0
    set_num = set(nums)
    answer = min(len(nums) // 2, len(set_num))
    return answer