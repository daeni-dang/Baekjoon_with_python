tmp = []

def solution(depth):
    if depth == 6:
        print(' '.join(map(str, tmp)))
        return
    for i in range(k):
        if len(tmp) == 0 or arr[i] > tmp[-1]:
            tmp.append(arr[i])
            solution(depth + 1)
            tmp.pop()

while True:
    k, *arr = map(int, input().split())
    if k == 0:
        break
    solution(0)
    print()
    