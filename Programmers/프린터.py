from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for idx, i in enumerate(priorities):
        queue.append([i, idx])
    cnt = 0
    while queue:
        flag = True
        cur = queue.popleft()
        for j in queue:
            if cur[0] < j[0]:
                queue.append(cur)
                flag = False
                break
        if flag:
            cnt += 1
            if cur[1] == location:
                answer = cnt
                break
    return answer