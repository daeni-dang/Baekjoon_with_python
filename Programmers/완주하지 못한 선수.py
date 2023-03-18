from collections import defaultdict

def solution(participant, completion):
    answer = ''
    part_dict = defaultdict(int)
    for i in participant:
        part_dict[i] += 1
    for i in completion:
        part_dict[i] -= 1
    for i in part_dict:
        if part_dict[i] != 0:
            answer = i
            break
    return answer