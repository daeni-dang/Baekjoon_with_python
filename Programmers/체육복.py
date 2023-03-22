def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    dup = []
    for i in lost:
        if i in reserve:
            dup.append(i)
    nlost = []
    nreserve = []
    for i in lost:
        if i not in dup:
            nlost.append(i)
    for i in reserve:
        if i not in dup:
            nreserve.append(i)
    answer = n - len(nlost)
    for i in range(len(nlost)):
        for j in range(len(nreserve)):
            if nlost[i] - 1 == nreserve[j] or nlost[i] + 1 == nreserve[j]:
                answer += 1
                nreserve[j] = -1
                break
    return answer