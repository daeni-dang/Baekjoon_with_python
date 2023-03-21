def solution(prices):
    answer = []
    for idx1, i in enumerate(prices):
        flag = True
        for j in range(idx1 + 1, len(prices)):
            if prices[j] < i:
                answer.append(j - idx1)
                flag = False
                break
        if flag:
            answer.append(len(prices) - 1 - idx1)
    return answer