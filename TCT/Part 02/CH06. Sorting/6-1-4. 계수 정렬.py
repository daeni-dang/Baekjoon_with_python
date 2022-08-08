array = list(map(int, input().split()))

def counting_sort(array):
    answer = []
    record = [0] * (max(array) + 1)
    for i in array:
        record[i] += 1
    for i in range(len(record)):
        for _ in range(record[i]):
            answer.append(i)
    return answer

print(counting_sort(array))