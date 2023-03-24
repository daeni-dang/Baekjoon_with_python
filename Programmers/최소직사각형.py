def solution(sizes):
    answer = 0
    for size in sizes:
        size.sort()
    max_x = 0
    max_y = 0
    for i in sizes:
        if i[0] > max_x:
            max_x = i[0]
        if i[1] > max_y:
            max_y = i[1]
    answer = max_x * max_y
    return answer