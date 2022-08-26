def possible(answer):
    for x, y, a in answer:
        if a == 0: # 기둥
            if y == 0 or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer or [x, y, 1] in answer:
                continue
            return False
        else:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer:
                continue
            if [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
                continue
            return False
    return True
                

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, a, b = build
        if b == 1: # 설치
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])
        else:
            if [x, y, a] in answer:
                answer.remove([x, y, a])
                if not possible(answer):
                    answer.append([x, y, a])
    answer.sort()
    return answer