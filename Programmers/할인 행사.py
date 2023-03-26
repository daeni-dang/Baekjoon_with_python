def solution(want, number, discount):
    answer = 0
    want10 = []
    for i in range(len(want)):
        for j in range(number[i]):
            want10.append(want[i])
    want10.sort()
    for i in range(len(discount) - 9):
        if sorted(discount[i:i+10]) == want10:
            answer += 1
    return answer
