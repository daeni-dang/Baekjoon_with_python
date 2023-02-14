def solution(s):
    answer = 0
    same, diff = 0, 0
    first = s[0]
    for i in range(len(s)):
        if s[i] == first:
            same += 1
        else:
            diff += 1
        if same == diff:
            answer += 1
            same = 0
            diff = 0
            if i + 1 >= len(s):
                break
            first = s[i + 1]
        if i == len(s) - 1 and same != diff:
            answer += 1
    return answer