def solution(common):
    answer = 0
    diff = []
    set_tmp = set()
    for i in range(1, len(common)):
        diff.append(common[i] - common[i - 1])
        set_tmp.add(common[i] - common[i - 1])
    if len(set_tmp) == 1: # 등차수열
        print(len(common) - 1)
        answer = common[len(common) - 1] + diff[0]
    else: # 등비수열
        answer = common[len(common) - 1] * (diff[len(diff) - 1] // diff[len(diff) - 2])
    return answer