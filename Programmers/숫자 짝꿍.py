def solution(X, Y):
    answer = ''
    max_Y = int(max(Y))
    Y_list = [0] * (max_Y + 1)
    for i in Y:
        Y_list[int(i)] += 1
    for i in X:
        if int(i) <= max_Y:
            if Y_list[int(i)] != 0:
                answer += i
                Y_list[int(i)] -= 1
    if not answer:
        return "-1"
    cnt = 0
    for i in answer:
        if i == "0":
            cnt += 1
    if cnt == len(answer):
        return "0"
    answer = sorted(answer, reverse=True)
    answer = "".join(answer)
    return answer