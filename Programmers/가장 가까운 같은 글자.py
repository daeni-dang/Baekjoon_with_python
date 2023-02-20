def solution(s):
    answer = []
    for idx, i in enumerate(s):
        flag = False
        for j in range(idx - 1, -1, -1):
            if i == s[j]:
                answer.append(idx - j)
                flag = True
                break
        if not flag:
            answer.append(-1)
            
    return answer