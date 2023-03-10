def solution(keymap, targets):
    answer = [0] * len(targets)
    for i, target in enumerate(targets):
        min_find_idx = []
        for t in target:
            find_idx = []
            for k in keymap:
                tmp = k.find(t)
                if tmp != -1:
                    find_idx.append(tmp)
            if find_idx:
                min_find_idx.append(min(find_idx))
        if len(min_find_idx) < len(target):
            answer[i] = -1
        else: 
            answer[i] += sum(min_find_idx) + len(min_find_idx)
    return answer