def solution(N, stages):
    answer = []
    player = len(stages)
    current = [0] * (N + 2)
    challenge = [0] * (N + 2)

    for i in range(player):
        current[stages[i]] += 1
        for j in range(1, stages[i] + 1):
            challenge[j] += 1

    fail = []
    for i in range(1, N + 1):
        tmp = []
        tmp.append(i)
        if challenge[i] == 0:
            tmp.append(0)
            fail.append(tmp)
        else:
            tmp.append(current[i] / challenge[i])
            fail.append(tmp)
    fail.sort(key=lambda x : -x[1])
    for i in fail:
        answer.append(i[0])
    return answer