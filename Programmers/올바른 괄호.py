def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        if i == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False