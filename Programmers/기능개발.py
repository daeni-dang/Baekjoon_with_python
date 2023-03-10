import math

def solution(progresses, speeds):
    answer = []
    serve = []
    for idx, i in enumerate(progresses):
        serve.append(math.ceil((100 - i) / speeds[idx]))
    cnt = 1
    cur = serve[0]
    for idx, i in enumerate(serve[1:]):
        if i > cur:
            cur = i
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
    return answer