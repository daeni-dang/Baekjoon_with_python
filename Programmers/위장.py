def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    tmp = len(score) % m
    for i in range(0, len(score) - tmp, m):
        answer += (score[i + m - 1]) * m
    return answer