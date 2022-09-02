def balance(s):
    left, right = 0, 0
    u, v = '', ''
    for i in s:
        if (left == 0 and right == 0) or left != right:
            if i == '(':
                left += 1
            else:
                right += 1
            u += i
        else:
            v += i
    return u, v

def correct(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    return False

def solution(p):
    answer = ''
    if p == '':
        return answer
    u, v = balance(p)
    if correct(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]
        for i in u:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    return answer