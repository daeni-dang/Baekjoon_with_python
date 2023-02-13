def solution(s, skip, index):
    answer = ''
    alp = ""
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) not in skip:
            alp += chr(i)
    for i in s:
        for j in range(len(alp)):
            if i == alp[j]:
                idx = j
        answer += alp[(idx + index) % len(alp)]
    return answer