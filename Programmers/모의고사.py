def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0] * 3
    for idx, i in enumerate(answers):
        if i == supo1[idx % len(supo1)]:
            score[0] += 1
        if i == supo2[idx % len(supo2)]:
            score[1] += 1
        if i == supo3[idx % len(supo3)]:
            score[2] += 1
    for idx, i in enumerate(score):
        if i == max(score):
            answer.append(idx + 1)
    return answer