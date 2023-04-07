def solution(sequence, k):
    answer = []
    candidate = []
    curSum = sequence[0]
    start, end = 0, 0
    lenSequence = len(sequence)
    
    while start <= end:
        if curSum < k:
            end += 1
            if end == lenSequence:
                break
            curSum += sequence[end]
        if curSum > k:
            curSum -= sequence[start]
            start += 1
        if curSum == k:
            candidate.append([end - start, start, end])
            curSum -= sequence[start]
            start += 1
    
    candidate.sort(key=lambda x: (x[0], x[1]))
    answer = candidate[0][1:]
    return answer