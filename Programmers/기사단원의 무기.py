def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        cnt = set()
        for j in range(1, int(i ** (1/2)) + 1):
            if i % j == 0:
                cnt.add(j)
                cnt.add(i // j)
        if len(cnt) > limit:
            answer += power
        else:
            answer += len(cnt)
    return answer