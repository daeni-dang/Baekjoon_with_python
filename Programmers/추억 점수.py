def solution(name, yearning, photo):
    answer = []
    yearDict = {}
    for i in range(len(name)):
        yearDict[name[i]] = yearning[i]
    for p in photo:
        tmp = 0
        for j in p:
            try:
                tmp += yearDict[j]
            except:
                continue
        answer.append(tmp)
    return answer