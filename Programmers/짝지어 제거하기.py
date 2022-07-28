def solution(s):
    answer = -1
    stack = []
    for c in s:
        if len(stack) > 0 and c == stack[-1]:
            stack.pop()
        else: stack.append(c)
    if (len(stack) == 0):
        answer = 1
    else: answer = 0
    return answer