def solution(array):
    answer = 0
    for i in array:
        str_i = str(i)
        for j in str_i:
            if j == '7':
                answer += 1
    return answer