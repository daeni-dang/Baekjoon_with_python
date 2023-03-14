from collections import defaultdict

def solution(genres, plays):
    answer = []
    pair = []
    count = defaultdict(int)
    for idx, i in enumerate(genres):
        count[i] += plays[idx]
    count = dict(sorted(count.items(), key=lambda x: -x[1]))
    for idx, i in enumerate(genres):
        pair.append([i, plays[idx], idx])
    pair.sort(key=lambda x: -x[1])
    for key, value in count.items():
        cnt = 0
        for i in pair:
            if i[0] == key:
                answer.append(i[2])
                cnt += 1
                if cnt == 2:
                    break
    return answer