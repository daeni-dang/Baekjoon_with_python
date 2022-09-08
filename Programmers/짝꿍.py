def solution(X, Y):
    answer = ''
    answer_tmp = []
    x_tmp = [0] * 10
    y_tmp = [0] * 10
    for i in X:
        x_tmp[int(i)] += 1
    for i in Y:
        y_tmp[int(i)] += 1
    for i in range(10):
        if x_tmp[i] != 0 and y_tmp[i] != 0:
            for j in range(min(x_tmp[i], y_tmp[i])):
                answer_tmp.append(str(i))
    if len(answer_tmp) == 0:
        answer_tmp.append('-1')
    count_zero = 0
    for i in range(len(answer_tmp)):
        if answer_tmp[i] == '0':
            count_zero += 1
    if count_zero == len(answer_tmp):
        answer_tmp.remove('0')
    answer_tmp.sort(reverse=True)
    answer = ''.join(answer_tmp)
    return answer