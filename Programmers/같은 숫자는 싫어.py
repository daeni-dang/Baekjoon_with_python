def solution(arr):
    answer = []
    prev = arr[0]
    answer.append(prev)
    for i in arr[1:]:
        if i != prev:
            answer.append(i)
            prev = i
    return answer