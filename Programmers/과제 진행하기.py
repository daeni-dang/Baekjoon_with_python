def solution(plans):
    answer = []
    # plans 시간 전처리
    for i in range(len(plans)):
        hour, minute = plans[i][1].split(":")
        plans[i][1] = int(hour) * 60 + int(minute)
        plans[i][2] = int(plans[i][2])
    # plans 시작시간 순서로 정렬
    plans.sort(key=lambda x: x[1])
    
    # 과제 시작
    stack = []  # 미완료 과제 저장
    for i in range(1, len(plans)):
        # 현재 과제 시작 시간이 이전 과제 종료 시간보다 늦는 경우. 이전 과제 수행 완료
        prevEnd = plans[i - 1][1] + plans[i - 1][2]
        if plans[i][1] >= prevEnd:
            answer.append(plans[i - 1][0])
            if plans[i][1] > prevEnd and stack:
                space = plans[i][1] - prevEnd
                while space > 0 and stack:
                    name, left = stack.pop()
                    if space >= left:
                        answer.append(name)
                    else:
                        stack.append([name, left - space])
                    space -= left
        # 이전 과제를 멈추는 경우
        else:
            # 스택에 이전 과제 이름, 남은 시간 저장
            stack.append([plans[i - 1][0], plans[i - 1][2] - (plans[i][1] - plans[i - 1][1])])
    
    answer.append(plans[-1][0])
    while stack:
        answer.append(stack.pop()[0])
    return answer